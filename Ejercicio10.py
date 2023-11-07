from abc import ABC, abstractmethod

class LongitudInvalidaError(Exception):
    pass

class FaltaMayusculaError(Exception):
    pass

class FaltaMinusculaError(Exception):
    pass

class FaltaNumeroError(Exception):
    pass

class FaltaCaracterEspecialError(Exception):
    pass

class FaltaCalistoError(Exception):
    pass

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave):
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave):
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave):
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave):
        return any(c.isdigit() for c in clave)

    @abstractmethod
    def es_valida(self, clave):
        pass

class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(8)

    def _contiene_caracter_especial(self, clave):
        return any(c in "@_#$%" for c in clave)

    def es_valida(self, clave):
        if not self._validar_longitud(clave):
            raise LongitudInvalidaError()
        if not self._contiene_mayuscula(clave):
            raise FaltaMayusculaError()
        if not self._contiene_minuscula(clave):
            raise FaltaMinusculaError()
        if not self._contiene_numero(clave):
            raise FaltaNumeroError()
        if not self._contiene_caracter_especial(clave):
            raise FaltaCaracterEspecialError()
        return True

class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(6)

    def _contiene_calisto(self, clave):
        return clave.upper().count("CALISTO") >= 2

    def es_valida(self, clave):
        if not self._validar_longitud(clave):
            raise LongitudInvalidaError()
        if not self._contiene_numero(clave):
            raise FaltaNumeroError()
        if not self._contiene_calisto(clave):
            raise FaltaCalistoError()
        return True

class Validador:
    def __init__(self, regla):
        self.regla = regla

    def es_valida(self, clave):
        try:
            return self.regla.es_valida(clave)
        except Exception as e:
            return False

# Ejemplo de Implementacion Codigo
regla_ganimedes = ReglaValidacionGanimedes()
regla_calisto = ReglaValidacionCalisto()

validador_ganimedes = Validador(regla_ganimedes)
validador_calisto = Validador(regla_calisto)

clave = "P@ssw0rd"

if validador_ganimedes.es_valida(clave):
    print("La clave cumple con la regla de Validación Ganímedes.")
else:
    print("La clave no cumple con la regla de Validación Ganímedes.")

if validador_calisto.es_valida(clave):
    print("La clave cumple con la regla de Validación Calisto.")
else:
    print("La clave no cumple con la regla de Validación Calisto.")