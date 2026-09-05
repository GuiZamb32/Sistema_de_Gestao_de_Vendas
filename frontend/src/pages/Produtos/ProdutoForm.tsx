import { useEffect, useState } from 'react'
import type { FormEvent } from 'react'

import {
  atualizarProduto,
  criarProduto,
} from '../../services/produtoService'

import type {
  Produto,
  ProdutoCreate,
  ProdutoUpdate,
} from '../../types/produto'

import './ProdutoForm.css'

interface ProdutoFormProps {
  produto?: Produto | null
  onSucesso: (produto: Produto) => void
  onCancelar: () => void
}

function ProdutoForm({
  produto,
  onSucesso,
  onCancelar,
}: ProdutoFormProps) {
  const modoEdicao = Boolean(produto)

  const [nome, setNome] = useState('')
  const [descricao, setDescricao] = useState('')
  const [preco, setPreco] = useState('')

  const [carregando, setCarregando] = useState(false)
  const [erro, setErro] = useState('')

  useEffect(() => {
    if (produto) {
      setNome(produto.nome)
      setDescricao(produto.descricao ?? '')
      setPreco(produto.preco)
    } else {
      setNome('')
      setDescricao('')
      setPreco('')
    }

    setErro('')
  }, [produto])

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()

    try {
      setCarregando(true)
      setErro('')

      const valor = Number(preco)

      if (!Number.isFinite(valor) || valor <= 0) {
        setErro('Informe um preço válido maior que zero.')
        return
      }

      if (modoEdicao && produto) {
        const dados: ProdutoUpdate = {
          nome: nome.trim(),
          descricao: descricao.trim() || null,
          preco: valor,
        }

        const produtoAtualizado = await atualizarProduto(
          produto.id,
          dados,
        )

        onSucesso(produtoAtualizado)
      } else {
        const dados: ProdutoCreate = {
          nome: nome.trim(),
          descricao: descricao.trim() || null,
          preco: valor,
        }

        const produtoCriado = await criarProduto(dados)

        onSucesso(produtoCriado)
      }
    } catch (error: any) {
      const mensagem =
        error?.response?.data?.detail ||
        `Não foi possível ${
          modoEdicao ? 'atualizar' : 'cadastrar'
        } o produto.`

      setErro(mensagem)
    } finally {
      setCarregando(false)
    }
  }

  return (
    <div className="produto-form-overlay">
      <section className="produto-form-modal">
        <div className="produto-form-header">
          <div>
            <h2>
              {modoEdicao ? 'Editar produto' : 'Novo produto'}
            </h2>

            <p>
              {modoEdicao
                ? 'Atualize os dados do produto cadastrado.'
                : 'Cadastre um novo produto no sistema.'}
            </p>
          </div>

          <button
            type="button"
            className="produto-form-close"
            onClick={onCancelar}
            disabled={carregando}
            aria-label="Fechar"
          >
            ×
          </button>
        </div>

        <form onSubmit={handleSubmit}>
          <div className="produto-form-fields">
            <div className="produto-form-field">
              <label htmlFor="produto-nome">
                Nome
              </label>

              <input
                id="produto-nome"
                type="text"
                value={nome}
                onChange={(event) => setNome(event.target.value)}
                placeholder="Digite o nome do produto"
                required
                maxLength={150}
                disabled={carregando}
              />
            </div>

            <div className="produto-form-field">
              <label htmlFor="produto-descricao">
                Descrição
              </label>

              <textarea
                id="produto-descricao"
                value={descricao}
                onChange={(event) =>
                  setDescricao(event.target.value)
                }
                placeholder="Digite a descrição do produto"
                maxLength={500}
                rows={4}
                disabled={carregando}
              />
            </div>

            <div className="produto-form-field">
              <label htmlFor="produto-preco">
                Preço
              </label>

              <input
                id="produto-preco"
                type="number"
                value={preco}
                onChange={(event) => setPreco(event.target.value)}
                placeholder="0,00"
                min="0.01"
                step="0.01"
                required
                disabled={carregando}
              />
            </div>
          </div>

          {erro && (
            <div className="produto-form-error">
              {erro}
            </div>
          )}

          <div className="produto-form-actions">
            <button
              type="button"
              className="produto-form-cancel"
              onClick={onCancelar}
              disabled={carregando}
            >
              Cancelar
            </button>

            <button
              type="submit"
              className="produto-form-submit"
              disabled={carregando}
            >
              {carregando
                ? 'Salvando...'
                : modoEdicao
                  ? 'Atualizar produto'
                  : 'Salvar produto'}
            </button>
          </div>
        </form>
      </section>
    </div>
  )
}

export default ProdutoForm