// ...new file...
output "lambda_function_name" {
  value = aws_lambda_function.youtube_summarizer.function_name
}

output "lambda_function_arn" {
  value = aws_lambda_function.youtube_summarizer.arn
}

output "layer_arn" {
  value = aws_lambda_layer_version.dependencies_layer.arn
}