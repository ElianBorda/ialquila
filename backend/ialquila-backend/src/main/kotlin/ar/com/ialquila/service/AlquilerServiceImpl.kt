package ar.com.ialquila.service

import ar.com.ialquila.dao.AlquilerDAO
import ar.com.ialquila.model.Producto
import ar.com.ialquila.model.exceptions.NoExisteElAlquilerException
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.data.domain.PageRequest
import org.springframework.data.repository.findByIdOrNull
import org.springframework.stereotype.Service
import org.springframework.transaction.annotation.Transactional

@Service
@Transactional
class AlquilerServiceImpl: AlquilerService {

    @Autowired
    lateinit var alquilerDAO: AlquilerDAO

    override fun save(producto: Producto): Producto {
        return this.alquilerDAO.save(producto)
    }

    override fun saveAll(alquileres: List<Producto>) {
        this.alquilerDAO.saveAll(alquileres)
    }

    override fun update(producto: Producto): Producto {
        return this.alquilerDAO.save(producto)
    }

    override fun getAll(): List<Producto> {
        return this.alquilerDAO.findAll()
    }

    override fun getAllPageale(numPag: Int): List<Producto> {
        val pageable = PageRequest.of(numPag, 20)
        return this.alquilerDAO.findAll(pageable).toList()
    }


    override fun getById(id: String): Producto {
        return this.alquilerDAO.findByIdOrNull(id) ?: throw NoExisteElAlquilerException(id)
    }

    override fun getAmount(): Long {
        return this.alquilerDAO.count()
    }

    override fun delete(id: String) {
        this.alquilerDAO.deleteById(id)
    }

    override fun deleteAll() {
        this.alquilerDAO.deleteAll()
    }
}