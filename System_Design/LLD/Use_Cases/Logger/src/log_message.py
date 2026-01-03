import threading
from datetime import datetime
from .log_level import LogLevel

class LogMessage:
    def __init__(self, level: LogLevel, message: str):
        self.level = level
        self.message = message
        self.timestamp = datetime.now()
        self.thread_id = threading.current_thread().ident

