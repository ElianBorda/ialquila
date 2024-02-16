import React from 'react'
import "../styles/barsearchstyle.css"


export default function BarSearch() {
  return (
    <div className='boxbarsearch'>
        <input className="barsearch" placeholder='buscar...' type="text" name="nombre" />
    </div>
  )
}
