import random

def generar_lista_aleatoria(n, min_valor, max_valor):
    lista_aleatoria = [random.randint(min_valor, max_valor) for _ in range(n)]
    return lista_aleatoria

cantidad_numeros = int(input("Ingresa la cantidad de números aleatorios que deseas generar: "))
valor_minimo = int(input("Ingresa el valor mínimo para los números aleatorios: "))
valor_maximo = int(input("Ingresa el valor máximo para los números aleatorios: "))

lista_aleatoria = generar_lista_aleatoria(cantidad_numeros, valor_minimo, valor_maximo)
print("Lista de números aleatorios:", lista_aleatoria)