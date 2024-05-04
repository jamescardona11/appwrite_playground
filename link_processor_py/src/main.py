from .utils import  throw_if_missing
from .per import  perplexity_aI
from .yt import  get_transcript
import os


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
        result = perplexity_aI(context, link)

    return context.res.json({"ok": True, "response": result}, 200)


