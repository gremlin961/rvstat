import board
import adafruit_dht

def get():
    dhtDevice1 = adafruit_dht.DHT22(board.D4, use_pulseio=False)
    temperature_f = dhtDevice1.temperature * 1.8 + 32
    humidity = dhtDevice1.humidity

    return temperature_f
    return humidity
