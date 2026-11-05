terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "philgeps_data" {
  bucket = "philgeps-data-bucket"
}

resource "aws_s3_bucket_ownership_controls" "philgeps_data" {
  bucket = aws_s3_bucket.philgeps_data.id
  rule {
    object_ownership = "BucketOwnerEnforced"
  }
}

resource "aws_s3_bucket_versioning" "philgeps_data" {
  bucket = aws_s3_bucket.philgeps_data.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "philgeps_data" {
  bucket = aws_s3_bucket.philgeps_data.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}