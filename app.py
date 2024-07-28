from flask import Flask, jsonify, request
from yt_api import video_info

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/info", methods=["GET"])
def get_video_data():
    video_url = request.args.get("url")
    data = video_info(video_url)
    return jsonify(data)


if __name__ == "__main__":
    app.run()
