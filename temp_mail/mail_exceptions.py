class TenMinuteMailError(Exception):
    pass


class APIError(TenMinuteMailError):
    def __init__(self, status_code, message) -> None:
        self.status_code = status_code
        self.message = message
        super().__init__(f"TenMinuteMail API Error: {message} (Status Code: {status_code})")
        

class TimeoutError(TenMinuteMailError):
    def __init__(self, message) -> None:
        self.message = message
        super().__init__(f"TenMinuteMail Timeout Error: {message}")