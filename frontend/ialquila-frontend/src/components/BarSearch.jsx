import React from 'react'
import "../styles/barsearchstyle.css"


export default function BarSearch({setUbiBtn, ubiBtn}) {

  const valuesearch = ubiBtn===null ? "" : ubiBtn 

  const handlerChangeText = (e) => {
    setUbiBtn(e.target.value)
  }

  return (
    <div className='boxbarsearch'>
        <input className="barsearch" value={valuesearch} placeholder='buscar ubicacion...' type="text" name="nombre" onChange={handlerChangeText}/>
    </div>
  )
}
