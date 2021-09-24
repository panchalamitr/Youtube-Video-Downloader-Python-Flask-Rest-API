# Youtube-Video-Downloader-Python-Flask-Rest-API

This is Python backend Rest API Service, which takes Youtube video url from GET request 

For example below is the request url from client side.

http://localhost:8080/youtube?url=https://www.youtube.com/watch?v=tf0vkRUlRms

Here, by usign below python code, we can extract "url" value,

```
url = request.args.get('url')
```

now result is like below,

https://www.youtube.com/watch?v=tf0vkRUlRms

Now, we will use above result and pass it to [pytube](https://github.com/pytube/pytube), to get youtube video's title and video download url.

```
yt = YouTube(url).streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first()

title = yt.title
downloadUrl = yt.url
```
These "Title" and "Download Video Url" will be send back to client with JSON response like below,

```
{
    "status": "Success", 
    "title": "Titan: The Marriage Proposal", 
    "downloadUrl": "https://r5---sn-nu5gi0c-npoee.googlevideo.com/videoplayback?expire=1632489280&ei=4HpNYam1C4WUvgSMt6CIBw&ip=lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIgSKebZlWioSXROEslL_PDNBI_YZJ3Uo37jmx7Y0DqGFACIQDf6h8_ft9WnKpskxPesk2l3p0DlLwR2S_RSECHNQnwTA%3D%3D"
}
```

If any problem with youtube video url then response will be below

```
{
    "status": "Fail", 
    "message": "regex_search: could not find match for (?:v=|\\/)([0-9A-Za-z_-]{11}).*"
}
