from datos_meteorologicos import DatosMeteorologicos

def main():
    nombre_archivo = "datos_meteorologicos.txt"

    try:
        datos_clima = DatosMeteorologicos(nombre_archivo)
        resultado = datos_clima.procesar_datos()

        temperatura_promedio, humedad_promedio, presion_promedio, direccion_predominante = resultado

        print(f"Temperatura promedio: {temperatura_promedio:.2f}°C")
        print(f"Humedad promedio: {humedad_promedio:.2f}%")
        print(f"Presión promedio: {presion_promedio:.2f} hPa")
        print(f"Dirección predominante del viento: {direccion_predominante}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main":
    main()