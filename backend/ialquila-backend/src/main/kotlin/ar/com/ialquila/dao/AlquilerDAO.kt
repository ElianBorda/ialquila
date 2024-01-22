package ar.com.ialquila.dao

import ar.com.ialquila.model.Producto
import org.springframework.data.mongodb.repository.MongoRepository

interface AlquilerDAO: MongoRepository<Producto, String> {
}