def calcular_suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

numeros_str = input("Ingresa una lista de números separados por espacios: ")
numeros_lista = [int(numero) for numero in numeros_str.split()]

suma_total = calcular_suma_lista(numeros_lista)
print("La suma de los números en la lista es:", suma_total)