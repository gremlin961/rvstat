from google.cloud import pubsub_v1
import json
import gcsdata

# TODO(developer)
project_id = "kiles-home"
topic_id = "rvstat-"

publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_id}`
topic_path = publisher.topic_path(project_id, topic_id)

Temp = '70'
Humidity = '40'
Image = '/home/admin_/wip/image.jpg'
ImageDest = 'image-up.jpg'

imageup = gcsdata.upload_blob('rkiles-test', Image, ImageDest)

data = '{"temp":"'+Temp+'", "humidity":"'+Humidity+'", "image":"'+ImageDest+'"}'

message = data.encode("utf-8")
future = publisher.publish(topic_path, message)
print(future.result())


#for n in range(1, 10):
#    data_str = f"Message number {n}"
#    # Data must be a bytestring
#    data = data_str.encode("utf-8")
#    # When you publish a message, the client returns a future.
#    future = publisher.publish(topic_path, data)
#    print(future.result())

print(f"Published messages to {topic_path}.")
