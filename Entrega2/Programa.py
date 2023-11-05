from dataclasses import dataclass


@dataclass
class Cliente:
    cedula: int
    nombre: str
    direccion: str
    telefono: int
    compras: int
    estado: int


class Videojuego:
    nombre_juego: str
    codigo_juego: int
    precio_alquiler: int
    precio_venta: int
    cantidad: int

    def vender(self, codigo_juego: int, cedula: int):
        for juego in self.catalogo.values():
            if juego.codigo_juego == codigo_juego:
                for cliente in self.listaclientes.values():
                    if cliente.cedula == cedula:
                        Videojuego.cantidad -= 1

    def alquilar(self, nombre_juego: str, cedula: int):
        for juego in self.catalogo.values():
            if juego.nombre_juego == nombre_juego:
                for cliente in self.listaclientes.values():
                    if cliente.cedula == cedula:
                        cliente.estado = 1
                        Videojuego.cantidad -= 1


class Tienda:

    def __init__(self):
        self.listaclientes: dict[str, Cliente] = dict()
        self.cat: dict[str, Videojuego] = dict()

    # noinspection PyTypeChecker
    def registrar_cliente(self, cedula: int, nombre: str, direccion: str, telefono: int, compras: int,
                          estado: int):
        if self.buscar_cliente(cedula) is None:
            cliente: Cliente = Cliente(cedula, nombre, direccion, telefono, compras, estado)
            self.listaclientes[cedula] = cliente

    # noinspection PyTypeChecker
    def buscar_cliente(self, cedula: int):
        if cedula in self.listaclientes.keys():
            return self.listaclientes[cedula]
        else:
            return None

    def registrar_juego(self, nombre_juego: str, codigo_juego: int, precio_alquiler: int, precio_venta: int,
                        cantidad: int):
        if self.buscar_juego_por_codigo(codigo_juego) is None:
            juego: Videojuego = Videojuego(nombre_juego, codigo_juego, precio_alquiler, precio + venta, cantidad)
            self.catalogo[codigo_juego] = juego

    def buscar_juego_por_nombre(self, nombre_juego: str):
        for juego in self.catalogo.values():
            if juego.nombre_juego == nombre_juego:
                return juego
        return None

    def buscar_juego_por_codigo(self, codigo_juego: int):
        for juego in self.catalogo.values():
            if juego.codigo_juego == codigo_juego:
                return juego
        return None

    def devolver_videojuego(self, cedula: int):
        for cliente in self.listaclientes.values():
            if cliente.cedula == cedula:
                if cliente.estado == 1:
                    self.registrar_juego()
                elif cliente.estado == 0:
                    print("NO TIENES JUEGOS ALQUILADOS")

    def comprar_juego_al_cliente(self, cedula: int):
        for cliente in self.listaclientes.values():
            if cliente.cedula == cedula:
                self.registrar_juego()
            else:
                self.registrar_cliente()
                self.registrar_juego()