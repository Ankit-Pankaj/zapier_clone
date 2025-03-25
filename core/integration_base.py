# core/integration_base.py
from abc import ABC, abstractmethod
from core.exceptions import AuthenticationError

class IntegrationBase(ABC):
    """Abstract base class for all integrations"""

    def __init__(self, credentials: dict):
        """Initialize with authentication credentials"""
        if not isinstance(credentials, dict):
            raise TypeError("Credentials must be a dictionary.")
        try:
            self.auth_token = self.authenticate(credentials)
            if not self.auth_token:
                raise AuthenticationError("Received an empty auth token.")
        except Exception as e:
            raise AuthenticationError(str(e))
        
    @abstractmethod
    def authenticate(self, credentials: dict):
        """Method to authenticate and return an auth token"""
        pass
