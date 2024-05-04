from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(youtube_url):
    video_id = youtube_url.split("v=")[-1]
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    # Try fetching the manual transcript
    try:
        transcript = transcript_list.find_manually_created_transcript()
    except:
        # If no manual transcript is found, try fetching an auto-generated transcript in a supported language
        try:
            generated_transcripts = [trans for trans in transcript_list if trans.is_generated]
            transcript = generated_transcripts[0]
        except:
            # If no auto-generated transcript is found, raise an exception
            return ''

    full_transcript = " ".join([part['text'] for part in transcript.fetch()])
    return full_transcript