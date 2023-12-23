package ar.com.ialquila.service

import ar.com.ialquila.dao.AlquilerDAO
import ar.com.ialquila.model.Alquiler
import ar.com.ialquila.model.exceptions.NoExisteElAlquilerException
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.data.repository.findByIdOrNull
import org.springframework.stereotype.Service
import org.springframework.transaction.annotation.Transactional

@Service
@Transactional
class AlquilerServiceImpl: AlquilerService {

    @Autowired
    lateinit var alquilerDAO: AlquilerDAO

    override fun save(alquiler: Alquiler): Alquiler {
        return this.alquilerDAO.save(alquiler)
    }

    override fun saveAll(alquileres: List<Alquiler>) {
        return this.saveAll(alquileres)
    }

    override fun update(alquiler: Alquiler): Alquiler {
        return this.alquilerDAO.save(alquiler)
    }

    override fun getAll(): List<Alquiler> {
        return this.alquilerDAO.findAll()
    }

    override fun getById(id: String): Alquiler {
        return this.alquilerDAO.findByIdOrNull(id) ?: throw NoExisteElAlquilerException(id)
    }

    override fun delete(id: String) {
        this.alquilerDAO.deleteById(id)
    }

    override fun deleteAll() {
        this.alquilerDAO.deleteAll()
    }
}