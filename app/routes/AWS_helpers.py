import boto3
import botocore
import os
# Generates unique ids and hashes from python
import uuid

# Our s3 bucket
# Accessing all of our credentials to access AWS
s3 = boto3.client(
    "s3",
    aws_access_key_id=os.environ.get("S3_KEY"),
    aws_secret_access_key=os.environ.get("S3_SECRET")
)

ALLOWED_EXTENSIONS = {"mp3", "mp4", "m4a", "wav"}

# Taking buckname and s3 location from .env
BUCKET_NAME = os.environ.get("S3_BUCKET")
S3_LOCATION = f"http://{BUCKET_NAME}.s3.amazonaws.com/"

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
def remove_file_from_s3(image_url):
    # AWS needs the image file name, not the URL, 
    # so you split that out of the URL
    key = image_url.rsplit("/", 1)[1]
    try:
        s3.delete_object(
        Bucket=BUCKET_NAME,
        Key=key
        )
    except Exception as e:
        return { "errors": str(e) }
    return True

# def remove_audio_file_from_s3(audio_url):
#     # Assuming your audio URL structure is like "s3://BUCKET_NAME/KEY"
#     # You may need to adjust this if your URL structure is different
#     parts = audio_url.split("/")
#     if len(parts) < 4:
#         return {"error": "Invalid audio URL format"}

#     bucket_name = parts[2]
#     key = '/'.join(parts[3:])

#     try:
#         s3.delete_object(
#             Bucket=bucket_name,
#             Key=key
#         )
#         return {"message": f"Audio file '{key}' successfully deleted from S3"}
#     except Exception as e:
#         return {"error": str(e)}

# # Usage example
# audio_url = "s3://YOUR_BUCKET_NAME/path/to/your/audiofile.mp3"
# result = remove_audio_file_from_s3(audio_url)
# print(result)

