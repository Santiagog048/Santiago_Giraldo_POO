import math

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    
    def punto_pertenece(self, punto):
        distancia_al_centro = math.sqrt((punto[0] - self.centro[0]) ** 2 + (punto[1] - self.centro[1]) ** 2)
        return distancia_al_centro <= self.radio

centro = (0, 0)
radio = 5
mi_circulo = Circulo(centro, radio)

print("Área:", mi_circulo.calcular_area())
print("Perímetro:", mi_circulo.calcular_perimetro())

punto = (7, 4)
if mi_circulo.punto_pertenece(punto):
    print("El punto", punto, "pertenece al círculo.")
else:
    print("El punto", punto, "no pertenece al círculo.")