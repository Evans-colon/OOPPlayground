class ValidationError(Exception):
    def __init__(self, message="Validation Failed"):
        super(ValidationError, self).__init__(message)