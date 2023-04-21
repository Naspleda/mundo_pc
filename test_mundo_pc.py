from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

monitor1 = Monitor("LG", "Grande")
teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
computadora1 = Computadora("HP", monitor1, teclado1, raton1)
print(computadora1)

monitor2 = Monitor("Samsung", "Chico")
teclado2 = Teclado('Acer', 'Bluetooth')
raton2 = Raton('Acer', 'Bluetooth')
computadora2 = Computadora('Acer', monitor2, teclado2, raton2)
print(computadora2)
