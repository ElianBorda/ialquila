import React from 'react'
import "../styles/paginatestyle.css"
import { useFetch } from '../apis/useFetch';
import createListJson from '../functions/createListJson'
import PaginateView from './views/PaginateView';


export default function Paginate({numPage, setNumPage}) {
  
    const cantCards = useFetch("http://localhost:8080/home/alquileres/count")
    const cantPages = Math.ceil(cantCards.data/20)
    const minCantPage = Math.min(cantPages, 5)
    const pagesList   = createListJson( minCantPage, numPage, cantPages )

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

    return (<PaginateView subNum={subNum} sumNum={sumNum} pagesList={pagesList} setNumPage={setNumPage} numPage={numPage}/>)
  
}
