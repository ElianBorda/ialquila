package ar.com.ialquila

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.data.mongodb.repository.config.EnableMongoRepositories

@SpringBootApplication
@EnableMongoRepositories
class IalquilaApplication

fun main(args: Array<String>) {
	runApplication<IalquilaApplication>(*args)
}
