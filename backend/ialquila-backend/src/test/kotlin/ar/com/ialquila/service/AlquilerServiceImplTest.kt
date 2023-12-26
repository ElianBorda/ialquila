package ar.com.ialquila.service

import ar.com.ialquila.model.Alquiler
import org.junit.jupiter.api.AfterEach
import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.BeforeEach
import org.junit.jupiter.api.Test
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.test.context.SpringBootTest

@SpringBootTest
class AlquilerServiceImplTest {

    @Autowired
    lateinit var alquilerService: AlquilerService

    lateinit var unAlquiler: Alquiler

    @BeforeEach
    fun setUp() {
        this.unAlquiler = Alquiler("Monoambiente", "Descripcion de la casa",
                                    120000, "$", "https://www.unaimagen.com", "Nicaragua")
    }

    @Test
    fun seVerificaQueSePersisteUnAlquiler() {
        val unAlquilerPersistido = this.alquilerService.save(this.unAlquiler)

        assertNotNull(unAlquilerPersistido.id)
    }

    @Test
    fun seVerificaQueSePuedeRecuperarUnAlquiler(){
        val unAlquiler           = this.alquilerService.save(this.unAlquiler)
        val unAlquilerRecuperado = this.alquilerService.getById(unAlquiler.id!!)

        assertEquals(unAlquilerRecuperado.id, unAlquiler.id)
        assertEquals(unAlquilerRecuperado.img, unAlquiler.img)
        assertEquals(unAlquilerRecuperado.precio, unAlquiler.precio)
        assertEquals(unAlquilerRecuperado.titulo, unAlquiler.titulo)
        assertEquals(unAlquilerRecuperado.cambio, unAlquiler.cambio)
        assertEquals(unAlquilerRecuperado.descripcion, unAlquiler.descripcion)
        assertEquals(unAlquilerRecuperado.ubicacion, unAlquiler.ubicacion)
    }

    @AfterEach
    fun tearDown(){
        this.alquilerService.deleteAll()
    }

}