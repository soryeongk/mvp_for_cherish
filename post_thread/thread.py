import json
import requests
from pandas.io.json import json_normalize
import secret
import trace

slack_token = secret.SLACK_TOKEN

chat_data = trace.chat_data
msg = chat_data.loc[chat_data['ts'] == trace.ts, 'text'].to_list()[0]
user_id = chat_data.loc[chat_data['ts'] == trace.ts, 'user'].to_list()[0]

users = {'U0147A175RQ': '소령'}
apply = msg.split('-')
user_id = user_id

message = f":cherries: {users[user_id]}님, 오늘을 기점으로 `{apply[1]}일`에 한 번 `{apply[2]}시` `{apply[0]}`에게의 물주기 신청이 완료되었습니다!"

# 파라미터
data = {'Content-Type': 'application/x-www-form-urlencoded',
        'token': slack_token,
        'channel': trace.channel_id,
        'text': message,
        'reply_broadcast': 'True',
        'thread_ts': trace.ts
        }

try:
    # 메시지 등록 API 메소드: chat.postMessage
    URL = "https://slack.com/api/chat.postMessage"
    res = requests.post(URL, data=data)
    passed = True
except:
    passed = False
