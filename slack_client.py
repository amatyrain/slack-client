import json
import requests


class SlackClient:
    def __init__(
        self,
        api_token: str = None
    ):
        self.base_url = "https://slack.com/api"
        self.api_token = api_token
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
        }

    def _request(
        self,
        method: str,
        url: str,
        params: dict = None,
    ):
        print(f"method: {method}")
        print(f"url: {url}")
        print(f"params: {params}")

        try:
            response = requests.request(method, url, params=params, headers=self.headers)
        except Exception as e:
            raise Exception(e)

        response_json = response.json()

        if (
            not response_json["ok"] or
            response.status_code >= 400
        ):
            raise Exception(response.json())

        return response

    def get_conversations_history(
        self,
        channel: str,
        limit: int = 1000,
        latest: str = None,
        oldest: str = None,
    ):
        url = f"{self.base_url}/conversations.history"
        method = "GET"

        params = {
            "channel": channel,
            "limit": limit,
        }

        if latest is not None:
            params["latest"] = latest
        if oldest is not None:
            params["oldest"] = oldest

        response = self._request(method, url, params=params)

        return response.json()

    def send_slack_message(
        self,
        url: str,
        message: str
    ):
        requests.post(url, data=json.dumps({
            "text": message,
        }))
