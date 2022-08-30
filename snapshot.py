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

def liveshot(path):
    path = path
    camera.start_preview()
    camera.start_recording(path)
    sleep(5)
    camera.stop_recording()
    camera.stop_preview()
    return('Video saved to ' +path)
