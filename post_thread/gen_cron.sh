#!/bin/bash

vi /home/ubuntu/work/soryeongk/mvp_for_cherish/post_msg/소령_엶.py
sudo sed -i '$ a\0 13 5-28/2 * * python3 post_msg.py' /var/spool/cron/crontabs/ubuntu
