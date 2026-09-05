import { useEffect, useState } from 'react'

import {
  atualizarStatusCliente,
  listarClientes,
} from '../../services/clienteService'
import type { Cliente } from '../../types/cliente'

import ClienteForm from './ClienteForm'
import './Clientes.css'

function Clientes() {
  const [clientes, setClientes] = useState<Cliente[]>([])
  const [carregando, setCarregando] = useState(true)
  const [erro, setErro] = useState('')
  const [mostrarFormulario, setMostrarFormulario] = useState(false)

  async function carregarClientes() {
    try {
      setCarregando(true)
      setErro('')

      const dados = await listarClientes()

      setClientes(dados)
    } catch {
      setErro('Não foi possível carregar os clientes.')
    } finally {
      setCarregando(false)
    }
  }

  useEffect(() => {
    carregarClientes()
  }, [])

  function handleClienteCriado() {
    setMostrarFormulario(false)
    carregarClientes()
  }

  async function handleAlterarStatus(cliente: Cliente) {
  try {
    setErro('')

    const clienteAtualizado = await atualizarStatusCliente(
      cliente.id,
      {
        ativo: !cliente.ativo,
      },
    )

    setClientes((clientesAtuais) =>
      clientesAtuais.map((clienteAtual) =>
        clienteAtual.id === clienteAtualizado.id
          ? clienteAtualizado
          : clienteAtual,
      ),
    )
  } catch {
    setErro('Não foi possível alterar o status do cliente.')
  }
}

  if (carregando) {
    return (
      <div className="clientes-state">
        <p>Carregando clientes...</p>
      </div>
    )
  }

  if (erro) {
    return (
      <div className="clientes-state clientes-error">
        <p>{erro}</p>
      </div>
    )
  }

  return (
    <div className="clientes">
      <div className="clientes-heading">
        <div>
          <h1>Clientes</h1>
          <p>Gerencie os clientes cadastrados no sistema.</p>
        </div>

        <button
          className="clientes-button"
          onClick={() => setMostrarFormulario(true)}
        >
          Novo cliente
        </button>
      </div>

      <section className="clientes-panel">
        <div className="clientes-panel-header">
          <div>
            <h2>Clientes cadastrados</h2>
            <p>
              {clientes.length}{' '}
              {clientes.length === 1
                ? 'cliente cadastrado'
                : 'clientes cadastrados'}
            </p>
          </div>
        </div>

        {clientes.length === 0 ? (
          <div className="clientes-empty">
            <p>Nenhum cliente cadastrado.</p>
          </div>
        ) : (
          <div className="clientes-table-wrapper">
            <table className="clientes-table">
              <thead>
                <tr>
                  <th>Cliente</th>
                  <th>E-mail</th>
                  <th>Telefone</th>
                  <th>Status</th>
                  <th>Cadastro</th>
                  <th>Ações</th>
                </tr>
              </thead>

              <tbody>
                {clientes.map((cliente) => (
                  <tr key={cliente.id}>
                    <td>
                      <div className="cliente-info">
                        <strong>{cliente.nome}</strong>
                        <span>#{cliente.id}</span>
                      </div>
                    </td>

                    <td>{cliente.email}</td>

                    <td>
                      {cliente.telefone || 'Não informado'}
                    </td>

                    <td>
                      <span
                        className={
                          cliente.ativo
                            ? 'cliente-status cliente-status-active'
                            : 'cliente-status cliente-status-inactive'
                        }
                      >
                        {cliente.ativo ? 'Ativo' : 'Inativo'}
                      </span>
                    </td>

                    <td>
                      <button
                        className="cliente-action-button"
                        onClick={() => handleAlterarStatus(cliente)}
                      >
                        {cliente.ativo ? 'Desativar' : 'Ativar'}
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </section>

      {mostrarFormulario && (
        <ClienteForm
          onSucesso={handleClienteCriado}
          onCancelar={() => setMostrarFormulario(false)}
        />
      )}
    </div>
  )
}

export default Clientes