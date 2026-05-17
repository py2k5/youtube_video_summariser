def generate_summary(transcript_text, video_url):
    """Generate summary using Google Generative AI"""
    
    # Create prompt
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
    
    # Initialize Google Generative AI
    llm = ChatGoogleGenerativeAI(
        model='gemini-3-flash-preview',
        google_api_key=GOOGLE_API_KEY
    )
    
    # Get response
    response = llm.invoke([HumanMessage(content=prompt)])
    
    # Extract text
    summary = response.content[0]['text']
    
    return summary