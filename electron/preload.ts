import { contextBridge, ipcRenderer } from 'electron'

const allowedInvokeChannels = new Set([
  'run-code',
  'db-get-setting',
  'db-set-setting',
  'db-get-ai-configs',
  'db-save-ai-config',
  'db-delete-ai-config',
  'db-get-default-ai-config',
  'ai-fetch-models',
  'ai-chat',
  'problems-list',
  'problems-get',
  'problems-submit',
  'problems-submissions',
  'mistakes-list',
  'mistakes-get',
  'mistakes-update-analysis',
  'mistakes-delete',
  'knowledge-upload',
  'knowledge-list',
  'knowledge-delete',
  'knowledge-search',
  'open-external',
  'chat-sessions-list',
  'chat-session-create',
  'chat-session-update',
  'chat-session-delete',
  'chat-messages-load',
  'chat-message-save',
  'chat-presets-list',
  'chat-preset-save',
  'chat-preset-delete',
  'chat-memories-list',
  'chat-memory-save',
  'chat-memory-delete',
  'chat-memory-capture',
])

const allowedEventChannels = new Set(['ai-chat-chunk', 'ai-chat-done'])

const api = {
  invoke: (channel: string, ...args: unknown[]) => {
    if (!allowedInvokeChannels.has(channel)) {
      throw new Error(`不允许的 IPC 调用: ${channel}`)
    }
    return ipcRenderer.invoke(channel, ...args)
  },
  on: (channel: string, callback: (...args: unknown[]) => void) => {
    if (!allowedEventChannels.has(channel)) {
      throw new Error(`不允许的 IPC 事件监听: ${channel}`)
    }
    const subscription = (_event: Electron.IpcRendererEvent, ...args: unknown[]) => callback(...args)
    ipcRenderer.on(channel, subscription)
    return () => ipcRenderer.removeListener(channel, subscription)
  }
}

contextBridge.exposeInMainWorld('api', api)
