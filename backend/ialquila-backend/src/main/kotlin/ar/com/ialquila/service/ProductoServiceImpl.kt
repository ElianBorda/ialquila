package ar.com.ialquila.service

import ar.com.ialquila.dao.ProductoDAO
import ar.com.ialquila.model.Producto
import ar.com.ialquila.model.exceptions.NoExisteElAlquilerException
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.data.domain.PageRequest
import org.springframework.data.repository.findByIdOrNull
import org.springframework.stereotype.Service
import org.springframework.transaction.annotation.Transactional

@Service
@Transactional
class ProductoServiceImpl: ProductoService {

    @Autowired
    lateinit var productoDAO: ProductoDAO

    override fun save(producto: Producto): Producto {
        return this.productoDAO.save(producto)
    }

    override fun saveAll(alquileres: List<Producto>) {
        this.productoDAO.saveAll(alquileres)
    }

    override fun update(producto: Producto): Producto {
        return this.productoDAO.save(producto)
    }

    override fun getAll(): List<Producto> {
        return this.productoDAO.findAll()
    }

    override fun getAllPageale(numPag: Int): List<Producto> {
        val pageable = PageRequest.of(numPag, 20)
        return this.productoDAO.findAll(pageable).toList()
    }


    override fun getById(id: String): Producto {
        return this.productoDAO.findByIdOrNull(id) ?: throw NoExisteElAlquilerException(id)
    }

    override fun getAmount(): Long {
        return this.productoDAO.count()
    }

    override fun delete(id: String) {
        this.productoDAO.deleteById(id)
    }

    override fun deleteAll() {
        this.productoDAO.deleteAll()
    }

    override fun getProductosFiltradosPorCompra(modoDeCompra: String): List<Producto> {
        return this.productoDAO.getProductosFiltradosPorCompra(modoDeCompra)
    }

    override fun getProductosFiltradosPorResidencia(residencia: String): List<Producto> {
        return this.productoDAO.getProductosFiltradosPorResidencia(residencia)
    }

    override fun getProductosOrdenados(sorted: Int): List<Producto> {
        return this.productoDAO.getProductosOrdenados(sorted)
    }
}