from time import sleep
from picamera import PiCamera

camera = PiCamera()

def stillshot(path):
    path = path
    camera.start_preview()
    sleep(5)
    camera.capture(path)
    camera.stop_preview()
    return('Image saved to ' +path)
