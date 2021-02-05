import thread
from datetime import datetime


user = thread.user
data = thread.msg
name = data[0]
cycle = data[1]
time = data[2]
today = int(datetime.today().strftime('%d'))
route = "/home/ubuntu/work/soryeongk/mvp_for_cherish/post_msg"
cmd = f"#!/bin/bash\n\nvi {route}/{user}_{name}.py\nsudo sed -i '$ a\\0 {time} {today}-28/{cycle} * * python3 post_msg.py' /var/spool/cron/crontabs/ubuntu\n"
py_code = """
import secret
from slacker import Slacker


# 메세지 보내기
slack = Slacker(secret.SLACK_TOKEN)
slack.chat.post_message('#mvp_test', '소령님! 오늘은 주자씨에게 물을 주는 날이에요.')
"""
with open(f"{route}/post_msg_{user}_{name}.py", "w") as f:
    f.write(py_code)

with open("gen_cron.sh", "a") as f:
    f.write(cmd)
