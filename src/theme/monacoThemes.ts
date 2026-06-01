import type * as Monaco from 'monaco-editor'
import type { ThemeId } from '../stores/appStore'

export const monacoThemeByAppTheme: Record<ThemeId, string> = {
  mocha: 'codehelper-mocha',
  fjord: 'codehelper-fjord',
  ember: 'codehelper-ember',
}

let registered = false

export function registerMonacoThemes(monaco: typeof Monaco) {
  if (registered) {
    return
  }

  monaco.editor.defineTheme('codehelper-mocha', {
    base: 'vs-dark',
    inherit: true,
    rules: [
      { token: 'comment', foreground: '6c7086' },
      { token: 'keyword', foreground: 'cba6f7' },
      { token: 'string', foreground: 'a6e3a1' },
      { token: 'number', foreground: 'f9e2af' },
      { token: 'type', foreground: '89b4fa' },
      { token: 'function', foreground: 'f5c2e7' },
    ],
    colors: {
      'editor.background': '#11111b',
      'editor.lineHighlightBackground': '#181825',
      'editor.selectionBackground': '#313244',
      'editor.inactiveSelectionBackground': '#232634',
      'editorCursor.foreground': '#cba6f7',
      'editorWhitespace.foreground': '#313244',
      'editorIndentGuide.background1': '#232634',
      'editorIndentGuide.activeBackground1': '#45475a',
      'editorLineNumber.foreground': '#6c7086',
      'editorLineNumber.activeForeground': '#cdd6f4',
      'editorWidget.background': '#181825',
      'editorWidget.border': '#313244',
    },
  })

  monaco.editor.defineTheme('codehelper-fjord', {
    base: 'vs-dark',
    inherit: true,
    rules: [
      { token: 'comment', foreground: '7f9bb1' },
      { token: 'keyword', foreground: '69d2e7' },
      { token: 'string', foreground: '7fe0b1' },
      { token: 'number', foreground: 'f2c66d' },
      { token: 'type', foreground: '84b6ff' },
      { token: 'function', foreground: 'abdff0' },
    ],
    colors: {
      'editor.background': '#0c1320',
      'editor.lineHighlightBackground': '#13202c',
      'editor.selectionBackground': '#24384c',
      'editor.inactiveSelectionBackground': '#152433',
      'editorCursor.foreground': '#69d2e7',
      'editorWhitespace.foreground': '#294055',
      'editorIndentGuide.background1': '#1b2938',
      'editorIndentGuide.activeBackground1': '#3a5872',
      'editorLineNumber.foreground': '#7f9bb1',
      'editorLineNumber.activeForeground': '#e7f2fb',
      'editorWidget.background': '#13202c',
      'editorWidget.border': '#294055',
    },
  })

  monaco.editor.defineTheme('codehelper-ember', {
    base: 'vs-dark',
    inherit: true,
    rules: [
      { token: 'comment', foreground: 'a48673' },
      { token: 'keyword', foreground: 'f2a65a' },
      { token: 'string', foreground: '89d39b' },
      { token: 'number', foreground: 'f4cb71' },
      { token: 'type', foreground: '88b9ff' },
      { token: 'function', foreground: 'f6c89f' },
    ],
    colors: {
      'editor.background': '#18110d',
      'editor.lineHighlightBackground': '#221913',
      'editor.selectionBackground': '#3a2a20',
      'editor.inactiveSelectionBackground': '#241b15',
      'editorCursor.foreground': '#f2a65a',
      'editorWhitespace.foreground': '#4b372b',
      'editorIndentGuide.background1': '#2b1f18',
      'editorIndentGuide.activeBackground1': '#63493a',
      'editorLineNumber.foreground': '#a48673',
      'editorLineNumber.activeForeground': '#f3e7db',
      'editorWidget.background': '#221913',
      'editorWidget.border': '#4b372b',
    },
  })

  registered = true
}
