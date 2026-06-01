import { ipcMain } from 'electron'
import { getDB } from '../db/index'

export function registerMistakesIPC() {
  ipcMain.handle('mistakes-list', () => {
    return getDB().prepare(`
      SELECT m.*, p.title, p.difficulty, p.tags 
      FROM mistakes m 
      JOIN problems p ON m.problem_id = p.id 
      ORDER BY m.updated_at DESC
    `).all()
  })

  ipcMain.handle('mistakes-get', (_e, id: number) => {
    return getDB().prepare(`
      SELECT m.*, p.title, p.description, p.difficulty, p.tags, p.starter_code
      FROM mistakes m 
      JOIN problems p ON m.problem_id = p.id 
      WHERE m.id = ?
    `).get(id)
  })

  ipcMain.handle('mistakes-update-analysis', (_e, id: number, analysis: string) => {
    getDB().prepare('UPDATE mistakes SET ai_analysis = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?').run(analysis, id)
  })

  ipcMain.handle('mistakes-delete', (_e, id: number) => {
    getDB().prepare('DELETE FROM mistakes WHERE id = ?').run(id)
  })
}
