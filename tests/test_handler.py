from unittest import TestCase
from src.handler import lambda_handler

class TestLambdaHandler(TestCase):
    def test_valid_url(self):
        event = {
            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        }
        response = lambda_handler(event, None)
        self.assertIn("summary", response)
        self.assertIn("video_id", response)

    def test_invalid_url(self):
        event = {
            "url": "invalid_url"
        }
        response = lambda_handler(event, None)
        self.assertEqual(response, {"error": "Invalid YouTube URL"})

    def test_missing_url(self):
        event = {}
        response = lambda_handler(event, None)
        self.assertEqual(response, {"error": "No URL provided"})