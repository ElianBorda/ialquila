import React, { useState, useEffect } from 'react'
import "../styles/containerstyle.css"
import { useFetch } from '../apis/useFetch';
import PrincipalContainerView from './views/PrincipalContainerView';


export default function PrincipalContainer() {


    const initialNumPage = parseInt(localStorage.getItem('numPage')) || 1;
    const [numPage, setNumPage] = useState(initialNumPage)
    const { data } = useFetch(`http://localhost:8080/home/filter/null/null/null/${numPage}`, numPage)

    useEffect(() => {
      const storedNumPage = parseInt(localStorage.getItem('numPage'));
      if (!isNaN(storedNumPage)) {
        setNumPage(storedNumPage);
      }
    }, []); 


    return (<PrincipalContainerView data={data} numPage={numPage} setNumPage={setNumPage}/>)
}
