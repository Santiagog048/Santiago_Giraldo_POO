class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo
        self.datos = []

    def procesar_datos(self):
        try:
            with open(self.nombre_archivo, 'r') as archivo:
                estaciones = archivo.read().strip().split('\n\n')

            for estacion in estaciones:
                datos_estacion = estacion.strip().split('\n')
                estacion_dict = {}

                for dato in datos_estacion:
                    clave, valor = dato.split(': ')
                    if clave == 'Viento':
                        velocidad, direccion = valor.split(',')
                        estacion_dict['Velocidad_viento'] = float(velocidad)
                        estacion_dict['Direccion_viento'] = direccion
                    else:
                        estacion_dict[clave] = valor

                self.datos.append(estacion_dict)

            if not self.datos:
                raise ValueError("No se encontraron datos en el archivo.")

            temperatura_promedio = sum(float(estacion['Temperatura']) for estacion in self.datos) / len(self.datos)
            humedad_promedio = sum(float(estacion['Humedad']) for estacion in self.datos) / len(self.datos)
            presion_promedio = sum(float(estacion['Presion']) for estacion in self.datos) / len(self.datos)

            direcciones = [estacion['Direccion_viento'] for estacion in self.datos]
            direccion_predominante = max(set(direcciones), key=direcciones.count)

            return temperatura_promedio, humedad_promedio, presion_promedio, direccion_predominante

        except FileNotFoundError:
            raise FileNotFoundError("El archivo no se encuentra en el directorio especificado.")
        except Exception as e:
            raise Exception(f"Error al procesar los datos: {str(e)}")