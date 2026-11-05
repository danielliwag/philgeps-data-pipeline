"""Upload local parquet data files to S3.

Reads parquet files from data/ and uploads them to the configured S3 bucket.
Bucket name is read from the S3_BUCKET environment variable.
"""

import os
from typing import List

import boto3
from botocore.exceptions import ClientError

DATA_DIR: str = "data"
S3_BUCKET: str = os.environ.get("S3_BUCKET", "philgeps-data-bucket")
S3_PREFIX: str = "data/"


def upload_parquet(file_path: str, bucket: str, key: str) -> None:
    """Upload a parquet file to S3."""
    s3 = boto3.client("s3")
    try:
        s3.upload_file(file_path, bucket, key)
        print(f"Uploaded {file_path} -> s3://{bucket}/{key}")
    except ClientError as e:
        print(f"S3 upload failed for {file_path}: {e}")
        raise


def list_parquet_files(directory: str) -> List[str]:
    """Return sorted list of .parquet files in the given directory."""
    return sorted(
        f for f in os.listdir(directory) if f.endswith(".parquet")
    )


def main() -> None:
    parquet_files: List[str] = list_parquet_files(DATA_DIR)
    if not parquet_files:
        print(f"No parquet files found in {DATA_DIR}/")
        return

    for filename in parquet_files:
        file_path: str = os.path.join(DATA_DIR, filename)
        key: str = S3_PREFIX + filename
        upload_parquet(file_path, S3_BUCKET, key)


if __name__ == "__main__":
    main()