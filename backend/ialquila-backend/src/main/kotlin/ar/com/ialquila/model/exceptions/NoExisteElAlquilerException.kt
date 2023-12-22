package ar.com.ialquila.model.exceptions

class NoExisteElAlquilerException(id: Long) :
    Throwable("No existe el alquiler con id $id") {


}
