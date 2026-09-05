import api from './api'

import type {
  Produto,
  ProdutoCreate,
  ProdutoStatusUpdate,
  ProdutoUpdate,
} from '../types/produto'

export async function listarProdutos(): Promise<Produto[]> {
  const response = await api.get<Produto[]>('/api/produtos')
  return response.data
}

export async function criarProduto(
  dados: ProdutoCreate,
): Promise<Produto> {
  const response = await api.post<Produto>(
    '/api/produtos',
    dados,
  )

  return response.data
}

export async function atualizarProduto(
  produtoId: number,
  dados: ProdutoUpdate,
): Promise<Produto> {
  const response = await api.put<Produto>(
    `/api/produtos/${produtoId}`,
    dados,
  )

  return response.data
}

export async function atualizarStatusProduto(
  produtoId: number,
  dados: ProdutoStatusUpdate,
): Promise<Produto> {
  const response = await api.patch<Produto>(
    `/api/produtos/${produtoId}/status`,
    dados,
  )

  return response.data
}