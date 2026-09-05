import type { ReactNode } from 'react'

import Header from './Header'
import Sidebar from './Sidebar'
import '../../styles/layout.css'

interface LayoutProps {
  children: ReactNode
}

function Layout({ children }: LayoutProps) {
  return (
    <div className="app-layout">
      <Sidebar />

      <div className="main-area">
        <Header />

        <main className="page-content">
          {children}
        </main>
      </div>
    </div>
  )
}

export default Layout