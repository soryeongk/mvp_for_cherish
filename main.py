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
