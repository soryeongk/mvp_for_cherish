import json
import requests
from pandas.io.json import json_normalize
import re
import secret
import search


channel_id = search.channel_id
# 채널 내 문구 조회 API 메소드: conversations.list
URL = 'https://slack.com/api/conversations.history'

# 파라미터
params = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'token': secret.SLACK_TOKEN,
    'channel': channel_id
}

# API 호출
res = requests.get(URL, params=params)
chat_data = json_normalize(res.json()['messages'])
# print(res.json()['messages'])
chat_data['text'] = chat_data['text'].apply(lambda x: x.replace("\xa0", " "))
msg = chat_data.loc[chat_data['text'].str.match(
    r".+-\d+-\d+") == True, 'text'].to_list()[0]
ts = chat_data.loc[chat_data['text'] == msg, 'ts'].to_list()[0]
user = chat_data.loc[chat_data['text'] == msg, 'user'].to_list()[0]
