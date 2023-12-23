package ar.com.ialquila.model.exceptions

class NoExisteElAlquilerException(id: String) :
    Throwable("No existe el alquiler con id $id") {


}
