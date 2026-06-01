import { X, Plus } from 'lucide-react'
import { useEditorStore } from '../../stores/editorStore'

export function EditorTabs() {
  const { tabs, activeTabId, setActiveTab, closeTab, addTab } = useEditorStore()

  const handleNewTab = () => {
    const id = `file-${Date.now()}`
    addTab({
      id,
      filename: `untitled-${tabs.length + 1}.py`,
      language: 'python',
      content: '',
    })
  }

  return (
    <div className="flex items-center overflow-x-auto">
      {tabs.map((tab) => (
        <div
          key={tab.id}
          onClick={() => setActiveTab(tab.id)}
          className={`flex shrink-0 items-center gap-2 border-r px-3 py-2 text-sm glass-line ${
            activeTabId === tab.id
              ? 'bg-[var(--theme-bg-app)] text-[var(--theme-text-primary)]'
              : 'text-[var(--theme-text-muted)] hover:bg-[var(--theme-bg-hover)]/60'
          }`}
        >
          <span className="max-w-[140px] truncate">{tab.filename}</span>
          <button
            onClick={(event) => {
              event.stopPropagation()
              closeTab(tab.id)
            }}
            className="rounded p-0.5 opacity-60 hover:bg-[var(--theme-bg-hover)] hover:opacity-100"
          >
            <X size={12} />
          </button>
        </div>
      ))}
      <button
        onClick={handleNewTab}
        className="mx-1 rounded p-1.5 text-[var(--theme-text-muted)] hover:bg-[var(--theme-bg-hover)] hover:text-[var(--theme-text-primary)]"
        title="新建文件"
      >
        <Plus size={14} />
      </button>
    </div>
  )
}
