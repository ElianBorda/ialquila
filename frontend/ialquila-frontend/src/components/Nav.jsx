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
        <NavLink className='btnNav' to='/todo'>Home</NavLink>
        <NavLink className='btnNav' to='/departamentos'>Departamentos</NavLink>
        <NavLink className='btnNav' to='/casas'>Casas</NavLink>
        <NavLink className='btnNav' to='/informacion'>Acerca de</NavLink>
    </nav>
  )
}
