def invertir_lista(lista):
    lista_invertida = lista[::-1]
    return lista_invertida

elementos_str = input("Ingresa una lista de elementos separados por espacios: ")
elementos_lista = elementos_str.split()

lista_invertida = invertir_lista(elementos_lista)
print("Lista invertida:", lista_invertida)