package ar.com.ialquila.dao

import ar.com.ialquila.model.Producto
import org.springframework.data.domain.Page
import org.springframework.data.domain.Pageable
import org.springframework.data.mongodb.repository.Aggregation
import org.springframework.data.mongodb.repository.MongoRepository

interface ProductoDAO: MongoRepository<Producto, String> {

    @Aggregation(pipeline = [
        "?0",
        "?1",
        "?2"
    ])
    fun getProductos(residencia: String, compra: String, ord: String, pageable: Pageable): List<Producto>
}
