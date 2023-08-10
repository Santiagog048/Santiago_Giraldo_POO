import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mostrar(self):
        print("Coordenadas del punto: ({}, {})".format(self.x, self.y))
    
    def mover(self, nueva_x, nueva_y):
        self.x = nueva_x
        self.y = nueva_y
    
    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)
        return distancia

punto1 = Punto(3, 5)
punto2 = Punto(7, 2)

punto1.mostrar()
punto2.mostrar()

punto1.mover(8, 10)
punto1.mostrar()

distancia = punto1.calcular_distancia(punto2)
print("Distancia entre los puntos:", distancia)