import React from 'react'
import Card from '../Card';
import Paginate from '../Paginate';


export default function PrincipalContainerView({data, numPage, setNumPage, scrollRef1}) {
  return (
    <div className='container' ref={scrollRef1}>
        <div className='subcontainer'>
            {data?.map((card) => (<Card key={card.id} id={card.id} title={card.titulo} number={card.precio} exchange={card.cambio} img={card.img} location={card.ubicacion} link={card.link} residence={card.residencia}/>))}
        </div>
        <div className='pags'>
            <Paginate numPage={numPage} setNumPage={setNumPage} scrollRef1={scrollRef1}/>
        </div>
    </div>
  )
}
