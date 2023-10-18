from libro_error import LibroError

class LibroExistenteError(LibroError):
    def __init__(self, titulo, isbn):
        super().__init__()
        self.titulo = titulo
        self.isbn = isbn

    def __str__(self):
        return f"El libro con título '{self.titulo}' y ISBN {self.isbn} ya existe en el catálogo"

