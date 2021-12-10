import paho.mqtt.client as mqtt
import time
import random
from sensor_de_lluvia import lluvia
from hc_sr04 import distancia

broker = 'industrial.api.ubidots.com'
port =  1883
topic = '/v1.6/devices/raspberry'
client_id = "raspberry"
username = "BBFF-tkacYesQ8o99q4XEOBfzOPKD5nhtg9"
password = ''

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Conectado al broker mqtt')
        else:
            print('Fallo al conectar, error: %d', rc)
    client = mqtt.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    while True:
        time.sleep(1)
        nivel_1 = distancia()
        lluvia_1 = lluvia()
	
        mensaje = "{\"nivel\":"+ str(nivel_1)+", \"lluvia\":"+ str(lluvia_1)+"}"
        print(mensaje)
	
        result = client.publish(topic, mensaje)
	
        status = result[0]
        if status == 0:
            print('send')
        else:
            prinf('fail')

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()
