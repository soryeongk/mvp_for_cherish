import secret
from slacker import Slacker


# 메세지 보내기
slack = Slacker(secret.SLACK_TOKEN)
slack.chat.post_message('#mvp_test', '소령아, 오늘 주자씨에게 연락 했어..? (오전 1시 43분)')
