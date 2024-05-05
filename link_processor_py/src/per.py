from .open_ai import  open_ai
import requests
import os

def perplexity_aI(context, link):
    url = "https://api.perplexity.ai/chat/completions"

    prompt = "Your task is give the transcribe word by word this post if the post is private or can't access the post, you can give the summary of the post."
    payload = {
        "model": "mistral-7b-instruct",
        "messages": [
            {
                "role": "user",
                "content": prompt
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
        context.log(json['choices'][0]['message']['content'])

        
        result = json['choices'][0]['message']['content']

        if "I cannot provide" in result:
            return open_ai(context, link)

        return json['choices'][0]['message']['content']
        
        
    except Exception as e:
        context.error(e)
        return ''