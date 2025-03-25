# integrations/slack/slack.py
from core.integration_base import IntegrationBase
from .auth import SlackAuth
import requests
from core.exceptions import APIRequestError


class SlackIntegration(IntegrationBase):
    """Slack Integration Strategy"""

    def authenticate(self, credentials: dict):
        """Authenticate using Slack's own auth method"""
        return SlackAuth.authenticate(credentials)
    
    def send_message(self, channel:str, message:str):
        """Sends a message to a Slack channel"""
        # write logic to fetch messages
        if not isinstance(channel, str) or not isinstance(message, str):
            raise TypeError("Channel and message must be strings.")
        try:
            # logic to send a messge to slack channel
            return {'success': True, 'data': {'message': 'output message', 'metadata': 'output metadata'}}
        except requests.RequestException as e:
            raise APIRequestError(f"Slack API request failed: {str(e)}")
        
    def get_channels(self, params):
        """Fetches available Slack channels"""
        try:
            headers = {"Authorization": f"Bearer {self.auth_token}"}
            return {'success': True, 'data': {'channels': [{'channel_id': 'id_0'}, {'channel_id': 'id_1'}], 'metadata': 'output metadata'}}
        except requests.RequestException as e:
            raise APIRequestError(f"Slack API request failed: {str(e)}")