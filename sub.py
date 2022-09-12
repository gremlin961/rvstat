from google.cloud import datastore
import base64
import json


def run(event, context):
  """Triggered from a message on a Cloud Pub/Sub topic.
  Args:
       event (dict): Event payload.
       context (google.cloud.functions.Context): Metadata for the event.
  """
  pubsub_message = base64.b64decode(event['data']).decode('utf-8')
  data = json.loads(pubsub_message)
  temp = data["temp"]
  humidity = data["humidity"]
  date = data["date"]
  time = data["time"]
  image = data["image"]
  #print("data from pubsub = "+temp+" "+humidity+" "+date+" "+time+" "+image+" ")

  client = datastore.Client()

  reading_key = client.key("Reading", "environmental")

  reading = datastore.Entity(key=reading_key)
  print("Starting delivery to Datastore")

  reading.update(
      {
          "temp": temp,
          "humidity": humidity,
          "time": time,
          "date": date,
          "image": image
      }
  )

  client.put(reading)
  print("Message delivery comlete")
