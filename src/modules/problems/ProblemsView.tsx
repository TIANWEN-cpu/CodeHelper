import { ProblemList } from './ProblemList'
import { ProblemDetail } from './ProblemDetail'
import { AISidebar } from './AISidebar'
import { useProblemStore } from '../../stores/problemStore'

export function ProblemsView() {
  const { listCollapsed, aiPanelOpen } = useProblemStore()

  return (
    <div className="flex-1 flex min-h-0 overflow-hidden">
      {!listCollapsed && <ProblemList />}
      <ProblemDetail />
      {aiPanelOpen && <AISidebar />}
    </div>
  )
}
