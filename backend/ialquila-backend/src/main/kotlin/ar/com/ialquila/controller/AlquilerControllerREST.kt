package ar.com.ialquila.controller

import ar.com.ialquila.controller.dto.AlquilerDTO
import ar.com.ialquila.dao.AlquilerDAO
import ar.com.ialquila.model.Alquiler
import ar.com.ialquila.service.AlquilerService
import org.springframework.web.bind.annotation.CrossOrigin
import org.springframework.web.bind.annotation.DeleteMapping
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PathVariable
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.PutMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController

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

    @GetMapping("/alquiler/{id}")
    fun obtenerAlquiler(@PathVariable id: String) = AlquilerDTO.desdeModeloAJson(alquilerService.getById(id))

    @PutMapping("/actualizar-alquiler/{id}")
    fun actualizarAlquiler(@RequestBody alquiler: AlquilerDTO, @PathVariable id: String) {
        val alquilerAActualizar = alquilerService.getById(id)
        alquilerAActualizar.titulo = alquiler.titulo
        alquilerAActualizar.descripcion = alquiler.descripcion
        alquilerAActualizar.img         = alquiler.img
        alquilerAActualizar.precio      = alquiler.precio
        alquilerAActualizar.ubicacion   = alquiler.ubicacion
        alquilerService.update(alquilerAActualizar)
    }

    @DeleteMapping("/eliminar-alquiler")
    fun eliminarTodosAlquiler() = alquilerService.deleteAll()

    @DeleteMapping("/eliminar-alquiler/{id}")
    fun eliminarAlquiler(@PathVariable id: String) = alquilerService.delete(id)
}