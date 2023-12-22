package ar.com.ialquila.model

import org.springframework.data.annotation.Id
import org.springframework.data.mongodb.core.mapping.Document

@Document
class Alquiler {

    @Id
    var id: String? = null
    var titulo: String? = null
    var descripcion: String? = null
    var precio: Long? = null
    var img: String? = null

    constructor(titulo: String, descripcion: String, precio: Long, img: String){
        
    }
}