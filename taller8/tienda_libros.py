from libro import Libro
from carro_compra import CarroCompras
from item_compra import ItemCompra
from libro_error import LibroError
from libro_existente_error import LibroExistenteError
from libro_agotado_error import LibroAgotadoError
from existencias_insuficientes_error import ExistenciasInsuficientesError



class TiendaLibros:
    def __init__(self):
        self.catalogo = {}
        self.carrito = CarroCompras()

    def adicionar_libro_a_catalogo(self, isbn, titulo, precio, existencias):
        if isbn in self.catalogo:
            raise LibroExistenteError(titulo, isbn)
        libro = Libro(isbn, titulo, precio, existencias)
        self.catalogo[isbn] = libro
        return libro

    def agregar_libro_a_carrito(self, isbn, cantidad):
        if isbn not in self.catalogo:
            raise LibroError(f"El libro con ISBN {isbn} no existe en el catálogo")
        libro = self.catalogo[isbn]
        if libro.existencias == 0:
            raise LibroAgotadoError(libro.titulo, isbn)
        if cantidad > libro.existencias:
            raise ExistenciasInsuficientesError(libro.titulo, isbn, cantidad, libro.existencias)
        self.carrito.agregar_item(libro, cantidad)
        libro.existencias -= cantidad

    def retirar_item_de_carrito(self, isbn):
        self.carrito.quitar_item(isbn)

