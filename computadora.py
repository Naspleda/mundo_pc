from mundo_pc.monitor import Monitor
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado


class Computadora:

    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        ID: {self._id}
        Nombre: {self._nombre}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
'''


if __name__ == "__main__":
    monitor1 = Monitor("HP", 15)
    teclado1 = Teclado("HP", "USB")
    raton1 = Raton("HP", "USB")
    computadora1 = Computadora("MC", monitor1, teclado1, raton1)
    print(computadora1)
