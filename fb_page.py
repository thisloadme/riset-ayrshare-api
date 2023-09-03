import requests

# "platforms": ["facebook", "instagram", "twitter", "youtube", "tiktok", "linkedin", "pinterest"],

# Post
# payload = {
#     "post": "Halo! Ini adalah teks auto generated :p",
#     "platforms": ["facebook"],
#     "mediaUrls": ["https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA11N2LX.img"],
# }

# reels
payload = {
    "post": "Testing reel video",
    "platforms": ["facebook"],
    "mediaUrls": ["https://img.ayrshare.com/012/reel.mp4"],
    "faceBookOptions": {
        "reels": 1,
        "title": "Judul Reel"
    }
}

# Live API Key
headers = {'Content-Type': 'application/json', 
        'Authorization': 'Bearer 60V2J2C-SYAMKWW-QZVKKCT-4RDPZ81'}

r = requests.post('https://app.ayrshare.com/api/post', 
    json=payload, 
    headers=headers)
print(r.status_code)
print(r.text)