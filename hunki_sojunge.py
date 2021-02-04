import secret
from slacker import Slacker


# 메세지 보내기
slack = Slacker(secret.SLACK_TOKEN)
slack.chat.post_message('#mvp_test', '훈기님! 오늘은 소중이에게 물을 주는 날이에요!')
