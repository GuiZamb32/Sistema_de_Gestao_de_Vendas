import api from './api'
import type {
  Cliente,
  ClienteCreate,
  ClienteStatusUpdate,
} from '../types/cliente'

export async function listarClientes(): Promise<Cliente[]> {
  const response = await api.get<Cliente[]>('/api/clientes')

  return response.data
}

export async function criarCliente(
  dados: ClienteCreate,
): Promise<Cliente> {
  const response = await api.post<Cliente>('/api/clientes', dados)

  return response.data
}

export async function atualizarStatusCliente(
  clienteId: number,
  dados: ClienteStatusUpdate,
): Promise<Cliente> {
  const response = await api.patch<Cliente>(
    `/api/clientes/${clienteId}/status`,
    dados,
  )

  return response.data
}