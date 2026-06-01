import { ipcMain } from 'electron'
import { runCodeSnippet } from '../utils/codeRunner'

export function registerRunnerIPC() {
  ipcMain.handle('run-code', async (_event, args: { code: string; language: string; stdin?: string }) => {
    return runCodeSnippet(args.code, args.language, args.stdin)
  })
}
