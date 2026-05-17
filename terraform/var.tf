variable "tf_state_bucket" {
  type        = string
  description = "S3 bucket for Terraform state"
  default     = "pradip-tf-state-bucket"
}

variable "tf_state_key" {
  type        = string
  description = "S3 key for Terraform state file"
  default     = "terraform.tfstate"
}

variable "google_api_key" {
  description = "Google API Key for Generative AI"
  type        = string
  sensitive   = true
  default = "value_should_be_set_in_github_actions_secrets_or_terraform.tfvars"
}

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}