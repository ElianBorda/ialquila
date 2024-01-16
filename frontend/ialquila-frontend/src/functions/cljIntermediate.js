import React from 'react'

export default function cljIntermediate(numPage, minCantPage) {

    const listjson = []

    for (let i = (numPage-2); i <= minCantPage+(numPage - 3); i++) {
        
        const pagina = {
            numPage: i,
            current: i == numPage,
        };
        listjson.push(pagina)
    }    

  return (listjson)
}
