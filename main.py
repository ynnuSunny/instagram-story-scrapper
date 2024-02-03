
## rinning bot

from bots.instagram_bot import InstagramBot


searched_keyword = "bangladeshtigers"
service = "INSTAGRAM_BOT"
parameters = {
            "FRIENDS_STORY":True,
            # "INDEVIDUAL_STORY": True,
            # "USER_ID": "yoga_healers",

        }

instagram_bot = InstagramBot(
    parameters = parameters,
)
instagram_bot.init_driver_local_chrome()
instagram_bot.get_pages(service=service, )
instagram_bot.close()
instagram_bot.quit()