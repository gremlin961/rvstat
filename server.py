from flask import Flask
import os
import datetime
from google.cloud import storage
from google.cloud import datastore
import json
import tempfile
import gcsdata


app = Flask(__name__)

IMG_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER


def download_blob(bucket_name, source_file, destination_file):
    """Downloads a blob from the bucket."""
    # The ID of your GCS bucket
    bucket_name = bucket_name
    # The ID of your GCS object
    source_file = source_file
    # The path to which the file should be downloaded
    destination_file = destination_file

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(source_file)
    blob.download_to_filename(destination_file)


@app.route('/')
def hello():
    #now = datetime.datetime.now()
    #time = now.strftime("%H:%M:%S")
    #temp = 72
    #humidity = 42
    client = datastore.Client()
    reading_key = client.key("Reading", "environmental")
    query = client.get(reading_key)
    #print(query['temp'])
    temp = query['temp']
    humidity = query['humidity']
    date = query['date']
    time = query['time']
    image_down = download_blob('rvstat-dev', 'image-up.jpg', './static/images/image.jpg')
    image = os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg')



    PAGE="""\
    <html>
    <head>
    <title>Raspberry Pi - Surveillance Camera</title>
    </head>
    <body>
    <center><h1>Current temperature is {temp} &#8457;</h1></center>
    <center><h1>Current humidity is {humidity} %</h1></center>
    <center><h1>Current time is {time} on {date}%</h1></center>
    <center><img src={image} width="640" height="480"></center>
    </body>
    </html>
    """.format(temp=temp, humidity=humidity, time=time, date=date, image=image)
    return PAGE



# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='0.0.0.0', port=80)
