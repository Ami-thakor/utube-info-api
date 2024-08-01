from flask import Flask, jsonify, request
from yt_api import yt_fetchData
from fetchAPIs import *

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/yt", methods=["GET"])
def get_yt_data():
    video_url = request.args.get("url")
    data = yt_fetchData(video_url)
    return jsonify(data)


@app.route("/ig", methods=["GET"])
def get_ig_data():
    video_url = request.args.get("url")
    data = insta_fetch(video_url)
    return jsonify(data)


@app.route("/twitter", methods=["GET"])
def get_twitter_data():
    video_url = request.args.get("url")
    data = twitter_fetch(video_url)
    return jsonify(data)


@app.route("/tiktok", methods=["GET"])
def get_tiktok_data():
    video_url = request.args.get("url")
    data = tiktok_fetch(video_url)
    return jsonify(data)


@app.route("/fb", methods=["GET"])
def get_fb_data():
    video_url = request.args.get("url")
    data = facebbok_fetch(video_url)
    return jsonify(data)
