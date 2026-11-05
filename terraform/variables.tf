variable "region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "bucket_name" {
  description = "Name of the S3 bucket for philgeps data"
  type        = string
  default     = "philgeps-data-bucket"
}