import json
import requests
from datetime import date

with open('api_key.txt', 'r') as f:
    text = f.read()
    access_token = text[76:]

headers = {"Authorization": access_token}
para = {
    "name": f'{str(date.today())}.jpg',
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("./image.png", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)