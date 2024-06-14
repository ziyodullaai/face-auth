with open("img1.txt", "r") as f:
    img1 = f.read()

with open("img2.txt", "r") as f:
    img2 = f.read()

import requests

response = requests.post("http://localhost:8000/deepface/verify",json={
    "img_1": img1,
    "img_2": img2
})


print(response.json())