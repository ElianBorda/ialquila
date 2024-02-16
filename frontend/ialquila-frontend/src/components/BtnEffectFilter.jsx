import React from 'react'
import "../styles/btneffectfilterstyle.css"
import { Link } from 'react-router-dom'

export default function BtnEffectFilter({categBtn, ordBtn, setCateg, setOrd}) {
  return (
    <Link className='clickboxbtneffect' onClick={() => { setCateg(categBtn);
                                                         setOrd(ordBtn);}}>
      <div className='boxbtneffect'>
        Buscar
      </div>
    </Link>
  )
}
