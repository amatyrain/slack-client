import json
import requests


class SlackClient:
    def send_slack_message(
        self,
        url: str,
        message: str
    ):
        requests.post(url, data=json.dumps({
            "text": message,
        }))
