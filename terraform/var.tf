variable "google_api_key" {
  description = "Google API Key for Generative AI"
  type        = string
  sensitive   = true
}

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}