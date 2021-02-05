import json
import requests
from pandas.io.json import json_normalize
import secret
import trace


msg = trace.msg.split('-')
users = {'U0147A175RQ': '소령'}
user_id = trace.user
user = users[user_id]

message = f":cherries: {user}님, 오늘을 기점으로 `{msg[1]}일`에 한 번 `{msg[2]}시` `{msg[0]}`에게의 물주기 신청이 완료되었습니다!"

# 파라미터
data = {'Content-Type': 'application/x-www-form-urlencoded',
        'token': secret.SLACK_TOKEN,
        'channel': trace.channel_id,
        'text': message,
        'reply_broadcast': 'True',
        'thread_ts': trace.ts
        }

# 메시지 등록 API 메소드: chat.postMessage
URL = "https://slack.com/api/chat.postMessage"
res = requests.post(URL, data=data)

print('done')
