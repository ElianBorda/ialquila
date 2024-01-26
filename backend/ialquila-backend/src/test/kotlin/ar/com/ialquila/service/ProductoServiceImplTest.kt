package ar.com.ialquila.service

import ar.com.ialquila.dao.ProductoDAO
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

    @Autowired
    lateinit var productoDAO: ProductoDAO

    lateinit var unProducto: Producto
    lateinit var unProducto1: Producto
    lateinit var unProducto2: Producto
    lateinit var unProducto3: Producto


    @BeforeEach
    fun setUp() {
        this.unProducto = Producto("Monoambiente", "Descripcion de la casa",
                                    100000, "$", "https://www.unaimagen.com", "Nicaragua", "link", "Venta", "Departamento")
        this.unProducto1 = Producto("Monoambiente1", "Descripcion de la casa1",
            995, "$", "https://www.unaimagen1.com", "Nicaragua1", "link1", "Venta", "Casa")
        this.unProducto2 = Producto("Monoambiente2", "Descripcion de la casa2",
            35700, "$", "https://www.unaimagen.com2", "Nicaragua2", "link2", "Venta", "Casa")
        this.unProducto3 = Producto("Monoambiente3", "Descripcion de la casa3",
            17777, "$", "https://www.unaimagen3.com", "Nicaragua3", "link3", "Alquiler", "Casa")
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
    fun seVerificaQueSeRecuparaAlquileresPaginadosDeTodosLosProductos(){
        this.productoService.save(this.unProducto)
        this.productoService.save(this.unProducto1)
        this.productoService.save(this.unProducto2)
        this.productoService.save(this.unProducto3)

        var alquileres: List<Producto> = this.productoService.getProductos(null, null, null, 0)

        assertEquals(4, alquileres.size)
    }

    @Test
    fun seVerificaQueSeRecuparaAlquileresPaginadosDeUnFiltroDeResidencia(){
        this.productoService.save(this.unProducto)
        this.productoService.save(this.unProducto1)
        this.productoService.save(this.unProducto2)
        this.productoService.save(this.unProducto3)

        var alquileres: List<Producto> = this.productoService.getProductos("Casa", null, null, 0)

        assertEquals(3, alquileres.size)
    }

    @Test
    fun seVerificaQueSeRecuparaAlquileresPaginadosDeUnFiltroDeCompra(){
        this.productoService.save(this.unProducto)
        this.productoService.save(this.unProducto1)
        this.productoService.save(this.unProducto2)
        this.productoService.save(this.unProducto3)

        var alquileres: List<Producto> = this.productoService.getProductos("Casa", null, null, 0)

        assertEquals(3, alquileres.size)
    }

    @Test
    fun seVerificaQueSeRecuparaAlquileresPaginadosDeUnFiltroDeOrdenAcendente(){
        this.productoService.save(this.unProducto)
        this.productoService.save(this.unProducto1)
        this.productoService.save(this.unProducto2)
        this.productoService.save(this.unProducto3)

        var alquileres: List<Producto> = this.productoService.getProductos(null, null, 1, 0)

        assertEquals(4, alquileres.size)
        assertEquals(995, alquileres.first().precio)
        assertEquals(100000, alquileres.last().precio)
    }

    @Test
    fun seVerificaQueSeRecuparaAlquileresPaginadosDeUnFiltroDeOrdenDecendente(){
        this.productoService.save(this.unProducto)
        this.productoService.save(this.unProducto1)
        this.productoService.save(this.unProducto2)
        this.productoService.save(this.unProducto3)

        var alquileres: List<Producto> = this.productoService.getProductos(null, null, -1, 0)

        assertEquals(4, alquileres.size)
        assertEquals(100000, alquileres.first().precio)
        assertEquals(995, alquileres.last().precio)
    }

    @Test
    fun deleteAll(){}

    @Test
    fun seVerificaQueSePuedeFiltrarPorCasasYDepartamentos(){
        this.productoService.save(this.unProducto)
        this.productoService.save(this.unProducto1)
        this.productoService.save(this.unProducto3)
        this.productoService.save(this.unProducto2)
        val productos: List<Producto> = this.productoService.getProductosFiltradosPorResidencia("Casa")
        val productos2: List<Producto> = this.productoService.getProductosFiltradosPorResidencia("Departamento")

        assertEquals(productos.size, 3)
        assertEquals(productos2.size, 1)

    }

    @Test
    fun seVerificaQueSePuedeFiltrarPorVentasYAlquileres(){
        this.productoService.save(this.unProducto)
        this.productoService.save(this.unProducto1)
        this.productoService.save(this.unProducto3)
        this.productoService.save(this.unProducto2)

        var productos: List<Producto> = this.productoService.getProductosFiltradosPorCompra("Venta")

        assertEquals(productos.size, 3)
    }

    @Test
    fun seVerficaQueSePuedenTraerLosDatosOrdenadosDeMenorAMayor(){
        val productoMayor = this.productoService.save(this.unProducto)
        val productoMenor = this.productoService.save(this.unProducto1)
        this.productoService.save(this.unProducto2)
        this.productoService.save(this.unProducto3)

        var productosMenorMayor: List<Producto> = this.productoService.getProductosOrdenados(1)
        var productosMayorMenor: List<Producto> = this.productoService.getProductosOrdenados(-1)

        assertEquals(productosMenorMayor.first().id, productoMenor.id!!)
        assertEquals(productosMayorMenor.first().id, productoMayor.id!!)

    }

    @AfterEach
    fun tearDown(){
        //this.productoService.deleteAll()
    }

}