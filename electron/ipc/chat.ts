import { ipcMain } from 'electron'
import { getDB } from '../db/index'

const BUILTIN_PRESETS = [
  { name: '通用助手', prompt: '你是一个友好的AI助手，请用中文回答问题。' },
  { name: '代码专家', prompt: '你是一个资深编程专家，擅长代码审查、调试和优化。请用中文回答，给出代码时附带注释。' },
  { name: '面试官', prompt: '你是一个技术面试官，会针对编程和算法提出问题，评估回答质量，并给出改进建议。请用中文交流。' },
  { name: '学习导师', prompt: '你是一个耐心的编程学习导师，善于用简单的语言解释复杂概念，会循序渐进地引导学习。请用中文教学。' },
]

export interface MemoryRow {
  id: number
  content: string
  category: string
  source: string
  source_ref: string | null
  pinned: number
  enabled: number
  confidence: number
  created_at: string
  updated_at: string
  last_used_at: string | null
}

interface MemoryInput {
  id?: number
  content: string
  category?: string
  source?: string
  source_ref?: string
  pinned?: number | boolean
  enabled?: number | boolean
  confidence?: number
}

export function registerChatIPC() {
  const db = getDB()

  const presetCount = (db.prepare('SELECT COUNT(*) as c FROM prompt_presets WHERE is_builtin = 1').get() as { c: number }).c
  if (presetCount === 0) {
    const stmt = db.prepare('INSERT INTO prompt_presets (name, prompt, is_builtin) VALUES (?,?,1)')
    for (const preset of BUILTIN_PRESETS) {
      stmt.run(preset.name, preset.prompt)
    }
  }

  ipcMain.handle('chat-sessions-list', () => {
    return db.prepare('SELECT * FROM chat_sessions ORDER BY updated_at DESC').all()
  })

  ipcMain.handle('chat-session-create', (_e, args: { id: string; title?: string; system_prompt?: string }) => {
    db.prepare('INSERT INTO chat_sessions (id, title, system_prompt) VALUES (?,?,?)').run(
      args.id, args.title || '新对话', args.system_prompt || '',
    )
    return db.prepare('SELECT * FROM chat_sessions WHERE id = ?').get(args.id)
  })

  ipcMain.handle('chat-session-update', (_e, id: string, updates: { title?: string; system_prompt?: string }) => {
    if (updates.title !== undefined) {
      db.prepare('UPDATE chat_sessions SET title = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?').run(updates.title, id)
    }
    if (updates.system_prompt !== undefined) {
      db.prepare('UPDATE chat_sessions SET system_prompt = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?').run(updates.system_prompt, id)
    }
  })

  ipcMain.handle('chat-session-delete', (_e, id: string) => {
    db.prepare('DELETE FROM chat_history WHERE session_id = ?').run(id)
    db.prepare('DELETE FROM chat_sessions WHERE id = ?').run(id)
  })

  ipcMain.handle('chat-messages-load', (_e, sessionId: string) => {
    return db.prepare('SELECT * FROM chat_history WHERE session_id = ? ORDER BY created_at ASC, id ASC').all(sessionId)
  })

  ipcMain.handle('chat-message-save', (_e, msg: { session_id: string; role: string; content: string; model?: string }) => {
    db.prepare('INSERT INTO chat_history (session_id, role, content, model) VALUES (?,?,?,?)').run(
      msg.session_id, msg.role, msg.content, msg.model || null,
    )
    db.prepare('UPDATE chat_sessions SET updated_at = CURRENT_TIMESTAMP WHERE id = ?').run(msg.session_id)
  })

  ipcMain.handle('chat-presets-list', () => {
    return db.prepare('SELECT * FROM prompt_presets ORDER BY is_builtin DESC, id ASC').all()
  })

  ipcMain.handle('chat-preset-save', (_e, preset: { id?: number; name: string; prompt: string }) => {
    if (preset.id) {
      db.prepare('UPDATE prompt_presets SET name = ?, prompt = ? WHERE id = ? AND is_builtin = 0').run(preset.name, preset.prompt, preset.id)
      return
    }
    db.prepare('INSERT INTO prompt_presets (name, prompt) VALUES (?,?)').run(preset.name, preset.prompt)
  })

  ipcMain.handle('chat-preset-delete', (_e, id: number) => {
    db.prepare('DELETE FROM prompt_presets WHERE id = ? AND is_builtin = 0').run(id)
  })

  ipcMain.handle('chat-memories-list', (_e, search?: string) => {
    const rows = db.prepare('SELECT * FROM memories ORDER BY pinned DESC, updated_at DESC, id DESC').all() as MemoryRow[]
    if (!search?.trim()) {
      return rows
    }
    const keyword = search.trim().toLowerCase()
    return rows.filter((row) =>
      row.content.toLowerCase().includes(keyword) || row.category.toLowerCase().includes(keyword),
    )
  })

  ipcMain.handle('chat-memory-save', (_e, memory: MemoryInput) => {
    if (memory.id) {
      db.prepare(
        `UPDATE memories
         SET content = ?, category = ?, pinned = ?, enabled = ?, confidence = ?, updated_at = CURRENT_TIMESTAMP
         WHERE id = ?`,
      ).run(
        memory.content,
        memory.category ?? 'general',
        memory.pinned ? 1 : 0,
        memory.enabled === false ? 0 : 1,
        memory.confidence ?? 1,
        memory.id,
      )
      return db.prepare('SELECT * FROM memories WHERE id = ?').get(memory.id)
    }

    const existing = db.prepare('SELECT * FROM memories WHERE lower(content) = lower(?) LIMIT 1').get(memory.content) as MemoryRow | undefined
    if (existing) {
      db.prepare(
        `UPDATE memories
         SET category = ?, pinned = ?, enabled = ?, confidence = ?, source = ?, source_ref = ?, updated_at = CURRENT_TIMESTAMP
         WHERE id = ?`,
      ).run(
        memory.category ?? existing.category,
        memory.pinned ? 1 : 0,
        memory.enabled === false ? 0 : 1,
        memory.confidence ?? existing.confidence ?? 1,
        memory.source ?? existing.source,
        memory.source_ref ?? existing.source_ref,
        existing.id,
      )
      return db.prepare('SELECT * FROM memories WHERE id = ?').get(existing.id)
    }

    const result = db.prepare(
      'INSERT INTO memories (content, category, source, source_ref, pinned, enabled, confidence) VALUES (?,?,?,?,?,?,?)',
    ).run(
      memory.content,
      memory.category ?? 'general',
      memory.source ?? 'manual',
      memory.source_ref ?? null,
      memory.pinned ? 1 : 0,
      memory.enabled === false ? 0 : 1,
      memory.confidence ?? 1,
    )
    return db.prepare('SELECT * FROM memories WHERE id = ?').get(result.lastInsertRowid)
  })

  ipcMain.handle('chat-memory-delete', (_e, id: number) => {
    db.prepare('DELETE FROM memories WHERE id = ?').run(id)
  })

  ipcMain.handle('chat-memory-capture', (_e, args: { content: string; session_id?: string }) => {
    return captureMemoriesFromMessage(args.content, args.session_id)
  })
}

export function getRelevantMemories(query: string, limit = 6) {
  const db = getDB()
  const rows = db.prepare('SELECT * FROM memories WHERE enabled = 1').all() as MemoryRow[]
  const terms = buildSearchTerms(query)

  const scored = rows
    .map((row) => {
      let score = row.pinned ? 50 : 0
      const content = row.content.toLowerCase()

      for (const term of terms) {
        if (content.includes(term)) {
          score += Math.max(2, term.length)
        }
      }

      if (query && (content.includes(query.toLowerCase()) || query.toLowerCase().includes(content))) {
        score += 20
      }

      if (!score && row.pinned) {
        score = 1
      }

      return { row, score }
    })
    .filter((item) => item.score > 0)
    .sort((a, b) => b.score - a.score || b.row.id - a.row.id)

  if (scored.length > 0) {
    return scored.slice(0, limit).map((item) => item.row)
  }

  return rows
    .sort((a, b) => Number(Boolean(b.pinned)) - Number(Boolean(a.pinned)) || b.id - a.id)
    .slice(0, Math.min(limit, 3))
}

export function markMemoriesUsed(ids: number[]) {
  if (ids.length === 0) return
  const db = getDB()
  const stmt = db.prepare('UPDATE memories SET last_used_at = CURRENT_TIMESTAMP WHERE id = ?')
  for (const id of ids) {
    stmt.run(id)
  }
}

export function captureMemoriesFromMessage(content: string, sessionId?: string) {
  const candidates = extractMemoryCandidates(content)
  const saved: MemoryRow[] = []
  const db = getDB()

  for (const candidate of candidates) {
    const existing = db.prepare('SELECT * FROM memories WHERE lower(content) = lower(?) LIMIT 1').get(candidate.content) as MemoryRow | undefined

    if (existing) {
      db.prepare(
        'UPDATE memories SET category = ?, source = ?, source_ref = ?, enabled = 1, updated_at = CURRENT_TIMESTAMP WHERE id = ?',
      ).run(candidate.category, 'chat', sessionId ?? null, existing.id)
      saved.push(db.prepare('SELECT * FROM memories WHERE id = ?').get(existing.id) as MemoryRow)
      continue
    }

    const result = db.prepare(
      'INSERT INTO memories (content, category, source, source_ref, confidence) VALUES (?,?,?,?,?)',
    ).run(candidate.content, candidate.category, 'chat', sessionId ?? null, 0.85)
    saved.push(db.prepare('SELECT * FROM memories WHERE id = ?').get(result.lastInsertRowid) as MemoryRow)
  }

  return saved
}

function extractMemoryCandidates(message: string) {
  const text = message.trim()
  const patterns: Array<{ regex: RegExp; category: string }> = [
    { regex: /^(?:请|帮我)?记住[:：\s]*(.+)$/i, category: 'fact' },
    { regex: /^(?:请|帮我)?记一下[:：\s]*(.+)$/i, category: 'fact' },
    { regex: /^(?:以后|后面)(.+)$/i, category: 'preference' },
  ]

  return patterns
    .map(({ regex, category }) => {
      const matched = text.match(regex)?.[1]?.trim()
      if (!matched || matched.length < 2) return null
      return { content: matched.slice(0, 300), category }
    })
    .filter((item): item is { content: string; category: string } => Boolean(item))
}

function buildSearchTerms(query: string) {
  const normalized = query.trim().toLowerCase()
  const terms = new Set<string>()

  normalized
    .split(/[\s,，。！？!?:：;；()[\]{}"'`]+/)
    .filter((item) => item.length >= 2)
    .forEach((item) => terms.add(item))

  const compact = normalized.replace(/\s+/g, '')
  if (compact.length >= 2) {
    terms.add(compact.slice(0, Math.min(compact.length, 12)))
  }

  return [...terms]
}
