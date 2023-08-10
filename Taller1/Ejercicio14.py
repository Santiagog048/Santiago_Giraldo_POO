def calcular_media_aritmetica(lista):
    suma = sum(lista)
    media = suma / len(lista)
    return media

numeros_str = input("Ingresa una lista de números separados por espacios: ")
numeros_lista = [float(numero) for numero in numeros_str.split()]

media_aritmetica = calcular_media_aritmetica(numeros_lista)
print("La media aritmética es:", media_aritmetica)