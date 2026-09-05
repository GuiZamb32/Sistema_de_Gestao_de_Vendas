export interface VendaRecente {
  id: number
  cliente_id: number
  valor_total: string
  status: string
  criado_em: string
}

export interface ProdutoMaisVendido {
  produto_id: number
  nome: string
  quantidade_vendida: number
}

export interface DashboardResumo {
  total_vendas: number
  faturamento_total: string
  total_produtos: number
  total_clientes: number
  produtos_estoque_baixo: number
  vendas_recentes: VendaRecente[]
  produtos_mais_vendidos: ProdutoMaisVendido[]
}