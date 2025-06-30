import boto3
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

try:
    # Use the IAM role attached to the EC2 instance
    sts_client = boto3.client('sts')
    identity = sts_client.get_caller_identity()
    logging.info(f"Caller Identity: {identity}")

    s3 = boto3.client('s3')
    bucket_name = 'sa-app-logs-gabriel'  # Replace with your actual bucket

    # Attempt to list objects to verify access
    response = s3.list_objects_v2(Bucket=bucket_name)

    if 'Contents' in response:
        logging.info(f"S3 Bucket '{bucket_name}' Contents:")
        for obj in response['Contents']:
            logging.info(f" - {obj['Key']}")
    else:
        logging.warning("Bucket is empty or access issue.")

except Exception as e:
    logging.error(f"Access failed: {e}")
