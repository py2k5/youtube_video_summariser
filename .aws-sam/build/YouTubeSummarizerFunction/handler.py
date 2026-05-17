from youtube_transcript_api import YouTubeTranscriptApi
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage
import json

def get_video_id(url):
    """Extract video ID from YouTube URL"""
    if 'youtu.be' in url:
        return url.split('/')[-1].split('?')[0]
    elif 'youtube.com' in url:
        parsed = urlparse(url)
        video_id = parse_qs(parsed.query).get('v', [None])[0]
        return video_id
    return None

def get_transcript(video_id):
    """Get transcript from YouTube video"""
    try:
        api = YouTubeTranscriptApi()
        transcript_data = api.fetch(video_id, languages=['en'])
        full_text = " ".join([entry['text'] for entry in transcript_data])
        return full_text, len(full_text.split())
    except Exception as e:
        return None, 0

def generate_summary(transcript_text, video_url):
    """Generate summary using Google Generative AI"""
    prompt = f"""Summarize this YouTube video transcript in a clear, structured format.

Video URL: {video_url}

Transcript:
{transcript_text}

Provide:
1. A concise 2-3 paragraph summary of the main content
2. Key topics covered (as bullet points)
3. Main takeaways (as a numbered list)
4. Whether the video is worth watching and for whom

Keep it concise but informative. Use clear headings and formatting."""
    
    llm = ChatGoogleGenerativeAI(
        model='gemini-3-flash-preview',
        google_api_key=GOOGLE_API_KEY
    )
    
    response = llm.invoke([HumanMessage(content=prompt)])
    summary = response.content[0]['text']
    
    return summary

def lambda_handler(event, context):
    """Main entry point for the AWS Lambda function"""
    url = event.get('url')
    
    if not url:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing YouTube URL'})
        }
    
    video_id = get_video_id(url)
    
    if not video_id:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid YouTube URL'})
        }
    
    transcript_text, word_count = get_transcript(video_id)
    
    if not transcript_text:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Could not fetch transcript'})
        }
    
    summary = generate_summary(transcript_text, url)
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'summary': summary,
            'word_count': word_count
        })
    }