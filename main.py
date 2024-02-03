
## rinning bot

from bots.instagram_bot import InstagramBot
import requests
import json

service = "INSTAGRAM_BOT"
parameters = {
            # "USER-NAME":"mx_lua2",
            # "PASSWORD": "NGQ+nHA?8$9;4rM",
            "USER-NAME":"__ful22__",
            "PASSWORD": "flower@@@",
            "FRIENDS_STORY":True,
            # "INDEVIDUAL_STORY": True,
            # "USER_ID": "yoga_healers",

        }

instagram_bot = InstagramBot(
    parameters = parameters,
)
instagram_bot.init_driver_local_chrome()

data = instagram_bot.get_pages(service=service, )
# print(data)

instagram_bot.close()
instagram_bot.quit()


url = "http://192.168.20.148:8010/api/social-media/save-social-media-data/"
response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    print("Response:", result)
else:
    print("Success:", response.status_code)
    print(response.text)