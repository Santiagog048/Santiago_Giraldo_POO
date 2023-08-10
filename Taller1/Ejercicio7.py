def encontrar_maximo_minimo(lista):
    maximo = lista[0]
    minimo = lista[0]
    
    for numero in lista:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero
    
    return maximo, minimo

numeros_str = input("Ingresa una lista de números separados por espacios: ")
numeros_lista = [int(numero) for numero in numeros_str.split()]

maximo, minimo = encontrar_maximo_minimo(numeros_lista)
print("El número más grande es:", maximo)
print("El número más pequeño es:", minimo)