import board
import adafruit_dht

def get(device):
    # "device" references the GPIO port or remote device passed to the module from the calling script
    dhtDevice = adafruit_dht.DHT22(board. +device, use_pulseio=False)
    temperature_f = dhtDevice.temperature * 1.8 + 32
    humidity = dhtDevice.humidity
    print(
        "Temp: {:.1f} F / Humidity: {}% ".format(
            temperature_f, humidity
        )
    )
