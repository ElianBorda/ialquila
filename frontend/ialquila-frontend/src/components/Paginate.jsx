import React from 'react'
import "../styles/paginatestyle.css"
import { Link } from 'react-router-dom'
import { useFetch } from '../apis/useFetch';
import createListJson from '../functions/createListJson'


export default function Paginate({numPage, setNumPage}) {
  
  const cantCards = useFetch("http://localhost:8080/home/alquileres/count")
  const cantPages = Math.ceil(cantCards.data/20)

    const sumNum = () => {
        const newPage    = numPage + 1
        const nuevoValor = newPage > cantPages ? numPage : newPage
        setNumPage(nuevoValor)
        localStorage.setItem('numPage', nuevoValor.toString());
    }

    const subNum = () => {
        const newPage    = numPage - 1
        const nuevoValor = newPage <= 0 ? 1 : newPage
        setNumPage(nuevoValor)
        localStorage.setItem('numPage', nuevoValor.toString());
    }

  
  const minCantPage = Math.min(cantPages, 5)
  const pagesList   = createListJson( minCantPage, numPage, cantPages )

  return (
    <div className='pagContainer'>
      <Link className='pagNext' onClick={subNum}>Anterior</Link>
      <div className='pagList'>
        <ul>
          {pagesList.map((page) => (<li><Link className={`linkPag ${page.current ? 'pageCurrent' : ''}`} onClick={() => setNumPage(page.numPage)}>{page.numPage}</Link></li>))}
        </ul>
      </div>
      <Link className='pagNext' onClick={sumNum}>Siguiente</Link>
    </div>
  )
}
