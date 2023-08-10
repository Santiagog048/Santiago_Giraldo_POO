import math

def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area

radio = float(input("Ingresa el radio del círculo: "))

area = calcular_area_circulo(radio)
print("El área del círculo es:", area)