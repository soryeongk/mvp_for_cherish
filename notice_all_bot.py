import secret
from slacker import Slacker


# 메세지 보내기
slack = Slacker(secret.SLACK_TOKEN)
slack.chat.post_message('#mvp_test', '오늘 저녁 10시 전체 회의 있습니다! :cherries:')

