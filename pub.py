from google.cloud import pubsub_v1
import json
import sys
import os
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
    print(data)
    message = data.encode("utf-8")
    future = publisher.publish(topic_path, message)
    print(future.result())

    #print(f"Published messages to {topic_path}.")
if __name__ == "__main__":
    exvar1 = sys.argv[1]
    exvar2 = sys.argv[2]
    exvar3 = sys.argv[3]
    exvar4 = sys.argv[4]
    exvar5 = sys.argv[5]
    path = '/app/output.log'
    sys.stdout = open(path, 'w')
    print('Message is: publish('+exvar1+', '+exvar2+', '+exvar3+', '+exvar4+', '+exvar5+')')
    sendmessage = publish(exvar1, exvar2, exvar3, exvar4, exvar5)
    print('message sent')

    print(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
