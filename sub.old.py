from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1
import json
import gcsdata

# TODO(developer)
project_id = "rkiles-home"
subscription_id = "rvstat-test1-sub"
# Number of seconds the subscriber should listen for messages
timeout = 3.0

subscriber = pubsub_v1.SubscriberClient()
# The `subscription_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/subscriptions/{subscription_id}`
subscription_path = subscriber.subscription_path(project_id, subscription_id)

def callback(message):
    global readings
    readings = json.loads(message.data)
    message.ack()


streaming_pull_future = subscriber.subscribe(subscription_path, callback)
print(f"Listening for messages on {subscription_path}..\n")


# Wrap subscriber in a 'with' block to automatically call close() when done.
with subscriber:
    try:
        # When `timeout` is not set, result() will block indefinitely,
        # unless an exception is encountered first.
        streaming_pull_future.result(timeout=timeout)
    except TimeoutError:
        streaming_pull_future.cancel()  # Trigger the shutdown.
        streaming_pull_future.result()  # Block until the shutdown is complete.

if 'readings'in globals():
    temp = readings["temp"]
    humidity = readings["humidity"]
    image = readings["image"]
    print('Temp is '+temp+' and humidity is '+humidity)
    print('Downloading image now')
    imagedown = gcsdata.download_blob('rkiles-home', image, '/home/admin_/wip/image-down.jpg')
else:
    print('No new data found')
    exit()
