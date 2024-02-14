import React from 'react'
import "../styles/paginatestyle.css"
import { useFetch } from '../apis/useFetch';
import createListJson from '../functions/createListJson'
import PaginateView from './views/PaginateView';


export default function Paginate({numPage, setNumPage, scrollRef1}) {
    const cantCards = useFetch("http://localhost:8080/home/alquileres/count")
    const cantPages = Math.ceil(cantCards.data/20)
    const minCantPage = Math.min(cantPages, 5)
    const pagesList   = createListJson( minCantPage, numPage, cantPages )

    const scrollUp = (scrollRef) => {
        if (scrollRef.current) {
          scrollRef.current.scrollTop = 0;
        }
    };

    const sumNum = () => {
        scrollUp(scrollRef1)
        const newPage    = numPage + 1
        const nuevoValor = newPage > cantPages ? numPage : newPage
        setNumPage(nuevoValor)
        localStorage.setItem('numPage', nuevoValor.toString())
    }

    const subNum = () => {
        scrollUp(scrollRef1)
        const newPage    = numPage - 1
        const nuevoValor = newPage <= 0 ? 1 : newPage
        setNumPage(nuevoValor)
        localStorage.setItem('numPage', nuevoValor.toString())
    }

    return (<PaginateView subNum={subNum} sumNum={sumNum} pagesList={pagesList} setNumPage={setNumPage} cant={cantPages} scroll={scrollUp} scrollRef1={scrollRef1}/>)
  
}
