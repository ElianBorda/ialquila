package ar.com.ialquila.service

import ar.com.ialquila.model.Producto
import java.awt.print.Pageable

interface ProductoService {
    fun save(producto: Producto): Producto
    fun saveAll(alquileres: List<Producto>)
    fun update(producto: Producto): Producto
    fun getAll(): List<Producto>
    fun getProductos(residencia: String?, compra: String?, ord: Int?, ubiencode: String?,numPag: Int): List<Producto>
    fun getById(id: String): Producto
    fun getAmount(): Long
    fun delete(id: String)
    fun deleteAll()
}