import board
import adafruit_dht

def get():
    dhtDevice1 = adafruit_dht.DHT22(board.D4, use_pulseio=False)
    return temperature_f = dhtDevice1.temperature * 1.8 + 32
    return humidity = dhtDevice1.humidity
