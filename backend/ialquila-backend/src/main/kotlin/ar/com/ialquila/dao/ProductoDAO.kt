package ar.com.ialquila.dao

import ar.com.ialquila.model.Producto
import org.springframework.data.domain.Page
import org.springframework.data.domain.Pageable
import org.springframework.data.mongodb.repository.Aggregation
import org.springframework.data.mongodb.repository.MongoRepository

interface ProductoDAO: MongoRepository<Producto, String> {

    @Aggregation(pipeline = [
        "{\$match:{categoria: ?0}}",
    ])
    fun getProductosFiltradosPorCompra(modoDeCompra: String): List<Producto>

    @Aggregation(pipeline = [
        "{\$match: {residencia: ?0}}"
    ])
    fun getProductosFiltradosPorResidencia(residencia: String): List<Producto>

    @Aggregation(pipeline = [
        "{\$sort: {precio: ?0}}"
    ])
    fun getProductosOrdenados(sorted: Int): List<Producto>

    @Aggregation(pipeline = [
        "?0",
        "?1",
        "?2"
    ])
    fun getProductos(residencia: String, compra: String, ord: String, pageable: Pageable): List<Producto>
}
