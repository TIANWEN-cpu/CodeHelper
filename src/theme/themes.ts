import type { ThemeId } from '../stores/appStore'

export interface ThemeOption {
  id: ThemeId
  name: string
  description: string
  accent: string
  panel: string
  glow: string
}

export const themeOptions: ThemeOption[] = [
  {
    id: 'mocha',
    name: 'Mocha Night',
    description: '柔和紫调的沉浸深夜模式，适合长时间写代码和刷题。',
    accent: '#cba6f7',
    panel: '#181825',
    glow: 'rgba(203,166,247,0.24)',
  },
  {
    id: 'fjord',
    name: 'Fjord Blue',
    description: '更清冷的蓝青配色，分区对比更强，信息密度更清楚。',
    accent: '#69d2e7',
    panel: '#13202c',
    glow: 'rgba(105,210,231,0.24)',
  },
  {
    id: 'ember',
    name: 'Ember Copper',
    description: '偏暖的铜橙色阅读氛围，更适合夜间复盘和知识整理。',
    accent: '#f2a65a',
    panel: '#221913',
    glow: 'rgba(242,166,90,0.22)',
  },
]
