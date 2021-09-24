from flask import Flask
from pytube import YouTube
from flask import request
import json

app = Flask(__name__)

@app.route("/youtube")
def downloadVideo():
    
    try:
        url = request.args.get('url')
        yt = YouTube(url).streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first()
        title = yt.title
        downloadUrl = yt.url
        response = json.dumps({"status": "Success", "title":title, "downloadUrl": downloadUrl})
        return response, 200
    except Exception as e:
        response = {"status":"Fail", "message":str(e)}
        return json.dumps(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)