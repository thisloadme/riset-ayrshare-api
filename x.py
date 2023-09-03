import requests

# "platforms": ["facebook", "instagram", "twitter", "youtube", "tiktok", "linkedin", "pinterest"],

# Post
payload = {
    "post": "Halo! Ini adalah teks auto generated :p",
    "platforms": ["twitter"],
    "mediaUrls": ["https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA11N2LX.img"],
}

# Live API Key
headers = {'Content-Type': 'application/json', 
        'Authorization': 'Bearer 60V2J2C-SYAMKWW-QZVKKCT-4RDPZ81'}

r = requests.post('https://app.ayrshare.com/api/post', 
    json=payload, 
    headers=headers)
print(r.status_code)
print(r.text)