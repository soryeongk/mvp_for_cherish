import secret
from slacker import Slacker


# 메세지 보내기
slack = Slacker(secret.SLACK_TOKEN)
slack.chat.post_message('#mvp_test', '소령님! 진영님에게 연락 한 통 어떤가요? (오전 1시 45분)')
