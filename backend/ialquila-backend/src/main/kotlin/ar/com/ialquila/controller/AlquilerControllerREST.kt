package ar.com.ialquila.controller

import ar.com.ialquila.controller.dto.AlquilerDTO
import ar.com.ialquila.dao.AlquilerDAO
import ar.com.ialquila.model.Alquiler
import ar.com.ialquila.service.AlquilerService
import org.springframework.web.bind.annotation.CrossOrigin
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController

@RestController
@CrossOrigin
@RequestMapping("/home")
class AlquilerControllerREST(private val alquilerService: AlquilerService) {

    @GetMapping("/alquileres")
    fun todosLosAlquileres() = alquilerService.getAll().map { alquiler -> AlquilerDTO.desdeModeloAJson(alquiler)  }

    @PostMapping("/guardar-alquiler")
    fun guardarAlquiler(@RequestBody alquiler: AlquilerDTO) = alquilerService.save(alquiler.desdeJsonAModelo())
}