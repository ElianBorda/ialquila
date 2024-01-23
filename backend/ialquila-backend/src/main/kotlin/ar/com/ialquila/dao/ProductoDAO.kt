package ar.com.ialquila.dao

import ar.com.ialquila.model.Producto
import org.springframework.data.mongodb.repository.Aggregation
import org.springframework.data.mongodb.repository.MongoRepository

interface ProductoDAO: MongoRepository<Producto, String> {

    @Aggregation(pipeline = [
        "{\$match:{categoria: ?0}}",
    ])
    fun getProductosFiltradosPorCompra(modoDeCompra: String): List<Producto>
}