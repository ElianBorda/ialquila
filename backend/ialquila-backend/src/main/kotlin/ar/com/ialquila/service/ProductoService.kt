package ar.com.ialquila.service

import ar.com.ialquila.model.Producto

interface ProductoService {

    fun save(producto: Producto): Producto
    fun saveAll(alquileres: List<Producto>)
    fun update(producto: Producto): Producto
    fun getAll(): List<Producto>
    fun getAllPageale(numPag: Int): List<Producto>
    fun getById(id: String): Producto
    fun getAmount(): Long
    fun delete(id: String)
    fun deleteAll()
}