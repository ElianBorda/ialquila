import React from 'react'
import "../styles/btneffectfilterstyle.css"
import { Link } from 'react-router-dom'

export default function BtnEffectFilter() {
  return (
    <Link className='clickboxbtneffect'>
      <div className='boxbtneffect'>
        Buscar
      </div>
    </Link>
  )
}
