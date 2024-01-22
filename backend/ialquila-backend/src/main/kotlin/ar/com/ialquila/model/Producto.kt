package ar.com.ialquila.model

import org.springframework.data.annotation.Id
import org.springframework.data.mongodb.core.mapping.Document

@Document
class Alquiler() {

    @Id
    var id: String? = null
    var titulo: String? = null
    var descripcion: String? = null
    var precio: Long? = null
    var cambio: String? = null
    var img: String? = null
    var ubicacion: String? = null
    var link: String? = null

    constructor(titulo: String, descripcion: String, precio: Long, cambio: String, img: String, ubicacion: String, link: String) : this() {
        this.titulo = titulo
        this.descripcion = descripcion
        this.precio = precio
        this.cambio = cambio
        this.img = img
        this.ubicacion = ubicacion
        this.link = link
    }
}