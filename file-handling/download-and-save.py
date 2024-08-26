import requests

url = "https://www.appclick.ng/assets/img/course/appclick-academy-courses-graphic-design-training-institute-in-ibadan-lagos-nigeria.jpg"

response = requests.get(url)

print(response.ok)

if response.ok: 
    file = open("online.png", "wb")
    file.write(response.content)
    file.close()