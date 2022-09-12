from google.cloud import storage

def upload_blob(bucket_name, source_file, destination_file):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    bucket_name = bucket_name
    # The path to your file to upload
    source_file = source_file
    # The ID of your GCS object
    destination_file = destination_file

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_file)

    blob.upload_from_filename(source_file)

    print(
        f"File {source_file} uploaded to {destination_file}."
    )


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

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    blob = bucket.blob(source_file)
    blob.download_to_filename(destination_file)
