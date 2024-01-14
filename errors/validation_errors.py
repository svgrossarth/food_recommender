
class ValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
        
    def error_response(self):
        return f'Invalid input: {self.message}'

class InvalidJSON(ValidationError):
    def __init__(self, message):
        super().__init__(message)

class InvalidJSONField(ValidationError):
    def __init__(self, message):
        super().__init__(message)

