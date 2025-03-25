# integrations/Gmail/Gmail.py
from core.integration_base import IntegrationBase
from .auth import GmailAuth
import requests
from core.exceptions import APIRequestError


class GmailIntegration(IntegrationBase):
    """Gmail Integration Strategy"""

    def authenticate(self, credentials: dict):
        """Authenticate using Gmail's own auth method"""
        return GmailAuth.authenticate(credentials)
    
    def send_email(self, params):
        """Sends an email to a Gmail channel"""
        if not isinstance(params, dict):
            raise TypeError("params must be a dictionary.")
        try:
            return {'success': True, 'data': {'data': 'output data', 'metadata': 'output metadata'}}
        except requests.RequestException as e:
            raise APIRequestError(f"Gmail API request failed: {str(e)}")
        
    def fetch_emails(self, params):
        """Fetches recent emails from gmail"""
        try:
            headers = {"Authorization": f"Bearer {self.auth_token}"}
            return {'success': True, 'data': {'mails': [{'data': 'email data'}, {'data': 'email data'}], 'metadata': 'output metadata'}}
        except requests.RequestException as e:
            raise APIRequestError(f"Gmail API request failed: {str(e)}")