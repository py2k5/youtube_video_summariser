output "lambda_function_name" {
  value = aws_lambda_function.youtube_summarizer.function_name
}

output "api_invoke_url" {
  value = aws_apigatewayv2_stage.default.invoke_url
}