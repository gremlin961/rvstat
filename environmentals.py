import board
import adafruit_dht
import datetime


dhtDevice1 = adafruit_dht.DHT22(board.D4, use_pulseio=False)

def temp():
    temp = dhtDevice1.temperature * 1.8 + 32
    return temp


def humidity():
    humidity = dhtDevice1.humidity
    return humidity

def date():
    now = datetime.datetime.now()
    date = now.strftime("%d-%m-%Y")
    return date

def time():
    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")
    return time
