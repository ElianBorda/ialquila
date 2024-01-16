package ar.com.ialquila.service

import ar.com.ialquila.model.Alquiler
import org.junit.jupiter.api.AfterEach
import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.BeforeEach
import org.junit.jupiter.api.Test
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.test.context.SpringBootTest
import org.springframework.data.domain.Page
import org.springframework.data.domain.Pageable

@SpringBootTest
class AlquilerServiceImplTest {

    @Autowired
    lateinit var alquilerService: AlquilerService

    lateinit var unAlquiler: Alquiler
    lateinit var unAlquiler1: Alquiler
    lateinit var unAlquiler2: Alquiler
    lateinit var unAlquiler3: Alquiler


    @BeforeEach
    fun setUp() {
        this.unAlquiler = Alquiler("Monoambiente", "Descripcion de la casa",
                                    120000, "$", "https://www.unaimagen.com", "Nicaragua", "link")
        this.unAlquiler1 = Alquiler("Monoambiente1", "Descripcion de la casa1",
            120000, "$", "https://www.unaimagen1.com", "Nicaragua1", "link1")
        this.unAlquiler2 = Alquiler("Monoambiente2", "Descripcion de la casa2",
            120000, "$", "https://www.unaimagen.com2", "Nicaragua2", "link2")
        this.unAlquiler3 = Alquiler("Monoambiente3", "Descripcion de la casa3",
            120000, "$", "https://www.unaimagen3.com", "Nicaragua3", "link3")
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
        assertEquals(unAlquilerRecuperado.link, unAlquiler.link)
    }

    @Test
    fun seVerificaQueSeRecuparaAlquileresPaginados(){
        this.alquilerService.save(this.unAlquiler)
        this.alquilerService.save(this.unAlquiler1)
        this.alquilerService.save(this.unAlquiler2)
        this.alquilerService.save(this.unAlquiler3)

        var alquileres: List<Alquiler> = this.alquilerService.getAllPageale(0)

        assertEquals(4, alquileres.size)
    }

    @Test
    fun deleteAll(){}

    @AfterEach
    fun tearDown(){
        this.alquilerService.deleteAll()
    }

}