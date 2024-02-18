import React, { useState, useEffect, useRef} from 'react'
import "../styles/containerstyle.css"
import { useFetch } from '../apis/useFetch';
import PrincipalContainerView from './views/PrincipalContainerView';


export default function PrincipalContainer({typefilter, ord, categ, ubi}) {

    const scrollRef1            = useRef(null);
    const initialNumPage        = parseInt(localStorage.getItem('numPage')) || 1;
    const [numPage, setNumPage] = useState(initialNumPage)
    const ubiencode             = ubi==!'null' ? 'null' :encodeURIComponent(ubi)  
  

    console.log(ubiencode)
    const { data }              = useFetch(`http://localhost:8080/home/filter/${typefilter}/${categ}/${ord}/${ubiencode}/${numPage}`, numPage)


    useEffect(() => {
      const storedNumPage = parseInt(localStorage.getItem('numPage'));
      if (!isNaN(storedNumPage)) {
        setNumPage(storedNumPage);
      }
    }, []); 


    return (<PrincipalContainerView data={data} numPage={numPage} setNumPage={setNumPage} scrollRef1={scrollRef1}/>)
}
