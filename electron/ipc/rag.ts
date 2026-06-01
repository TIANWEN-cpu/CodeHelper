import { ipcMain, dialog } from 'electron'
import { getDB } from '../db/index'
import { readFileSync } from 'fs'
import { basename, extname } from 'path'

export function registerRAGIPC() {
  ipcMain.handle('knowledge-upload', async () => {
    const result = await dialog.showOpenDialog({
      properties: ['openFile', 'multiSelections'],
      filters: [
        { name: '文档', extensions: ['txt', 'md', 'pdf'] }
      ]
    })

    if (result.canceled || result.filePaths.length === 0) return null

    const db = getDB()
    const uploaded: string[] = []

    for (const filePath of result.filePaths) {
      const filename = basename(filePath)
      const ext = extname(filePath).toLowerCase()
      let content = ''

      if (ext === '.txt' || ext === '.md') {
        content = readFileSync(filePath, 'utf-8')
      } else if (ext === '.pdf') {
        try {
          const pdfParse = require('pdf-parse')
          const buffer = readFileSync(filePath)
          const data = await pdfParse(buffer)
          content = data.text
        } catch (error) {
          throw new Error(`PDF 解析失败: ${error instanceof Error ? error.message : String(error)}`)
        }
      }

      // Split into chunks (~500 chars)
      const chunks = splitIntoChunks(content, 500)

      const docResult = db.prepare(
        'INSERT INTO knowledge_docs (filename, file_type, content, chunk_count) VALUES (?,?,?,?)'
      ).run(filename, ext, content, chunks.length)

      const docId = docResult.lastInsertRowid
      const insertChunk = db.prepare(
        'INSERT INTO knowledge_chunks (doc_id, content, chunk_index) VALUES (?,?,?)'
      )

      chunks.forEach((chunk, i) => {
        insertChunk.run(docId, chunk, i)
      })

      uploaded.push(filename)
    }

    return uploaded
  })

  ipcMain.handle('knowledge-list', () => {
    return getDB().prepare('SELECT id, filename, file_type, chunk_count, created_at FROM knowledge_docs ORDER BY created_at DESC').all()
  })

  ipcMain.handle('knowledge-delete', (_e, id: number) => {
    getDB().prepare('DELETE FROM knowledge_docs WHERE id = ?').run(id)
  })

  ipcMain.handle('knowledge-search', (_e, query: string) => {
    // Simple keyword search (no embedding for now)
    const keywords = query.toLowerCase().split(/\s+/).filter(k => k.length > 1)
    if (keywords.length === 0) return []

    const db = getDB()
    const allChunks = db.prepare('SELECT kc.*, kd.filename FROM knowledge_chunks kc JOIN knowledge_docs kd ON kc.doc_id = kd.id').all() as any[]

    // Score chunks by keyword matches
    const scored = allChunks.map(chunk => {
      const text = chunk.content.toLowerCase()
      let score = 0
      for (const kw of keywords) {
        const matches = (text.match(new RegExp(escapeRegExp(kw), 'g')) || []).length
        score += matches
      }
      return { ...chunk, score }
    }).filter(c => c.score > 0)

    scored.sort((a, b) => b.score - a.score)
    return scored.slice(0, 5)
  })
}

function splitIntoChunks(text: string, maxLen: number): string[] {
  const chunks: string[] = []
  const paragraphs = text.split(/\n\n+/)
  let current = ''

  for (const para of paragraphs) {
    if ((current + '\n\n' + para).length > maxLen && current) {
      chunks.push(current.trim())
      current = para
    } else {
      current = current ? current + '\n\n' + para : para
    }
  }
  if (current.trim()) chunks.push(current.trim())
  return chunks.length ? chunks : ['']
}

function escapeRegExp(input: string) {
  return input.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
}
