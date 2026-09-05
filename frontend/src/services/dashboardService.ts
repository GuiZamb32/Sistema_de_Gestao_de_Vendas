import api from './api'
import type { DashboardResumo } from '../types/dashboard'

export async function obterResumoDashboard(): Promise<DashboardResumo> {
  const response = await api.get<DashboardResumo>('/api/dashboard/resumo')

  return response.data
}