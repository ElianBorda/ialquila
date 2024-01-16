import React from 'react'
import { Link, NavLink } from 'react-router-dom'
import logo from '../imgs/logonav.png'


export default function Nav() {
  return (
    <nav>
        <Link to='/'>
          <div className='logonav'>
            <img src={logo} alt='logo'/>
          </div>
        </Link>
      <NavLink className='btnNav' to='#'>Home</NavLink>
      <NavLink className='btnNav' to='#'>Departamento</NavLink>
      <NavLink className='btnNav' to='#'>Alquiler</NavLink>
      <NavLink className='btnNav' to='#'>Acerca de</NavLink>
    </nav>
  )
}
