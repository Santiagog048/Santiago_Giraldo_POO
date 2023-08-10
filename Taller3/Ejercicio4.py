class Rectángulo:
    def __init__(self, esquina_superior_izquierda, esquina_inferior_derecha):
        self.esquina_superior_izquierda = esquina_superior_izquierda
        self.esquina_inferior_derecha = esquina_inferior_derecha
    
    def calcular_perímetro(self):
        ancho = abs(self.esquina_inferior_derecha[0] - self.esquina_superior_izquierda[0])
        alto = abs(self.esquina_inferior_derecha[1] - self.esquina_superior_izquierda[1])
        return 2 * (ancho + alto)
    
    def calcular_área(self):
        ancho = abs(self.esquina_inferior_derecha[0] - self.esquina_superior_izquierda[0])
        alto = abs(self.esquina_inferior_derecha[1] - self.esquina_superior_izquierda[1])
        return ancho * alto
    
    def es_cuadrado(self):
        ancho = abs(self.esquina_inferior_derecha[0] - self.esquina_superior_izquierda[0])
        alto = abs(self.esquina_inferior_derecha[1] - self.esquina_superior_izquierda[1])
        return ancho == alto

esquina_sup_izq = (1, 3)
esquina_inf_der = (5, 1)
mi_rectángulo = Rectángulo(esquina_sup_izq, esquina_inf_der)

print("Perímetro:", mi_rectángulo.calcular_perímetro())
print("Área:", mi_rectángulo.calcular_área())
if mi_rectángulo.es_cuadrado():
    print("Es un cuadrado.")
else:
    print("No es un cuadrado.")