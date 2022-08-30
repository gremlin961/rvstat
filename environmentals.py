import board
import adafruit_dht

dhtDevice1 = adafruit_dht.DHT22(board.D4, use_pulseio=False)

def temp():
    temp = dhtDevice1.temperature * 1.8 + 32
    return temp


def humidity():
    humidity = dhtDevice1.humidity
    return humidity
