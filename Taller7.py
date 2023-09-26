from dataclasses import dataclass

@dataclass
class Item:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Item):
            return self.nombre == other.nombre
        return False

class Set:
    contador = 0

    def __init__(self, nombre):
        self.items = []
        self.nombre = nombre
        Set.contador += 1
        self.__id = Set.contador

    @property
    def id(self):
        return self.__id

    def contiene_item(self, item):
        return any(item == i for i in self.items)

    def agregar_item(self, item):
        if not self.contiene_item(item):
            self.items.append(item)

    def unir_sets(self, otro_set):
        nuevo_set = Set(f"{self.nombre} UNIDO {otro_set.nombre}")
        for item in self.items:
            nuevo_set.agregar_item(item)
        for item in otro_set.items:
            nuevo_set.agregar_item(item)
        return nuevo_set

    @classmethod
    def interseccion(cls, set1, set2):
        nombre_resultado = f"{set1.nombre} INTERSECTADO {set2.nombre}"
        items_comunes = [item for item in set1.items if set2.contiene_item(item)]
        nuevo_set = Set(nombre_resultado)
        nuevo_set.items = items_comunes
        return nuevo_set

    def __str__(self):
        items_str = ', '.join([item.nombre for item in self.items])
        return f"Set {self.nombre}: ({items_str})"

item1 = Item("A")
item2 = Item("B")
item3 = Item("C")

set1 = Set("Set A")
set1.agregar_item(item1)
set1.agregar_item(item2)

set2 = Set("Set B")
set2.agregar_item(item2)
set2.agregar_item(item3)

print(set1)
print(set2)
print(set1.unir_sets(set2))

interseccion = Set.interseccion(set1, set2)
print(interseccion)