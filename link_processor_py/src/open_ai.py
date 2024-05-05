import openai
import os


def open_ai(context, link):

    prompt= "Give the summary for the next url; maximum 30 words:" + link

    openai.api_key = os.environ["OPENAI_API_KEY"]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            max_tokens=int(os.environ.get("OPENAI_MAX_TOKENS", "512")),
            messages=[{"role": "user", "content": prompt}],
            
        )
        completion = response.choices[0].message.content
        return context.res.json({"ok": True, "completion": completion}, 200)

    except Exception:
        return context.res.json({"ok": False, "error": "Failed to query model."}, 500)