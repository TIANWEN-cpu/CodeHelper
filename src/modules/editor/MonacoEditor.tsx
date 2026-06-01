import Editor from '@monaco-editor/react'
import { useEditorStore } from '../../stores/editorStore'
import { useAppStore } from '../../stores/appStore'
import { monacoThemeByAppTheme, registerMonacoThemes } from '../../theme/monacoThemes'

export function MonacoEditor() {
  const { tabs, activeTabId, updateContent } = useEditorStore()
  const theme = useAppStore((state) => state.theme)
  const activeTab = tabs.find((tab) => tab.id === activeTabId)

  if (!activeTab) {
    return (
      <div className="flex flex-1 items-center justify-center text-[var(--theme-text-muted)]">
        没有打开的文件
      </div>
    )
  }

  return (
    <Editor
      key={activeTab.id}
      beforeMount={registerMonacoThemes}
      theme={monacoThemeByAppTheme[theme]}
      language={activeTab.language}
      value={activeTab.content}
      onChange={(value) => updateContent(activeTab.id, value ?? '')}
      options={{
        fontSize: 14,
        fontFamily: "'Cascadia Code', 'Fira Code', Consolas, monospace",
        minimap: { enabled: false },
        padding: { top: 12 },
        scrollBeyondLastLine: false,
        automaticLayout: true,
        tabSize: 4,
        wordWrap: 'on',
        renderLineHighlight: 'line',
        cursorBlinking: 'smooth',
        smoothScrolling: true,
      }}
    />
  )
}
