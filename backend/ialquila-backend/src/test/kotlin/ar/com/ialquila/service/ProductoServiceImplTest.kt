package ar.com.ialquila.service

import ar.com.ialquila.model.Producto
import org.junit.jupiter.api.AfterEach
import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.BeforeEach
import org.junit.jupiter.api.Test
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.test.context.SpringBootTest

@SpringBootTest
class ProductoServiceImplTest {

    @Autowired
    lateinit var productoService: ProductoService

    lateinit var unProducto: Producto
    lateinit var unProducto1: Producto
    lateinit var unProducto2: Producto
    lateinit var unProducto3: Producto


    @BeforeEach
    fun setUp() {
        this.unProducto = Producto("Monoambiente", "Descripcion de la casa",
                                    120000, "$", "https://www.unaimagen.com", "Nicaragua", "link", "Alquiler")
        this.unProducto1 = Producto("Monoambiente1", "Descripcion de la casa1",
            120000, "$", "https://www.unaimagen1.com", "Nicaragua1", "link1", "Alquiler")
        this.unProducto2 = Producto("Monoambiente2", "Descripcion de la casa2",
            120000, "$", "https://www.unaimagen.com2", "Nicaragua2", "link2", "Alquiler")
        this.unProducto3 = Producto("Monoambiente3", "Descripcion de la casa3",
            120000, "$", "https://www.unaimagen3.com", "Nicaragua3", "link3", "Alquiler")
    }

    @Test
    fun seVerificaQueSePersisteUnAlquiler() {
        val unAlquilerPersistido = this.productoService.save(this.unProducto)

        assertNotNull(unAlquilerPersistido.id)
    }

    @Test
    fun seVerificaQueSePuedeRecuperarUnAlquiler(){
        val unAlquiler           = this.productoService.save(this.unProducto)
        val unAlquilerRecuperado = this.productoService.getById(unAlquiler.id!!)

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
        this.productoService.save(this.unProducto)
        this.productoService.save(this.unProducto1)
        this.productoService.save(this.unProducto2)
        this.productoService.save(this.unProducto3)

        var alquileres: List<Producto> = this.productoService.getAllPageale(0)

        assertEquals(4, alquileres.size)
    }

    @Test
    fun deleteAll(){}

    @AfterEach
    fun tearDown(){
        this.productoService.deleteAll()
    }

}