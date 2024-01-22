package ar.com.ialquila.controller.dto

import ar.com.ialquila.model.Producto

class AlquilerDTO(
    val id: String?,
    val titulo: String?,
    val descripcion: String?,
    val precio: Long?,
    val cambio: String?,
    val img: String?,
    val ubicacion: String?,
    val link: String?,
    val categoria: String?
) {

    companion object {
        fun desdeModeloAJson(producto: Producto) =
            AlquilerDTO(
                producto.id,
                producto.titulo,
                producto.descripcion,
                producto.precio,
                producto.cambio,
                producto.img,
                producto.ubicacion,
                producto.link,
                producto.categoria
            )

    }

    fun desdeJsonAModelo(): Producto {
        val producto         = Producto()
        producto.id          = this.id
        producto.titulo      = this.titulo
        producto.descripcion = this.descripcion
        producto.precio      = this.precio
        producto.cambio      = this.cambio
        producto.img         = this.img
        producto.ubicacion   = this.ubicacion
        producto.link        = this.link
        producto.categoria   = this.categoria
        return producto
    }

}