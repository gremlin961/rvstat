import time
import environmentals
import snapshot
import pub
import gcsdata
import docker

temp = environmentals.temp()
humidity = environmentals.humidity()
date = environmentals.date()
time = environmentals.time()
image = snapshot.stillshot('/home/rkiles/image.jpg')
imageDest = 'image-up.jpg'
#video = snapshot.liveshot('/home/rkiles/video.h264')

imageup = gcsdata.upload_blob('rvstat-dev', image, imageDest)

docker_client = docker.from_env()
docker_client.containers.run("pub", "")
#message = pub.publish(temp, humidity, date, time, imageDest)
