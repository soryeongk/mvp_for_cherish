import secret
from slacker import Slacker

slack = Slacker(secret.SLACK_TOKEN)
slack.chat.post_message('#mvp_test', '영탁님! 오늘은 샐러드에게 물을 주는 날이에요.')

