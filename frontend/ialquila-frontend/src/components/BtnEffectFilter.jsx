import React from 'react'
import "../styles/btneffectfilterstyle.css"
import { Link } from 'react-router-dom'

export default function BtnEffectFilter({categBtn, ordBtn, ubiBtn, setCateg, setOrd, setUbi, setCategBtn, setOrdBtn, setUbiBtn, setRadSelected, setRadSelected2}) {
  return (
    <Link className='clickboxbtneffect' onClick={() => { setCateg(categBtn);
                                                         setOrd(ordBtn);
                                                         setUbi(ubiBtn)
                                                         setCategBtn(null);
                                                         setOrdBtn(null)
                                                         setUbiBtn(null)
                                                         setRadSelected(null)
                                                         setRadSelected2(null)}}>
      <div className='boxbtneffect'>
        Buscar
      </div>
    </Link>
  )
}
