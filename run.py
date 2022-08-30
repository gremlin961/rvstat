import time
import environmentals
import snapshot

Temp = environmentals.temp()
Humidity = environmentals.humidity()

print(Temp)
print(Humidity)

image = snapshot.stillshot('/home/rkiles/image.jpg')
video = snapshot.liveshot('/home/rkiles/video.h264')
