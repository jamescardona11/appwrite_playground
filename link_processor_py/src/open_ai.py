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


    prompt= """You are a web content summarization AI. You will summarize the content of a provided web page, focusing on extracting the most relevant information and key points.
        - The summary must be concise and limited to 30 lines.
        - Avoid any phrases that reference the structure of the post, such as "the next post," "the post is," or "this medium post."
        - Do not include any preamble, commentary, or quotes in the output.
         Present the summary in a clear and organized manner, ensuring it captures the essence of the content without unnecessary details."""

    sP = link

    if summary != "":
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
