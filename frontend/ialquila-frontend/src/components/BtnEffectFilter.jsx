import React from 'react'
import "../styles/btneffectfilterstyle.css"
import { Link } from 'react-router-dom'

export default function BtnEffectFilter({categBtn, ordBtn, setCateg, setOrd, setCategBtn, setOrdBtn, setRadSelected, setRadSelected2}) {
  return (
    <Link className='clickboxbtneffect' onClick={() => { setCateg(categBtn);
                                                         setOrd(ordBtn);
                                                         setCategBtn(null);
                                                         setOrdBtn(null)
                                                         setRadSelected(null)
                                                         setRadSelected2(null)}}>
      <div className='boxbtneffect'>
        Buscar
      </div>
    </Link>
  )
}
