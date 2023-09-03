import requests

# "platforms": ["facebook", "instagram", "twitter", "youtube", "tiktok", "linkedin", "pinterest"],

# Post
payload = {
    "post": "Ini adalah teks dan image auto generated from API eksternal :p",
    "platforms": ["instagram"],
    "mediaUrls": ["https://th.bing.com/th/id/OIP.gASMlPqsrIt_9q8Y76PZKgHaFj?pid=ImgDet&rs=1"],
}

# Live API Key
headers = {'Content-Type': 'application/json', 
        'Authorization': 'Bearer 60V2J2C-SYAMKWW-QZVKKCT-4RDPZ81'}

r = requests.post('https://app.ayrshare.com/api/post', 
    json=payload, 
    headers=headers)
print(r.status_code)
print(r.text)