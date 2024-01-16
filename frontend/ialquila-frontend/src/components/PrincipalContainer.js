import React, { useState, useEffect } from 'react'
import "../styles/containerstyle.css"
import Card from './Card';
import Paginate from './Paginate';
import { useFetch } from '../apis/useFetch';


export default function PrincipalContainer() {
    const initialNumPage = parseInt(localStorage.getItem('numPage')) || 1;
    const [numPage, setNumPage] = useState(initialNumPage)
    const { data } = useFetch(`http://localhost:8080/home/alquileres/${numPage}`, numPage)

    useEffect(() => {
      const storedNumPage = parseInt(localStorage.getItem('numPage'));
      if (!isNaN(storedNumPage)) {
        setNumPage(storedNumPage);
      }
    }, []); 

  return (
    <div className='container'>
        <div className='subcontainer'>
        {data?.map((card) => (<Card key={card.id} id={card.id} title={card.titulo} number={card.precio} exchange={card.cambio} img={card.img} location={card.ubicacion}/>))}
        </div>
        <div className='pags'>
          <Paginate numPage={numPage} setNumPage={setNumPage}/>
        </div>
    </div>
  )
}
