from .utils import  throw_if_missing
from .per import  perplexity_aI
from .yt import  get_transcript
from .open_ai import  open_ai
import os


def main(context):
    throw_if_missing(os.environ, ["PERPLEXITY_API_KEY", "OPENAI_API_KEY"])

    if context.req.method == "GET":
        return context.res.json({"ok": True, "response": "Hello, world!"}, 200)

    try:
        throw_if_missing(context.req.body, ["link"])
    except:
        return context.res.json({"ok": False, "response": ''}, 200)

    link = context.req.body["link"]
    onlySummary = context.req.body["onlySummary"] or False
    summary = context.req.body["summary"] or ""

    result = ''
    if "youtube.com" in link and onlySummary == False:
        result = get_transcript(link)
    elif onlySummary:
        result = open_ai(context, link, summary)
    else:
        result = perplexity_aI(context, link)

    return context.res.json({"ok": True, "response": result}, 200)


