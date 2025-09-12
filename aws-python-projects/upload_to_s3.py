# import boto3
# import os
# from dotenv import load_dotenv

# # Load .env file
# load_dotenv()

# # Get credentials
# AWS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
# AWS_SECRET = os.getenv("AWS_SECRET_ACCESS_KEY")
# REGION = os.getenv("AWS_DEFAULT_REGION")

# # Create boto3 session
# session = boto3.Session(
#     aws_access_key_id=AWS_KEY,
#     aws_secret_access_key=AWS_SECRET,
#     region_name=REGION
# )

# # Create S3 resource
# s3 = session.resource('s3')

# # Bucket name (must be created first in AWS Console)
# bucket_name = "anii-cloud-bucket"  # change if needed

# # Upload file
# file_name = "sample.txt"
# object_name = "uploads/sample.txt"

# try:
#     s3.Bucket(bucket_name).upload_file(file_name, object_name)
#     print(f"✅ File '{file_name}' uploaded to '{bucket_name}/{object_name}'")
# except Exception as e:
#     print(f"❌ Upload failed: {e}")


import boto3
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

AWS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET = os.getenv("AWS_SECRET_ACCESS_KEY")
REGION = os.getenv("AWS_DEFAULT_REGION")
BUCKET_NAME = "anii-cloud-bucket"   # ✅ Update this if needed
FILE_NAME = "sample.txt"
OBJECT_NAME = "uploads/sample.txt"

# print("🔑 Key:", AWS_KEY[:5], "********")  # Debug (partial key)
print("🌍 Region:", REGION)
print("📦 Bucket:", BUCKET_NAME)

try:
    # Create session
    session = boto3.Session(
        aws_access_key_id=AWS_KEY,
        aws_secret_access_key=AWS_SECRET,
        region_name=REGION
    )

    # Create S3 resource and upload
    s3 = session.resource('s3')
    s3.Bucket(BUCKET_NAME).upload_file(FILE_NAME, OBJECT_NAME)

    print(f"✅ File '{FILE_NAME}' uploaded to '{BUCKET_NAME}/{OBJECT_NAME}'")

except Exception as e:
    print(f"❌ Upload failed: Failed to upload {FILE_NAME} to {BUCKET_NAME}/{OBJECT_NAME}: {e}")
