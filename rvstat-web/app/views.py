from app import app
import os
from google.cloud import storage
from google.cloud import datastore
import tempfile
from flask import render_template

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
def home():
    client = datastore.Client()
    reading_key = client.key("Reading", "environmental")
    query = client.get(reading_key)
    temp = query['temp']
    humidity = query['humidity']
    date = query['date']
    time = query['time']
    image_down = download_blob('rvstat-dev', 'image-up.jpg', '/var/www/app/static/images/image.jpg')
    image = os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg')

    return render_template('home.html', temp=temp, humidity=humidity, date=date, time=time, image=image)
