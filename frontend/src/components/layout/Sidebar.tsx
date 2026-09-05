import { NavLink } from 'react-router-dom'

function Sidebar() {
  const links = [
    { label: 'Dashboard', path: '/dashboard' },
    { label: 'Clientes', path: '/clientes' },
    { label: 'Produtos', path: '/produtos' },
    { label: 'Estoque', path: '/estoque' },
    { label: 'Vendas', path: '/vendas' },
    { label: 'Relatórios', path: '/relatorios' },
  ]

  return (
    <aside className="sidebar">
      <div className="sidebar-brand">
        <h1>Gestão de Vendas</h1>
      </div>

      <nav className="sidebar-nav">
        {links.map((link) => (
          <NavLink
            key={link.path}
            to={link.path}
            className={({ isActive }) =>
              isActive ? 'sidebar-link active' : 'sidebar-link'
            }
          >
            {link.label}
          </NavLink>
        ))}
      </nav>
    </aside>
  )
}

export default Sidebar