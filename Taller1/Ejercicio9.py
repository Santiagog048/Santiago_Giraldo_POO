def generar_matriz(filas, columnas):
    matriz = [[0] * columnas for _ in range(filas)]
    numero = 1
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = numero
            numero += 1
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()

filas = int(input("Ingresa el número de filas: "))
columnas = int(input("Ingresa el número de columnas: "))

matriz_generada = generar_matriz(filas, columnas)
print("Matriz generada:")
imprimir_matriz(matriz_generada)