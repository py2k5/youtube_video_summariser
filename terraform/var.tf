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

variable "existing_role_name" {
  description = "Name of an existing IAM role to use for Lambda. Leave empty to create the role."
  type        = string
  default     = ""
}