def es_palindromo(cadena):
    cadena = cadena.lower() 
    cadena = cadena.replace(" ", "") 
    return cadena == cadena[::-1]

cadena = input("Ingresa una cadena de texto: ")

if es_palindromo(cadena):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")