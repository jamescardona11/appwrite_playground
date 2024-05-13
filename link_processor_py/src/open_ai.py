import requests
import os


def open_ai(context, link, summary):
    url = "https://api.openai.com/v1/chat/completions"
    api_key = os.environ["OPENAI_API_KEY"]
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer " + api_key   
    }
    
    
    prompt= "Give the summary for the next url; maximum 30 words."
    sP = link
    
    if summary != "":
        prompt= "Give the summary for next text something short; maximum 30 words."
        sP = summary
    
    context.log("prompt")
    context.log(prompt)
    

    
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": prompt}, 
            {"role": "user", "content": sP}
        ],
    }

    
    

    try:
        response = requests.post(url, json=payload, headers=headers)
        json = response.json()
        context.log(json)
        
        
        result = json['choices'][0]['message']['content']
        
        return result
    
    except Exception as e:
        context.error(e)
        return ''