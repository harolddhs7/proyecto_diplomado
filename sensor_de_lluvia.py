#!/usr/bin/python
#encoding:utf-8
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

def lluvia():
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1115(i2c)
    ads.gain = 1
    chan = AnalogIn(ads, ADS.P0)
    return -21.21*chan.voltage+70
    

