from abc import ABC, abstractmethod

from .log_message import LogMessage

class LogFormatter(ABC):
    @abstractmethod
    def format(self, message: LogMessage) -> str:
        pass


class SimpleLogFormatter(LogFormatter):
    def format(self, message: LogMessage) -> str:
        return f"[{message.timestamp}] [{message.level.name}] [Thread-{message.thread_id}]: {message.message}"
    
    def __str__(self):
        return "SimpleLogFormatter"