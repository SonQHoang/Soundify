from flask import send_file, jsonify
import boto3
import botocore
import os
# Generates unique ids and hashes from python
import uuid


ALLOWED_EXTENSIONS = {"mp3", "mp4", "m4a", "wav"}

# Taking buckname and s3 location from .env
BUCKET_NAME = os.environ.get("S3_BUCKET")
S3_LOCATION = f"http://{BUCKET_NAME}.s3.amazonaws.com/"

# Our s3 bucket
# Accessing all of our credentials to access AWS
s3 = boto3.client(
    "s3",
    aws_access_key_id=os.environ.get("S3_KEY"),
    aws_secret_access_key=os.environ.get("S3_SECRET")
)

def get_unique_filename(filename):
    # Split by the extension
    ext = filename.rsplit(".", 1)[1].lower()
    # Create a unique hash
    unique_filename = uuid.uuid4().hex
    # Put it all back together
    return f"{unique_filename}.{ext}"

# "public-read" lets us access our items from sites not related to AWS

##!! Use this for post and create, and possibly UPDATE
def upload_file_to_s3(file, acl="public-read"):
    try:
        s3.upload_fileobj(
            file,
            BUCKET_NAME,
            file.filename,
            # Extra args to help us connect to the bucket?
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )
    except Exception as e:
        # in case the your s3 upload fails
        return {"errors": str(e)}

    return {"url": f"{S3_LOCATION}{file.filename}"}

# If I want to do an audio file, what would I change this to?

##! Use this for delete routes
def remove_file_from_s3(audio_url):
    # AWS needs the audio file name, not the URL, 
    # so you split that out of the URL
    parts = audio_url.rsplit("/")

    key = parts[-1]

    try:
        s3.delete_object(
        Bucket=BUCKET_NAME,
        Key=key
        )
        return {"message": f"Audio file '{key}' successfully deleted from S3"}
    except Exception as e:
        return {"error": str(e)}

# AWS downloader 
bucket_name = os.environ.get("S3_BUCKET")

# Function to list all objects in the bucket
def list_objects_in_bucket(bucket_name):
    objects = []
    continuation_token = None

    while True:
        list_kwargs = {'Bucket': bucket_name}
        if continuation_token:
            list_kwargs['ContinuationToken'] = continuation_token

        response = s3.list_objects_v2(**list_kwargs)

        # Add the objects from the current page to the list
        objects.extend(response.get('Contents', []))

        # Check if there are more pages
        if 'NextContinuationToken' in response:
            continuation_token = response['NextContinuationToken']
        else:
            break

    return objects
