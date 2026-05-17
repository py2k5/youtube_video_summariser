// ...existing code...
terraform {
  required_version = ">= 1.3.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# If user provided an existing role name, read it. Otherwise create the role.
data "aws_iam_role" "existing" {
  count = var.existing_role_name != "" ? 1 : 0
  name  = var.existing_role_name
}

resource "aws_iam_role" "lambda_role" {
  count = var.existing_role_name == "" ? 1 : 0

  name = "youtube_summarizer_lambda_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
}

locals {
  lambda_role_arn  = var.existing_role_name != "" ? data.aws_iam_role.existing[0].arn : aws_iam_role.lambda_role[0].arn
  lambda_role_name = var.existing_role_name != "" ? data.aws_iam_role.existing[0].name : aws_iam_role.lambda_role[0].name
}

resource "aws_iam_role_policy_attachment" "lambda_basic_exec" {
  role       = local.lambda_role_name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# NEW: Lambda Layer with dependencies
resource "aws_lambda_layer_version" "dependencies_layer" {
  filename          = "../layer_package.zip"
  layer_name        = "youtube_summarizer_dependencies"
  compatible_runtimes = ["python3.12"]
  source_code_hash  = filebase64sha256("../layer_package.zip")
}

resource "aws_lambda_function" "youtube_summarizer" {
  filename         = "../deployment_package.zip"
  function_name    = "youtube-summarizer"
  role             = local.lambda_role_arn
  handler          = "src/handler.lambda_handler"
  runtime          = "python3.12"
  memory_size      = 128
  timeout          = 30
  source_code_hash = filebase64sha256("../deployment_package.zip")

  environment {
    variables = {
      GOOGLE_API_KEY = var.google_api_key
    }
  }

  # attach the layer
  layers = [
    aws_lambda_layer_version.dependencies_layer.arn
  ]
}