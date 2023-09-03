import requests

payload = {
    "post": "Halo! Ini adalah teks auto generated :p",
    "platforms": ["youtube"],
    "mediaUrls": ["https://prod-streaming-video-msn-com.akamaized.net/6b75e47b-77b2-4ccd-9205-664b027b435c/fa549b41-3b69-4bb7-9f65-13965b1685ea.mp4"],
    "youTubeOptions": {
        "title": "Halo! Ini adalah teks auto generated :p"
    }
}
# "mediaUrls": ["https://img-prod-cms-rt-microsoft-com.akamaized.net/cms/api/am/imageFileData/RE4wB7q?ver=efee"],
# "platforms": ["facebook", "instagram", "twitter", "youtube", "tiktok", "linkedin", "pinterest"],

# Live API Key
headers = {'Content-Type': 'application/json', 
        'Authorization': 'Bearer 60V2J2C-SYAMKWW-QZVKKCT-4RDPZ81'}

r = requests.post('https://app.ayrshare.com/api/post', 
    json=payload, 
    headers=headers)
print(r.status_code)
print(r.text)