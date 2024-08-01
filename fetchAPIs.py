import requests


###------ API URLs ------
iG_baseUrl = "https://vdser.vercel.app/api/insta?link={ig_url}"
fB_baseUrl = url_res = "https://x2download.app/api/ajaxSearch"
tiktok_baseUrl = "https://www.tikwm.com/api/?url={tt_link}a?hd=1"
twitter_baseUrl = "https://ssstwitter.net/wp-json/aio-dl/video-data"

#### -------- media links --------
ig_link = "https://www.instagram.com/reel/C4KbeOCP_eJ/"
tt_link = "https://www.tiktok.com/@scottsreality/video/7392953456517975328"
fb_link = "https://www.facebook.com/reel/450816877661894"
yt_link = "https://www.youtube.com/watch?v=CtnHqQuOGgc"
twitter_link = "https://x.com/webseriestalks/status/1573983401081643008"


def facebbok_fetch(link: str):

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    }

    data = {"q": f"{link}", "vt": "home"}
    res = requests.post(fB_baseUrl, headers=headers, data=data)

    jsondata = res.json()
    return jsondata


def twitter_fetch(link: str):
    json_data = {
        "url": link,
        "token": "89454208b75aba7c652165c3be128034e9a4426a5a4d660930d8d18dd17c07a8",
    }
    resp = requests.post(twitter_baseUrl, json=json_data)
    return resp.json()


def tiktok_fetch(link: str):
    resp = requests.get(tiktok_baseUrl.format(tt_link=link))
    return resp.json()


def insta_fetch(link: str):
    resp = requests.get(iG_baseUrl.format(ig_url=link))
    return resp.json()


