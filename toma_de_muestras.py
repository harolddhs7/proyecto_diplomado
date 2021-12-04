from sensor_de_lluvia import lluvia
from hc_sr04 import distancia
import time

while True:
    fecha = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(fecha + '\nCantidad de lluvia:' +str(lluvia())+' mm/h\n'+ 'Nivel del rio' + str(distancia())+' cm\n')
