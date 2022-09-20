import time
import environmentals
import snapshot
#import pub
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

pubdata = temp+' '+humidity+' '+date+' '+time+' '+imageDest

docker_client = docker.from_env()
docker_client.containers.run("pub", "python3 /app/pub.py "+pubdata, environment=['GOOGLE_APPLICATION_CREDENTIALS=/keys/rkiles-home-707f0b035f73.json'], volumes=['/keys:/keys','/home/rkiles/git/rvtemp:/app'])
#message = pub.publish(temp, humidity, date, time, imageDest)
