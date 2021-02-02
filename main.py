from slacker import Slacker
import secret

slack = Slacker(secret.SLACK_TOKEN)

slack.chat.post_message("#team", "successed!")
