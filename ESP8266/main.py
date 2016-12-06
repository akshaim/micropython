
from settings import *
import http_client
import machine
import time
import network

machine.freq(160000000)
adc = machine.ADC(0)

def measure():
    light=adc.read()
    time.sleep_ms(1)
    print('Light: ', light) 
    return light


def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(WIFI_SSID, WIFI_KEY)
        while not wlan.isconnected():
            time.sleep(0.1)
    print('network config:', wlan.ifconfig())


def go_sleep():
    time.sleep(20)

	
def post_data(light):
    http_client.post('https://api.thingspeak.com/update?api_key=' + APIKEY + '&field1=' + str(light))
    print('Posted to Thingspeak')	
	
while True:
    (light) = measure()
    post_data(light)
    go_sleep()
