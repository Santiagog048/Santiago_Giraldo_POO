class Vehículo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

mi_vehiculo = Vehículo(200, 15000)

print("Velocidad máxima:", mi_vehiculo.velocidad_maxima, "km/h")
print("Kilometraje:", mi_vehiculo.kilometraje, "km")