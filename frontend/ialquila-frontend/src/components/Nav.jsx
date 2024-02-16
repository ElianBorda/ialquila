import React, { useState } from 'react'
import { Link, NavLink } from 'react-router-dom'
import logo from '../imgs/logonav.png'
import FilterRadio from './FilterRadio'
import BarSearch from './BarSearch'
import BtnEffectFilter from './BtnEffectFilter'


export default function Nav({setCateg, setOrd}) {
  
  const [categBtn, setCategBtn] = useState(null)
  const [ordBtn, setOrdBtn] = useState(null)
  return (
    <nav>
        <div className='contentnav'>
          <Link to='/'>
            <div className='logonav'>
              <img src={logo} alt='logo'/>
            </div>
          </Link>
          <NavLink className='btnNav' to='/todo'>Home</NavLink>
          <NavLink className='btnNav' to='/departamentos'>Departamentos</NavLink>
          <NavLink className='btnNav' to='/casas'>Casas</NavLink>
          <NavLink className='btnNav' to='/informacion'>Acerca de</NavLink>
        </div>
        <div className='filternav'>
          <BarSearch />
          <div className='subfilter'>
            <FilterRadio 
                text='Filtrar categoria' 
                name='category' 
                option1='Venta' 
                option2='Alquiler'
                setFilter={setCategBtn}
                elemnopt1='Venta'
                elemnopt2='Alquiler'/>

            <FilterRadio 
                text='Filtrar precio' 
                name='ord' 
                option1='Por mayor' 
                option2='Por menor'
                setFilter={setOrdBtn}
                elemnopt1='-1'
                elemnopt2='1'/>
          </div>
          <BtnEffectFilter categBtn={categBtn} ordBtn={ordBtn} setCateg={setCateg} setOrd={setOrd}/>
        </div>

        
        
    </nav>
  )
}
