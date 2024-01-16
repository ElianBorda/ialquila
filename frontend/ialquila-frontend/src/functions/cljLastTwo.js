import React from 'react'

export default function cljLastTwo(numPage, minCantPage, cantPages) {
    const listjson = []

    const calc = Math.max(cantPages-4, 1)

    for (let i = calc; i <= cantPages; i++) {
                
        const pagina = {
            numPage: i,
            current: i == numPage,
        };
        listjson.push(pagina)
        
    }
    return (listjson)
}
