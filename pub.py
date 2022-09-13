from google.cloud import pubsub_v1
import json
import sys
#import gcsdata

# TODO(developer)
project_id = "rkiles-home"
topic_id = "rvstat-dev1"

publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_id}`
topic_path = publisher.topic_path(project_id, topic_id)

def publish(temp, humidity, date, time, imageDest):
    temp = temp
    humidity = humidity
    date = date
    time = time
    #image = image
    imageDest = imageDest

    #imageup = gcsdata.upload_blob('rvstat-dev', image, imageDest)

    data = '{"temp":"'+temp+'", "humidity":"'+humidity+'", "date":"'+date+'", "time":"'+time+'", "image":"'+imageDest+'"}'

    message = data.encode("utf-8")
    future = publisher.publish(topic_path, message)
    #print(future.result())

    #print(f"Published messages to {topic_path}.")
