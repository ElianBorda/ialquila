package ar.com.ialquila.service

import ar.com.ialquila.model.Alquiler
import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.BeforeEach
import org.springframework.beans.factory.annotation.Autowired

class AlquilerServiceImplTest {

    @Autowired
    lateinit var alquilerService: AlquilerService

    lateinit var unAlquiler: Alquiler

    @BeforeEach
    fun setUp() {
        this.unAlquiler = Alquiler("Monoambiente", "Descripcion de la casa",
                                    120000, "https://www.unaimagen.com", "Nicaragua")
    }

    fun seVerificaQueSePersisteUnAlquiler() {
        val unAlquilerPersistido = this.alquilerService.save(this.unAlquiler)

        assertNotNull(unAlquilerPersistido.id)
    }

}