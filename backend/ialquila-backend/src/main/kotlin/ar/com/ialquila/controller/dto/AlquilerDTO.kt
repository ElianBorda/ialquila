package ar.com.ialquila.controller.dto

import ar.com.ialquila.model.Alquiler

class AlquilerDTO(
    val id: String?,
    val titulo: String?,
    val descripcion: String?,
    val precio: Long?,
    val img: String?,
    val ubicacion: String?
) {

    companion object {
        fun desdeModeloAJson(alquiler: Alquiler) =
            AlquilerDTO(
                alquiler.id,
                alquiler.titulo,
                alquiler.descripcion,
                alquiler.precio,
                alquiler.img,
                alquiler.ubicacion
            )

    }

    fun desdeJsonAModelo(): Alquiler {
        val alquiler         = Alquiler()
        alquiler.id          = this.id
        alquiler.titulo      = this.titulo
        alquiler.descripcion = this.descripcion
        alquiler.precio      = this.precio
        alquiler.img         = this.img
        alquiler.ubicacion   = this.ubicacion
        return alquiler
    }

}