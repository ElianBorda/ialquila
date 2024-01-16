import React from 'react'

export default function cljFirstTwo(numPage, minCantPage) {
    const listjson = []
    for (let i = 1; i <= minCantPage; i++) {
        const pagina = {
            numPage: i,
            current: i == numPage,
        };
        listjson.push(pagina)
    }

  return (listjson)
}
