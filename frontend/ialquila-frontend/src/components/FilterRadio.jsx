import React from 'react'
import { Link } from 'react-router-dom'

import "../styles/filterradiostyle.css"


export default function FilterRadio({text, name, option1, option2}) {
  return (
    <div className='boxfilter'>
        <ul className='headerfilter'>
          <li><a href='#'>{text}</a>
              <ul className='verticalfilter'>
                <li><input type="radio" name={name} value={option1} id={option1}/><label htmlFor={option1}>{option1}</label></li>
                <li><input type="radio" name={name} value={option2} id={option2}/><label htmlFor={option2}>{option2}</label></li>
              </ul>
          </li>
            
        </ul>
    </div>
  )
}
