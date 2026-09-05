export interface Cliente {
  id: number
  nome: string
  email: string
  telefone: string | null
  ativo: boolean
  criado_em: string
}

export interface ClienteCreate {
  nome: string
  email: string
  telefone?: string | null
}

export interface ClienteStatusUpdate {
  ativo: boolean
}