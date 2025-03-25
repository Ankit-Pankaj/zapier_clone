# core/exceptions.py
class IntegrationError(Exception):
    """Base class for all integration-related errors"""
    pass

class AuthenticationError(IntegrationError):
    """Raised when authentication fails"""
    def __init__(self, message="Authentication failed"):
        super().__init__(message)

class APIRequestError(IntegrationError):
    """Raised when an API request fails"""
    def __init__(self, message="API request failed", status_code=None):
        self.status_code = status_code
        super().__init__(f"{message} (HTTP {status_code})" if status_code else message)
