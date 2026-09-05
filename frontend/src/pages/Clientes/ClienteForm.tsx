import { useState } from 'react'
import type { FormEvent } from 'react'

import { criarCliente } from '../../services/clienteService'
import type { ClienteCreate } from '../../types/cliente'

import './ClienteForm.css'

interface ClienteFormProps {
  onSucesso: () => void
  onCancelar: () => void
}

function ClienteForm({
  onSucesso,
  onCancelar,
}: ClienteFormProps) {
  const [nome, setNome] = useState('')
  const [email, setEmail] = useState('')
  const [telefone, setTelefone] = useState('')

  const [carregando, setCarregando] = useState(false)
  const [erro, setErro] = useState('')

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()

    try {
      setCarregando(true)
      setErro('')

      const dados: ClienteCreate = {
        nome: nome.trim(),
        email: email.trim(),
        telefone: telefone.trim() || null,
      }

      await criarCliente(dados)

      onSucesso()
    } catch (error: any) {
      const mensagem =
        error?.response?.data?.detail ||
        'Não foi possível cadastrar o cliente.'

      setErro(mensagem)
    } finally {
      setCarregando(false)
    }
  }

  return (
    <div className="cliente-form-overlay">
      <section className="cliente-form-modal">
        <div className="cliente-form-header">
          <div>
            <h2>Novo cliente</h2>
            <p>Cadastre um novo cliente no sistema.</p>
          </div>

          <button
            type="button"
            className="cliente-form-close"
            onClick={onCancelar}
            disabled={carregando}
            aria-label="Fechar"
          >
            ×
          </button>
        </div>

        <form onSubmit={handleSubmit}>
          <div className="cliente-form-fields">
            <div className="cliente-form-field">
              <label htmlFor="cliente-nome">
                Nome
              </label>

              <input
                id="cliente-nome"
                type="text"
                value={nome}
                onChange={(event) => setNome(event.target.value)}
                placeholder="Digite o nome do cliente"
                required
                maxLength={150}
                disabled={carregando}
              />
            </div>

            <div className="cliente-form-field">
              <label htmlFor="cliente-email">
                E-mail
              </label>

              <input
                id="cliente-email"
                type="email"
                value={email}
                onChange={(event) => setEmail(event.target.value)}
                placeholder="cliente@email.com"
                required
                maxLength={150}
                disabled={carregando}
              />
            </div>

            <div className="cliente-form-field">
              <label htmlFor="cliente-telefone">
                Telefone
              </label>

              <input
                id="cliente-telefone"
                type="tel"
                value={telefone}
                onChange={(event) => setTelefone(event.target.value)}
                placeholder="(48) 99999-9999"
                maxLength={20}
                disabled={carregando}
              />
            </div>
          </div>

          {erro && (
            <div className="cliente-form-error">
              {erro}
            </div>
          )}

          <div className="cliente-form-actions">
            <button
              type="button"
              className="cliente-form-cancel"
              onClick={onCancelar}
              disabled={carregando}
            >
              Cancelar
            </button>

            <button
              type="submit"
              className="cliente-form-submit"
              disabled={carregando}
            >
              {carregando ? 'Salvando...' : 'Salvar cliente'}
            </button>
          </div>
        </form>
      </section>
    </div>
  )
}

export default ClienteForm