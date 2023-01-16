from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json
import requests


app = FastAPI()
templates = Jinja2Templates(directory="templates")


def get_meme(sr="/wholesomememes"):

    print("sr", sr)
    url = "https://meme-api.com/gimme" + sr
    data = json.loads(requests.request("GET", url).text)

    # print(data)

    meme_pic = data["preview"][-2]
    subreddit = data["title"]

    return meme_pic, subreddit


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    meme_pic, subreddit = get_meme()

    return templates.TemplateResponse(
        "index.html", {"request": request, "meme_pic": meme_pic, "subreddit": subreddit}
    )


@app.get("/meirl", response_class=HTMLResponse)
def home(request: Request, sr: str = Form(...)):
    meme_pic, subreddit = get_meme(sr)

    return templates.TemplateResponse(
        "index.html", {"request": request, "meme_pic": meme_pic, "subreddit": subreddit}
    )
