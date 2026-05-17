from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

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
        # Create API instance and fetch transcript
        api = YouTubeTranscriptApi()
        transcript_data = api.fetch(video_id, languages=['en'])
        
        # Combine all transcript segments into one text
        full_text = " ".join([entry['text'] for entry in transcript_data])
        
        return full_text, len(full_text.split())
    
    except Exception as e:
        print(f"✗ Error: Could not fetch transcript - {e}")
        print("  Note: This video may not have English captions available.")
        return None, 0