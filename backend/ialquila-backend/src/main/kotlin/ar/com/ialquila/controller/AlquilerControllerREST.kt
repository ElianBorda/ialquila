package ar.com.ialquila.controller

import ar.com.ialquila.controller.dto.AlquilerDTO
import ar.com.ialquila.model.Producto
import ar.com.ialquila.service.AlquilerService
import com.fasterxml.jackson.module.kotlin.jacksonObjectMapper
import com.fasterxml.jackson.module.kotlin.readValue
import org.springframework.web.bind.annotation.CrossOrigin
import org.springframework.web.bind.annotation.DeleteMapping
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PathVariable
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.PutMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController
import java.io.File
import java.io.IOException

@RestController
@CrossOrigin
@RequestMapping("/home")
class AlquilerControllerREST(private val alquilerService: AlquilerService) {

    @GetMapping("/alquileres")
    fun todosLosAlquileres() = alquilerService.getAll().map { alquiler -> AlquilerDTO.desdeModeloAJson(alquiler) }

    @PostMapping("/guardar/alquiler")
    fun guardarAlquiler(@RequestBody alquiler: AlquilerDTO) = alquilerService.save(alquiler.desdeJsonAModelo())

    @PostMapping("/guardar/alquileres")
    fun guardarAlquileres(@RequestBody alquileres: List<AlquilerDTO>) =
        alquilerService.saveAll(alquileres.map { a -> a.desdeJsonAModelo() })

    @GetMapping("/alquileres/{numPag}")
    fun obtenerAlquileresPaginados(@PathVariable numPag: Int): List<Producto> {
        return alquilerService.getAllPageale(numPag-1)
    }

    @GetMapping("/alquileres/count")
    fun obtenerAlquileresPaginados(): Long {
        return alquilerService.getAmount()
    }

    @GetMapping("/alquiler/{id}")
    fun obtenerAlquiler(@PathVariable id: String) = AlquilerDTO.desdeModeloAJson(alquilerService.getById(id))

    @PutMapping("/actualizar-alquiler/{id}")
    fun actualizarAlquiler(@RequestBody alquiler: AlquilerDTO, @PathVariable id: String) {
        val alquilerAActualizar = alquilerService.getById(id)
        alquilerAActualizar.titulo = alquiler.titulo
        alquilerAActualizar.descripcion = alquiler.descripcion
        alquilerAActualizar.img         = alquiler.img
        alquilerAActualizar.precio      = alquiler.precio
        alquilerAActualizar.cambio      = alquiler.cambio
        alquilerAActualizar.ubicacion   = alquiler.ubicacion
        alquilerAActualizar.link        = alquiler.link
        alquilerAActualizar.categoria   = alquiler.categoria
        alquilerService.update(alquilerAActualizar)
    }

    @PostMapping("/script")
    fun guardarAlquileresScript() {
        try {
            val processBuilder = ProcessBuilder("python", "../scrips/sw.py")
            val process = processBuilder.start()
            val exitCode = process.waitFor()

            if (exitCode == 0) {

                val archivoJson = File("datasw.json")

                val objectMapper = jacksonObjectMapper()
    
                val alquileresRecopilados: List<Producto> = objectMapper.readValue(archivoJson)
                alquilerService.saveAll(alquileresRecopilados)
            } else {
                print("Hubo algun error")
            }
        } catch (e: IOException) {
            e.printStackTrace()
        } catch (e: InterruptedException) {
            e.printStackTrace()
        }
    }

    @DeleteMapping("/eliminar-alquiler")    
    fun eliminarTodosAlquiler() = alquilerService.deleteAll()

    @DeleteMapping("/eliminar-alquiler/{id}")
    fun eliminarAlquiler(@PathVariable id: String) = alquilerService.delete(id)
}