# core/integration_base.py
class IntegrationBase:
    def authenticate(self, credentials: dict):
        """Handles authentication"""
        raise NotImplementedError
