import React from 'react'
import "../styles/landingstyle.css"
import logo from '../imgs/logo.png'
import { Link } from 'react-router-dom'


export default function Landing() {
  return (
    <div className='landingpage'>
        <div className='contentp'>
            <div className='logop'>
                <img src={logo} alt='logo'/>
            </div>
            <div className='descripcion'>
              <p>Tu buscador de alquileres de confianza</p>
            </div>
            <Link className='linkvivienda' to='/precios'>
              <div className='btnp'>Buscar vivienda</div>
            </Link>
        </div>
    </div>
  )
}
