class Carta:
    PINTAS = ('Corazones', 'Diamantes', 'Tréboles', 'Picas')
    
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta
    
    def __str__(self):
        return f"{self.valor} de {self.pinta}"

carta1 = Carta('As', Carta.PINTAS[0])
carta2 = Carta('10', Carta.PINTAS[3])

print(carta1)
print(carta2)