import time
import environmentals
import snapshot
import pub

temp = environmentals.temp()
humidity = environmentals.humidity()
date = environmentals.date()
time = environmentals.time()
image = snapshot.stillshot('/home/rkiles/image.jpg')
#video = snapshot.liveshot('/home/rkiles/video.h264')

message = pub.publish(temp, humidity, date, time, image)
