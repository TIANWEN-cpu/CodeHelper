import { Layout } from './components/Layout'
import { useEffect } from 'react'
import { useAppStore } from './stores/appStore'

function App() {
  const loadTheme = useAppStore((state) => state.loadTheme)

  useEffect(() => {
    void loadTheme()
  }, [loadTheme])

  return <Layout />
}

export default App
