import time
import board
import adafruit_dht
from picamera import picamera

# Initialize the DHT device, identify which GPIO port it's using (D4 in this case) and disable pulseIO
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

# Create a loop to pole for the temperature and humidity level
while True:
    try:
        # Format the temperature to ferenhite and print the values to the serial port
        temperature_f = dhtDevice.temperature * 1.8 + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} F / Humidity: {}% ".format(
                temperature_f, humidity
            )
        )

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    except KeyboardInterrupt:
        dhtDevice.exit()
        print('exiting script')
    time.sleep(2.0)
