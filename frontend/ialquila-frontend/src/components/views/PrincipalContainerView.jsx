import React from 'react'
import Card from '../Card';
import Paginate from '../Paginate';


export default function PrincipalContainerView({data, numPage, setNumPage}) {
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
