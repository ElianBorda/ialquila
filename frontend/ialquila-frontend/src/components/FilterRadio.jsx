import React, { useState } from 'react'
import { Link } from 'react-router-dom'

import "../styles/filterradiostyle.css"


export default function FilterRadio(
  {text, name, option1, option2, setFilter, elemnopt1, 
    elemnopt2, setRadSelected, radSelected}) {

  return (
    <div className='boxfilter'>
        <ul className='headerfilter'>
          <li><a href='#'>{text}</a>
              <ul className='verticalfilter'>
                <li onClick={() => {setRadSelected(1); setFilter(elemnopt1)}}>
                  <div className={radSelected === 1 ? "colorrad" : ""}></div>
                  <input className='inputradio' 
                        //  checked = {radSelected === 1}
                         type="radio" 
                         name={name} 
                         value={option1} 
                         id={option1}/>
                  <label className='labelradio' htmlFor={option1}>{option1}</label>
                </li>
                <li onClick={() => {setRadSelected(2); setFilter(elemnopt2)}}>
                  <div className={radSelected === 2 ? "colorrad" : ""}></div>
                  <input className='inputradio'
                        //  checked = {radSelected === 2} 
                         type="radio" 
                         name={name} 
                         value={option2} 
                         id={option2}/>
                  <label className='labelradio' htmlFor={option2}>{option2}</label>
                </li>
              </ul>
          </li>
            
        </ul>
    </div>
  )
}
