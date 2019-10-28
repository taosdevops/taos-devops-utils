""" Module to handle slack messaging """
import slack
import os
from taosdevopsutils import config
import requests
import json


class Slack:
    def __init__(self, token=config.SLACK_API_TOKEN):
        self.client = slack.WebClient(token=token)

    def _handle_webhook(self, target: str, message: str):
        if isinstance(message, str):
            response = requests.post(
                target, data=message, headers={"Content-Type": "application/json"}
            )
            try:
                payload = json.loads(message)
            except json.JSONDecodeError:
                payload = {"text": message}
        else:
            payload = message

        response = requests.post(target, json=payload)
        return {
            "status_code": response.status_code,
            "ok": response.status_code == 200,
            "message": message,
            "response": response.text,
        }

    def _handle_direct_message(self, target: str, message: str):
        if isinstance(message, str):
            return self.client.chat_postMessage(
                channel=target, text=message, as_user=True
            )
        return self.client.chat_postMessage(channel=target, as_user=True, **message)

    def post_slack_message(self, target: str, message: str):
        if target.startswith("https://"):
            return self._handle_webhook(target, message)
        return self._handle_direct_message(target, message)
