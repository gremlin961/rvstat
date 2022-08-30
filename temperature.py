import board
import adafruit_dht

dhtDevice1 = adafruit_dht.DHT22(board.D4, use_pulseio=False)

def temp():
    temperature_f = dhtDevice1.temperature * 1.8 + 32
    return temperature_f

def humidity():
    humidity = dhtDevice1.humidity
    return humidity
