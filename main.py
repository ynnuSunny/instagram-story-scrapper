
## rinning bot

from bots.instagram_bot import InstagramBot


service = "INSTAGRAM_BOT"
parameters = {
            "USER-NAME":"mx_lua2",
            "PASSWORD": "NGQ+nHA?8$9;4rM",
            "FRIENDS_STORY":True,
            # "INDEVIDUAL_STORY": True,
            # "USER_ID": "yoga_healers",


        }

instagram_bot = InstagramBot(
    parameters = parameters,
)
instagram_bot.init_driver_local_chrome()

data = instagram_bot.get_pages(service=service, )
print(data)

instagram_bot.close()
instagram_bot.quit()