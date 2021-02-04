import secret
from slacker import Slacker


# 메세지 보내기
slack = Slacker(secret.SLACK_TOKEN)
slack.chat.post_message('#0_notice', '오늘 저녁 9시 스크럼 회의 있습니다!')
