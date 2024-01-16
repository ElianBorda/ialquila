import React from 'react'
import isFirstTwo from './isFirstTwo'
import isLastTwo from './isLastTwo'
import cljFirstTwo from './cljFirstTwo'
import cljLastTwo from './cljLastTwo'
import cljIntermediate from './cljIntermediate'


export default function createListJson(minCantPage, numPage, cantPages) {
    const numPageAlt = Math.max(1, Math.min(numPage, cantPages))
    let listJson   = []
    
    if (isFirstTwo(numPageAlt)){
        listJson = cljFirstTwo(numPageAlt, minCantPage)
    }else if (isLastTwo(numPageAlt, cantPages)){
        listJson = cljLastTwo(numPageAlt, minCantPage, cantPages)
    } else {
        listJson = cljIntermediate(numPageAlt, minCantPage)
        console.log(listJson)
    }

  return (listJson)
}
