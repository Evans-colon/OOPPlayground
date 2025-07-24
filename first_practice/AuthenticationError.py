class AuthenticationError(Exception):
    def __init__(self, message="Authentication Failed"):
        super(AuthenticationError, self).__init__(message)