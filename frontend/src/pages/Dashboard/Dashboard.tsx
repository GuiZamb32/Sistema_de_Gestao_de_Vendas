import { useEffect, useState } from 'react'

import { obterResumoDashboard } from '../../services/dashboardService'
import type { DashboardResumo } from '../../types/dashboard'

import './Dashboard.css'

function formatarMoeda(valor: string) {
  return Number(valor).toLocaleString('pt-BR', {
    style: 'currency',
    currency: 'BRL',
  })
}

function formatarData(data: string) {
  return new Date(data).toLocaleString('pt-BR', {
    dateStyle: 'short',
    timeStyle: 'short',
  })
}

function Dashboard() {
  const [dados, setDados] = useState<DashboardResumo | null>(null)
  const [carregando, setCarregando] = useState(true)
  const [erro, setErro] = useState('')

  useEffect(() => {
    async function carregarDashboard() {
      try {
        setCarregando(true)
        setErro('')

        const resumo = await obterResumoDashboard()

        setDados(resumo)
      } catch {
        setErro('Não foi possível carregar os dados do dashboard.')
      } finally {
        setCarregando(false)
      }
    }

    carregarDashboard()
  }, [])

  if (carregando) {
    return (
      <div className="dashboard-state">
        <p>Carregando dashboard...</p>
      </div>
    )
  }

  if (erro) {
    return (
      <div className="dashboard-state dashboard-error">
        <p>{erro}</p>
      </div>
    )
  }

  if (!dados) {
    return (
      <div className="dashboard-state">
        <p>Nenhum dado disponível.</p>
      </div>
    )
  }

  return (
    <div className="dashboard">
      <div className="dashboard-heading">
        <div>
          <h1>Dashboard</h1>
          <p>Visão geral do desempenho do sistema.</p>
        </div>
      </div>

      <section className="dashboard-cards">
        <article className="dashboard-card">
          <span className="dashboard-card-label">Total de vendas</span>
          <strong>{dados.total_vendas}</strong>
        </article>

        <article className="dashboard-card">
          <span className="dashboard-card-label">Faturamento total</span>
          <strong>{formatarMoeda(dados.faturamento_total)}</strong>
        </article>

        <article className="dashboard-card">
          <span className="dashboard-card-label">Produtos ativos</span>
          <strong>{dados.total_produtos}</strong>
        </article>

        <article className="dashboard-card">
          <span className="dashboard-card-label">Clientes ativos</span>
          <strong>{dados.total_clientes}</strong>
        </article>

        <article className="dashboard-card dashboard-card-warning">
          <span className="dashboard-card-label">Estoque baixo</span>
          <strong>{dados.produtos_estoque_baixo}</strong>
        </article>
      </section>

      <section className="dashboard-grid">
        <article className="dashboard-panel">
          <div className="dashboard-panel-header">
            <div>
              <h2>Vendas recentes</h2>
              <p>Últimas vendas registradas no sistema.</p>
            </div>
          </div>

          {dados.vendas_recentes.length === 0 ? (
            <div className="dashboard-empty">
              <p>Nenhuma venda registrada.</p>
            </div>
          ) : (
            <div className="table-wrapper">
              <table className="dashboard-table">
                <thead>
                  <tr>
                    <th>Venda</th>
                    <th>Cliente</th>
                    <th>Valor</th>
                    <th>Status</th>
                    <th>Data</th>
                  </tr>
                </thead>

                <tbody>
                  {dados.vendas_recentes.map((venda) => (
                    <tr key={venda.id}>
                      <td>#{venda.id}</td>
                      <td>Cliente #{venda.cliente_id}</td>
                      <td>{formatarMoeda(venda.valor_total)}</td>
                      <td>
                        <span className="status-badge">
                          {venda.status}
                        </span>
                      </td>
                      <td>{formatarData(venda.criado_em)}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </article>

        <article className="dashboard-panel">
          <div className="dashboard-panel-header">
            <div>
              <h2>Produtos mais vendidos</h2>
              <p>Ranking por quantidade comercializada.</p>
            </div>
          </div>

          {dados.produtos_mais_vendidos.length === 0 ? (
            <div className="dashboard-empty">
              <p>Nenhum produto vendido.</p>
            </div>
          ) : (
            <div className="product-ranking">
              {dados.produtos_mais_vendidos.map((produto, index) => (
                <div
                  className="product-ranking-item"
                  key={produto.produto_id}
                >
                  <div className="product-ranking-position">
                    {index + 1}
                  </div>

                  <div className="product-ranking-info">
                    <strong>{produto.nome}</strong>
                    <span>
                      {produto.quantidade_vendida} unidades vendidas
                    </span>
                  </div>
                </div>
              ))}
            </div>
          )}
        </article>
      </section>
    </div>
  )
}

export default Dashboard