import os
import boto3
from dotenv import load_dotenv

# Load .env file (if you are using one)
load_dotenv()

def test_env_variables():
    print("Checking Environment Variables...\n")

    access_key = os.getenv("AWS_ACCESS_KEY_ID")
    secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    region = os.getenv("AWS_DEFAULT_REGION")

    print("AWS_ACCESS_KEY_ID:", access_key)
    print("AWS_SECRET_ACCESS_KEY:", "SET" if secret_key else None)
    print("AWS_DEFAULT_REGION:", region)

    if not access_key:
        print("\n❌ AWS_ACCESS_KEY_ID is NOT set")
    else:
        print("✅ AWS_ACCESS_KEY_ID is set")

    if not secret_key:
        print("❌ AWS_SECRET_ACCESS_KEY is NOT set")
    else:
        print("✅ AWS_SECRET_ACCESS_KEY is set")


def test_s3_connection():
    print("\nTesting S3 Connection...\n")

    try:
        s3 = boto3.client("s3")
        response = s3.list_buckets()

        print("✅ Connected successfully!")
        print("\nAvailable Buckets:")
        for bucket in response["Buckets"]:
            print(" -", bucket["Name"])

    except Exception as e:
        print("❌ S3 Connection Failed")
        print("Error:", e)


if __name__ == "__main__":
    test_env_variables()
    test_s3_connection()