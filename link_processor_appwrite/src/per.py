import requests

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