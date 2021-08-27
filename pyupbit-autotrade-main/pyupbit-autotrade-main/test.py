from requests.api import post
import requests
import pyupbit


access = "pvL1StUtbeKUGFdbdQzZdDqe8bOwpJmdTxzygPfs"
secret = "OxbvrFYnmZg1Ecj2xuz9vnfRx50AZQwxJ740gfG8"
myToken = "xoxb-2347464085765-2350723876131-kEIcYa2Nb66i5vE3WR2qfzNi"

upbit = pyupbit.Upbit(access, secret)


def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer "+token},
                             data={"channel": channel, "text": text}
                             )
    print(response)


data = upbit.get_balance("BTC")

post_message(myToken, "#notification", str(data))
