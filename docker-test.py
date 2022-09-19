import time
import environmentals
import snapshot
import pub
import gcsdata
import docker


docker_client = docker.from_env()

docker_client.containers.run("pub", "python3 /app/test.py test1 test2", volumes=['/keys:/keys','/home/rkiles/git/rvtemp:/app'])
#message = pub.publish(temp, humidity, date, time, imageDest)
