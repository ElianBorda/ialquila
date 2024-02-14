import React from 'react'
import "../styles/cardstyle.css"
import { Link } from 'react-router-dom'

export default function Card(props) {
    
    return (
        <Link className='link' to={props.link}>
            <div className={`tag ${props.residence === 'Departamentos' ? 'colorDep' : 'colorCas'}`}>{props.residence === 'Departamentos' ? 'Departamento' : 'Casa'}</div>
            <div className='card'>
                <div className='imgs'><img src={props.img} alt='imagen'/></div>
                <div className='info'>
                    <div className='title'><h3>{props.title}</h3></div>
                    <div className='location'>{props.location}</div>
                    <div className='price'>
                    {props.exchange === 'Consultar' && props.number === 0
                    ? props.exchange
                    : `${props.exchange}${props.number}`}
                    </div>
                </div>
            </div>
        </Link>    
    )
}
