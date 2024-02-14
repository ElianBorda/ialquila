package ar.com.ialquila.controller.dto

import ar.com.ialquila.model.Producto

class ProductoDTO(
    val id: String?,
    val titulo: String?,
    val precio: Long?,
    val cambio: String?,
    val img: String?,
    val ubicacion: String?,
    val link: String?,
    val categoria: String?,
    val residencia: String?
) {

    companion object {
        fun desdeModeloAJson(producto: Producto) =
            ProductoDTO(
                producto.id,
                producto.titulo,
                producto.precio,
                producto.cambio,
                producto.img,
                producto.ubicacion,
                producto.link,
                producto.categoria,
                producto.residencia
            )

    }

    fun desdeJsonAModelo(): Producto {
        val producto         = Producto()
        producto.id          = this.id
        producto.titulo      = this.titulo
        producto.precio      = this.precio
        producto.cambio      = this.cambio
        producto.img         = this.img
        producto.ubicacion   = this.ubicacion
        producto.link        = this.link
        producto.categoria   = this.categoria
        producto.residencia  = this.residencia
        return producto
    }

}