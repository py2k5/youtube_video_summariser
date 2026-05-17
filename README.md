# YouTube Summariser Lambda

This project is an AWS Lambda function that summarizes YouTube videos by fetching their transcripts and generating concise summaries using Google Generative AI.

## Project Structure

```
youtube-summariser-lambda
├── src
│   ├── handler.py         # Main entry point for the AWS Lambda function
│   ├── youtube.py         # Functions to extract video ID and fetch transcripts
│   └── utils.py           # Function to generate summaries
├── tests
│   └── test_handler.py     # Unit tests for the handler functions
├── requirements.txt       # Project dependencies
├── template.yaml          # AWS SAM template for deployment
├── .gitignore             # Files and directories to ignore in Git
└── README.md              # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd youtube-summariser-lambda
   ```

2. **Install dependencies:**
   Make sure you have Python and pip installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure AWS Credentials:**
   Ensure that your AWS credentials are configured. You can set them up using the AWS CLI:
   ```bash
   aws configure
   ```

4. **Deploy the Lambda function:**
   Use the AWS SAM CLI to build and deploy the function:
   ```bash
   sam build
   sam deploy --guided
   ```

## Usage

Once deployed, you can invoke the Lambda function with an event containing a YouTube URL. The function will return a summary of the video.

## Testing

To run the unit tests, navigate to the `tests` directory and execute:
```bash
pytest test_handler.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.# youtube_video_summariser
