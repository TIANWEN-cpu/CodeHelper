import { ipcMain } from 'electron'
import { getDB } from '../db/index'

export function registerDatabaseIPC() {
  // Settings
  ipcMain.handle('db-get-setting', (_e, key: string) => {
    const row = getDB().prepare('SELECT value FROM settings WHERE key = ?').get(key) as { value: string } | undefined
    return row?.value ?? null
  })

  ipcMain.handle('db-set-setting', (_e, key: string, value: string) => {
    getDB().prepare('INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)').run(key, value)
  })

  // AI Configs
  ipcMain.handle('db-get-ai-configs', () => {
    return getDB().prepare('SELECT * FROM ai_configs ORDER BY is_default DESC, id ASC').all()
  })

  ipcMain.handle('db-save-ai-config', (_e, config: {
    id?: number; name: string; api_key: string; base_url: string; model: string; is_default?: boolean; task_type?: string
  }) => {
    const db = getDB()
    if (config.is_default) {
      db.prepare('UPDATE ai_configs SET is_default = 0').run()
    }
    if (config.id) {
      db.prepare(
        'UPDATE ai_configs SET name=?, api_key=?, base_url=?, model=?, is_default=?, task_type=? WHERE id=?'
      ).run(config.name, config.api_key, config.base_url, config.model, config.is_default ? 1 : 0, config.task_type ?? null, config.id)
      return config.id
    } else {
      const result = db.prepare(
        'INSERT INTO ai_configs (name, api_key, base_url, model, is_default, task_type) VALUES (?,?,?,?,?,?)'
      ).run(config.name, config.api_key, config.base_url, config.model, config.is_default ? 1 : 0, config.task_type ?? null)
      return result.lastInsertRowid
    }
  })

  ipcMain.handle('db-delete-ai-config', (_e, id: number) => {
    getDB().prepare('DELETE FROM ai_configs WHERE id = ?').run(id)
  })

  ipcMain.handle('db-get-default-ai-config', () => {
    return getDB().prepare('SELECT * FROM ai_configs WHERE is_default = 1').get() ??
           getDB().prepare('SELECT * FROM ai_configs LIMIT 1').get() ?? null
  })

  // Fetch available models from API
  ipcMain.handle('ai-fetch-models', async (_e, args: { api_key: string; base_url: string }) => {
    const url = `${args.base_url.replace(/\/$/, '')}/models`
    const response = await fetch(url, {
      headers: { 'Authorization': `Bearer ${args.api_key}` },
    })
    if (!response.ok) {
      throw new Error(`获取模型列表失败 (${response.status})`)
    }
    const json = await response.json() as { data?: { id: string }[] }
    const models = (json.data || []).map((m) => m.id).sort()
    return models
  })
}
