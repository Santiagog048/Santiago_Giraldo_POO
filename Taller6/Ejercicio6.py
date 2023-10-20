import random

def nueva_carta():
    num = random.randint(1, 13)
    palo = random.choice(['CORAZÓN', 'TRÉBOL', 'DIAMANTE', 'ESPADA'])
    if num == 1:
        num = 11
    elif num == 12:
        num = 10
    elif num == 13:
        num = 10
    return palo, num

def mostrar_carta(carta):
    palo, num = carta
    return f"{palo} {num}"

def suma_mano(mano):
    suma = sum([num for palo, num in mano])
    for palo, num in mano:
        if num == 11 and suma + 10 <= 21:
            suma += 10
            break
    return suma

def crear_baraja():
    baraja = [(palo, num) for palo in ['CORAZÓN', 'TRÉBOL', 'DIAMANTE', 'ESPADA'] for num in range(1, 14)]
    random.shuffle(baraja)
    return baraja

def main():
    jugador = input("Ingrese su nombre: ")
    jugador_dinero = 100
    while True:
        if jugador_dinero == 0:
            print("No tiene más dinero para apostar. Adiós!")
            break
        apuesta = int(input(f"{jugador}, cuántas fichas desea apostar (máximo {jugador_dinero} fichas)? "))
        if apuesta <= 0 or apuesta > jugador_dinero:
            print("Apuesta inválida. Intente de nuevo.")
            continue
        jugador_dinero -= apuesta
        baraja = crear_baraja()
        jugador_mano = [baraja.pop() for _ in range(2)]
        casa_mano = [baraja.pop() for _ in range(2)]
        print(f"{jugador}, su mano: {', '.join(mostrar_carta(carta) for carta in jugador_mano)}")
        print(f"{jugador}, el valor de su mano es: {suma_mano(jugador_mano)}")
        if suma_mano(jugador_mano) == 21:
            print("¡Ha ganado al hacer blackjack!")
            jugador_dinero += 2 * apuesta
        else:
            while True:
                decision = input(f"{jugador}, ¿desea pedir otra carta ((Si)--> s / n <--(No))? ")
                if decision.lower() == 's':
                    jugador_mano.append(baraja.pop())
                    print(f"{jugador}, su mano ahora es: {', '.join(mostrar_carta(carta) for carta in jugador_mano)}")
                    print(f"{jugador}, el valor de su mano es: {suma_mano(jugador_mano)}")
                    if suma_mano(jugador_mano) > 21:
                        print("Ha perdido.")
                        break
                elif decision.lower() == 'n':
                    print(f"{jugador}, el valor de su mano es: {suma_mano(jugador_mano)}")
                    break
                else:
                    print("Respuesta inválida. Intente de nuevo.")
        
        if suma_mano(casa_mano) < 17:
            while suma_mano(casa_mano) < 17:
                casa_mano.append(baraja.pop())
                print(f"La mano de la casa ahora es: {', '.join(mostrar_carta(carta) for carta in casa_mano)}")
                print(f"El valor de la mano de la casa es: {suma_mano(casa_mano)}")
        else:
            print(f"La mano de la casa ahora es: {', '.join(mostrar_carta(carta) for carta in casa_mano)}")
            print(f"El valor de la mano de la casa es: {suma_mano(casa_mano)}")
        
        if suma_mano(jugador_mano) > 21:
            print("Ha perdido.")
        elif suma_mano(casa_mano) > 21:
            print("Ha ganado.")
            jugador_dinero += 2 * apuesta
        elif suma_mano(jugador_mano) == suma_mano(casa_mano):
            print("Ha empatado.")
        elif suma_mano(jugador_mano) > suma_mano(casa_mano):
            print("Ha ganado.")
            jugador_dinero += 2 * apuesta
        else:
            print("Ha perdido.")
        
        print(f"{jugador}, su dinero actual es: {jugador_dinero} fichas")
        decision = input(f"{jugador}, ¿desea seguir jugando ((Si)--> s / n <--(No))? ")
        if decision.lower() == 'n':
            print("Hasta la proxima")
            break

if __name__ == "__main__":
    main()