import React from 'react'
import { Link } from 'react-router-dom'


export default function PaginateView({subNum, sumNum, pagesList, numPage, setNumPage}) {
  return (
    <div className='pagContainer'>
        <Link className='pagNext' onClick={subNum}>Anterior</Link>
        <div className='pagList'>
            <ul>
                {pagesList.map((page) => (<li><Link className={`linkPag ${page.current ? 'pageCurrent' : ''}`} 
                  onClick={() => {
                    setNumPage(page.numPage)
                    localStorage.setItem('numPage', page.numPage.toString())
                  }}>{page.numPage}</Link></li>))}
            </ul>
        </div>
        <Link className='pagNext' onClick={sumNum}>Siguiente</Link>
    </div>
  )
}
