import { useEffect, useState } from 'react'

import {
  atualizarStatusProduto,
  listarProdutos,
} from '../../services/produtoService'

import type { Produto } from '../../types/produto'

import ProdutoForm from './ProdutoForm'

import './Produtos.css'

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

function Produtos() {
  const [produtos, setProdutos] = useState<Produto[]>([])
  const [carregando, setCarregando] = useState(true)
  const [erro, setErro] = useState('')

  const [formAberto, setFormAberto] = useState(false)
  const [produtoEditando, setProdutoEditando] =
    useState<Produto | null>(null)

  useEffect(() => {
    async function carregarProdutos() {
      try {
        setCarregando(true)
        setErro('')

        const dados = await listarProdutos()

        setProdutos(dados)
      } catch {
        setErro('Não foi possível carregar os produtos.')
      } finally {
        setCarregando(false)
      }
    }

    carregarProdutos()
  }, [])

  function handleNovoProduto() {
    setProdutoEditando(null)
    setFormAberto(true)
    setErro('')
  }

  function handleEditarProduto(produto: Produto) {
    setProdutoEditando(produto)
    setFormAberto(true)
    setErro('')
  }

  function handleCancelarFormulario() {
    setFormAberto(false)
    setProdutoEditando(null)
  }

  function handleSucessoFormulario(produtoSalvo: Produto) {
    setProdutos((produtosAtuais) => {
      const produtoExiste = produtosAtuais.some(
        (produto) => produto.id === produtoSalvo.id,
      )

      if (produtoExiste) {
        return produtosAtuais.map((produto) =>
          produto.id === produtoSalvo.id
            ? produtoSalvo
            : produto,
        )
      }

      return [...produtosAtuais, produtoSalvo]
    })

    setFormAberto(false)
    setProdutoEditando(null)
    setErro('')
  }

  async function handleAlterarStatus(produto: Produto) {
    try {
      setErro('')

      const produtoAtualizado = await atualizarStatusProduto(
        produto.id,
        { ativo: !produto.ativo },
      )

      setProdutos((produtosAtuais) =>
        produtosAtuais.map((produtoAtual) =>
          produtoAtual.id === produtoAtualizado.id
            ? produtoAtualizado
            : produtoAtual,
        ),
      )
    } catch {
      setErro(
        'Não foi possível alterar o status do produto.',
      )
    }
  }

  if (carregando) {
    return (
      <div className="produtos-state">
        <p>Carregando produtos...</p>
      </div>
    )
  }

  return (
    <div className="produtos">
      <div className="produtos-heading">
        <div>
          <h1>Produtos</h1>
          <p>
            Gerencie os produtos cadastrados no sistema.
          </p>
        </div>

        <button
          type="button"
          className="produtos-new-button"
          onClick={handleNovoProduto}
        >
          Novo produto
        </button>
      </div>

      {erro && (
        <div className="produtos-error">
          {erro}
        </div>
      )}

      <section className="produtos-panel">
        <div className="produtos-panel-header">
          <div>
            <h2>Produtos cadastrados</h2>
            <p>
              Consulte e gerencie os produtos disponíveis.
            </p>
          </div>

          <span className="produtos-count">
            {produtos.length} produto(s)
          </span>
        </div>

        {produtos.length === 0 ? (
          <div className="produtos-empty">
            <p>Nenhum produto cadastrado.</p>
          </div>
        ) : (
          <div className="table-wrapper">
            <table className="produtos-table">
              <thead>
                <tr>
                  <th>Produto</th>
                  <th>Descrição</th>
                  <th>Preço</th>
                  <th>Status</th>
                  <th>Cadastro</th>
                  <th>Ações</th>
                </tr>
              </thead>

              <tbody>
                {produtos.map((produto) => (
                  <tr key={produto.id}>
                    <td>
                      <strong>{produto.nome}</strong>
                    </td>

                    <td>
                      {produto.descricao ||
                        'Sem descrição'}
                    </td>

                    <td>
                      {formatarMoeda(produto.preco)}
                    </td>

                    <td>
                      <span
                        className={
                          produto.ativo
                            ? 'produto-status ativo'
                            : 'produto-status inativo'
                        }
                      >
                        {produto.ativo
                          ? 'Ativo'
                          : 'Inativo'}
                      </span>
                    </td>

                    <td>
                      {formatarData(produto.criado_em)}
                    </td>

                    <td>
                      <div className="produtos-actions">
                        <button
                          type="button"
                          className="produto-action-button produto-edit-button"
                          onClick={() =>
                            handleEditarProduto(produto)
                          }
                        >
                          Editar
                        </button>

                        <button
                          type="button"
                          className="produto-action-button"
                          onClick={() =>
                            handleAlterarStatus(produto)
                          }
                        >
                          {produto.ativo
                            ? 'Desativar'
                            : 'Ativar'}
                        </button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </section>

      {formAberto && (
        <ProdutoForm
          produto={produtoEditando}
          onSucesso={handleSucessoFormulario}
          onCancelar={handleCancelarFormulario}
        />
      )}
    </div>
  )
}

export default Produtos