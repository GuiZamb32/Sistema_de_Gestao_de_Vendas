export interface Produto {
  id: number
  nome: string
  descricao: string | null
  preco: string
  ativo: boolean
  criado_em: string
}

export interface ProdutoCreate {
  nome: string
  descricao?: string | null
  preco: number
}

export interface ProdutoUpdate {
  nome?: string
  descricao?: string | null
  preco?: number
}

export interface ProdutoStatusUpdate {
  ativo: boolean
}