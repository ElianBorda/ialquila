package ar.com.ialquila.dao

import ar.com.ialquila.model.Alquiler
import org.springframework.data.mongodb.repository.MongoRepository

interface AlquilerDAO: MongoRepository<Alquiler, String> {
}