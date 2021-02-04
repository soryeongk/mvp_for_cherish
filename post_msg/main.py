
import secret

# from slacksocket import SlackSocket
from slacker import Slacker


# 메세지 보내기
slack = Slacker(secret.SLACK_TOKEN)
slack.chat.post_message('#team', 'Hello')

# 메세지 주고 받기

# s = SlackSocket(secret.SLACK_TOKEN, translate=True)

# for event in s.events():
#     print(event.json)

'''
from rtmbot import RtmBot
from rtmbot.core import Plugin

import chat_logic
import secret


class HelloPlugin(Plugin):
    def process_message(self, data):
        text = data["text"]
        if not text.startswith('소령 '):
            return

        # print(data)
        reply = chat_logic.answer(text[3:])
        if reply is not None:
            self.outputs.append([data["channel"], ':heart:' + reply])


config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.HelloPlugin"]
}
bot = RtmBot(config)
bot.start()
'''
