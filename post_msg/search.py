import json
import requests
from pandas.io.json import json_normalize
import secret


slack_token = secret.SLACK_TOKEN

# 채널 이름
ChannelName = "mvp_test"

# 채널 조회 API 메소드: conversations.list
URL = 'https://slack.com/api/conversations.list'

# 파라미터
params = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'token': slack_token
}

# API 호출
res = requests.get(URL, params=params)

channel_list = json_normalize(res.json()['channels'])
channel_id = list(
    channel_list.loc[channel_list['name'] == ChannelName, 'id'])[0]
