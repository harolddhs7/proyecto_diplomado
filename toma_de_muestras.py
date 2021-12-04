from sensor_de_lluvia import lluvia
from hc_sr04 import distancia
import time

while True:
    print(str(lluvia())+' mm/h')
    print(str(distancia())+' cm')
