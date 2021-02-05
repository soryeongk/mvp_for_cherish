import thread
from datetime import datetime


data = thread.msg
name = data[0]
cycle = data[1]
time = data[2]
today = int(datetime.today().strftime('%d'))

cmd = f"0 {time} {today}-28/{cycle} * * python3 /home/ubuntu/work/soryeongk/mvp_for_cherish/post_msg/test.py"
print(cmd)
