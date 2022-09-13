# This image will execute the pub.py python script. This needs to run inside
# a contianer due to conflicts with other python modules on Raspbian OS.

FROM ubuntu:latest
RUN apt-get update && apt-get upgrade -y && apt-get install -y python3-pip
RUN pip install google-cloud-pubsub
