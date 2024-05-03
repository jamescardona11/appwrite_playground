
import requests
from youtube_transcript_api import YouTubeTranscriptApi

from .utils import  throw_if_missing
import os


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
            raise Exception("No suitable transcript found.")

    full_transcript = " ".join([part['text'] for part in transcript.fetch()])
    return full_transcript


def perplexity_aI(link):
    url = "https://api.perplexity.ai/chat/completions"

    payload = {
        "model": "mistral-7b-instruct",
        "messages": [
            {
                "role": "system",
                "content": "Your task is give the transcribe word by word this post if the post is private or can't access the post, you can give the summary of the post."
            },
            {
                "role": "user",
                "content": link
            }
        ]
    }
    
    api_key = os.environ["PERPLEXITY_API_KEY"]
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer " + api_key

    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        json = response.json()
        
        if(json['choices'].length == 0):
            return json['choices'][0]['message']['content']
        else:
            return ''
        
    except:
        return ''

def main(context):
    throw_if_missing(os.environ, ["PERPLEXITY_API_KEY"])

    if context.req.method == "GET":
        return context.res.json({"ok": True, "response": "Hello, world!"}, 200)

    try:
        throw_if_missing(context.req.body, ["link"])
    except:
        return context.res.json({"ok": False, "response": ''}, 200)

    link = context.req.body["link"]

    result = ''
    if "youtube.com" in link:
        result = get_transcript(link)
    else:
        result = perplexity_aI(link)

    return context.res.json({"ok": True, "response": result}, 200)


