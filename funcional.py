import paho.mqtt.client as mqtt
import time
import random
import RPi.GPIO as GPIO
from sensor_de_lluvia import lluvia
from hc_sr04 import distancia

broker = 'industrial.api.ubidots.com'
port =  1883
topic = '/v1.6/devices/raspberry'
client_id = "raspberry"
username = "BBFF-tkacYesQ8o99q4XEOBfzOPKD5nhtg9"
password = ''

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

time.sleep(1)
GPIO.output(5, True)
GPIO.output(6, True)
GPIO.output(16, True)
GPIO.output(20, True)
GPIO.output(21, True)
time.sleep(1)

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

        if nivel_1 < 10:
            GPIO.output(5, False)
            GPIO.output(6, False)
            time.sleep(10)
            GPIO.output(5, True)
            GPIO.output(6, True)
            time.sleep(1)

        if lluvia_1 >30:
            GPIO.output(16, False)
            time.sleep(10)
            GPIO.output(16, True)
            time.sleep(1)

        if lluvia_1 < 31 and lluvia_1 > 15:
            GPIO.output(20, False)
            time.sleep(10)
            GPIO.output(20, True)
            time.sleep(1)

        if lluvia_1 < 16:
            GPIO.output(21, False)
            time.sleep(10)
            GPIO.output(21, True)
            time.sleep(1) 

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
