package ar.com.ialquila.service

import ar.com.ialquila.dao.ProductoDAO
import ar.com.ialquila.model.Producto
import ar.com.ialquila.model.exceptions.NoExisteElAlquilerException
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.data.domain.PageRequest
import org.springframework.data.domain.Pageable
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

    override fun getProductos(residencia: String?, compra: String?, ord: Int?, ubiencode: String? ,numPag: Int): List<Producto> {
        val pageable: Pageable = PageRequest.of(numPag, 20)
        val res = if (residencia != null) {"{\$match: {residencia: $residencia}}"} else { "{\$match: {}}"}
        val compras = if (compra != null) {"{\$match: {categoria: $compra}}"} else { "{\$match: {}}"}
        val ubi = if (ubiencode != null) {"{\$match: {ubicacion: {\$regex: /$ubiencode/, \$options: 'i'}}}"} else { "{\$match: {}}"}
        val ords = if (ord != null) {"{\$sort: {precio: $ord}}"} else { "{\$match: {}}"}


        return productoDAO.getProductos(res, compras, ords, ubi, pageable)
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

}