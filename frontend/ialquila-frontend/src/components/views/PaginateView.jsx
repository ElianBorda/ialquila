import React from 'react'
import { Link } from 'react-router-dom'


export default function PaginateView({subNum, sumNum, pagesList, cant, setNumPage, scroll, scrollRef1}) {
  
  
  return (
    <div className='pagContainer'>
        <Link className='pagNext' onClick={() => {
              const num = 1
              setNumPage(num)
              localStorage.setItem('numPage', num.toString())
              scroll(scrollRef1)
            }}>Primero</Link>
        <Link className='pagNext' onClick={subNum}>Anterior</Link>
        <div className='pagList'>
            <ul>
                {pagesList.map((page) => (<li key={page.numPage}><Link className={`linkPag ${page.current ? 'pageCurrent' : ''}`} 
                  onClick={() => {
                    setNumPage(page.numPage)
                    localStorage.setItem('numPage', page.numPage.toString())
                    scroll(scrollRef1)
                  }}>{page.numPage}</Link></li>))}
            </ul>
        </div>
        <Link className='pagNext' onClick={sumNum}>Siguiente</Link>
        <Link className='pagNext' onClick={() => {
                    window.scrollTo(0, 0)
                    setNumPage(cant)
                    localStorage.setItem('numPage', cant.toString())
                    scroll(scrollRef1)
                  }}>Ultimo</Link>
    </div>
  )
}
