import React, { useState } from 'react'
import { Link, NavLink } from 'react-router-dom'
import logo from '../imgs/logonav.png'
import logo2 from '../imgs/logocontorno.png'
import FilterRadio from './FilterRadio'
import BarSearch from './BarSearch'
import BtnEffectFilter from './BtnEffectFilter'


export default function Nav({setCateg, setOrd, setUbi}) {
  
  const [categBtn, setCategBtn] = useState(null)
  const [ordBtn, setOrdBtn] = useState(null)
  const [ubiBtn, setUbiBtn] = useState(null)
  const [radSelected, setRadSelected] = useState(null)
  const [radSelected2, setRadSelected2] = useState(null)
  const [baractive, setBaractive] = useState('barverticalinactive')

  return (
    <nav>
        <Link onClick={() => {baractive === 'barverticalinactive' ? setBaractive('barverticalactive') : setBaractive('barverticalinactive')}}>
          <div className='btnvertical'></div>
        </Link>
        <div className={`barvertical ${baractive}`}>
          <div className='imgvertical'>
            <Link to='/'>
              <div className='logonavvertical'>
                <img src={logo2} alt='logo'/>
              </div>
            </Link>
          </div>
          <div className='contvertical'>
            <NavLink className='btnNavVertical' to='/todo'>Home</NavLink>
            <NavLink className='btnNavVertical' to='/departamentos'>Departamentos</NavLink>
            <NavLink className='btnNavVertical' to='/casas'>Casas</NavLink>
            <NavLink className='btnNavVertical' to='/informacion'>Acerca de</NavLink>
          </div>
        </div>
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
          <BarSearch setUbiBtn={setUbiBtn} ubiBtn={ubiBtn}/>
          <div className='subfilter'>
            <FilterRadio 
                text='Filtrar categoria' 
                name='category' 
                option1='Venta' 
                option2='Alquiler'
                setFilter={setCategBtn}
                elemnopt1='Venta'
                elemnopt2='Alquiler'
                setRadSelected={setRadSelected}
                radSelected={radSelected}/>

            <FilterRadio 
                text='Filtrar precio' 
                name='ord' 
                option1='Mayor a Menor' 
                option2='Menor a Mayor'
                setFilter={setOrdBtn}
                elemnopt1='-1'
                elemnopt2='1'
                setRadSelected={setRadSelected2}
                radSelected={radSelected2}/>
          </div>
          <BtnEffectFilter 
                categBtn={categBtn} 
                ordBtn={ordBtn} 
                ubiBtn={ubiBtn} 
                setCateg={setCateg} 
                setOrd={setOrd}
                setUbi={setUbi}
                setCategBtn={setCategBtn}
                setOrdBtn={setOrdBtn}
                setUbiBtn={setUbiBtn}
                setRadSelected={setRadSelected}
                setRadSelected2={setRadSelected2}/>
        </div> 
    </nav>
  )
}
