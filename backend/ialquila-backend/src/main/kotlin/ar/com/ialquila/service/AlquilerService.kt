package ar.com.ialquila.service

import ar.com.ialquila.dao.AlquilerDAO
import ar.com.ialquila.model.Alquiler
import org.springframework.beans.factory.annotation.Autowired

interface AlquilerService {

    fun save(alquiler: Alquiler): Alquiler
    fun saveAll(alquileres: List<Alquiler>)
    fun update(alquiler: Alquiler): Alquiler
    fun getAll(): List<Alquiler>
    fun getById(id: String): Alquiler
    fun delete(id: String)
    fun deleteAll()
}