import time
import environmentals
import snapshot
import pubtopic

Temp = environmentals.temp()
Humidity = environmentals.humidity()
image = snapshot.stillshot('/home/rkiles/image.jpg')
#video = snapshot.liveshot('/home/rkiles/video.h264')

message = pubtopic.send(Temp,Humidity)
