from abc import ABC, abstractmethod
from .log_message import LogMessage
from .log_formatter import LogFormatter, SimpleLogFormatter
import threading

class LogAppender(ABC):
    @abstractmethod
    def append(self, message: LogMessage) -> None:
        pass

    @abstractmethod
    def set_formatter(self, formatter: LogFormatter) -> None:
        pass

    @abstractmethod
    def get_formatter(self) -> LogFormatter:
        pass



class ConsoleLogAppender(LogAppender):
    def __init__(self):
        self.formatter = SimpleLogFormatter() # default formatter

    def append(self, message: LogMessage) -> None:
        formatted_message = self.formatter.format(message)
        print(formatted_message)

    def set_formatter(self, formatter: LogFormatter) -> None:
        self.formatter = formatter

    def get_formatter(self) -> LogFormatter:
        return self.formatter
    

class FileLogAppender(LogAppender):
    def __init__(self, file_path: str):
        self.formatter = SimpleLogFormatter() # default formatter
        self.thread_lock = threading.Lock()
        self.filesize_limit = 10 * 1024 * 1024  # 10 MB limit for example
        self.filename_index = 0
        self.file_path = file_path+ f".logs_{self.filename_index}.log"
        try:
            self.writer = open(self.file_path, 'a')
        except Exception as e:
            self.writer = None
            raise IOError(f"Failed to open log file {self.file_path}: {e}")
            

    def append(self, message: LogMessage) -> None:
        formatted_message = self.formatter.format(message)
        with self.thread_lock:
            try:
                # check file size and rotate if needed
                self.writer.seek(0, 2)  # Move to end of file
                if self.writer.tell() >= self.filesize_limit: # get file size in bytes
                    self.writer.close() 
                    self.filename_index += 1
                    self.file_path = self.file_path.split('.logs_')[0] + f".logs_{self.filename_index}.log"
                    self.writer = open(self.file_path, 'a')

                self.writer.write(formatted_message + '\n')
                self.writer.flush()
            except Exception as e:
                raise IOError(f"Failed to write to log file {self.file_path}: {e}")
    
    def close(self):
        if self.writer:
            try:
                self.writer.flush()
                self.writer.close()
            except Exception as e:
                raise IOError(f"Failed to close log file {self.file_path}: {e}")

    def set_formatter(self, formatter: LogFormatter) -> None:
        self.formatter = formatter

    def get_formatter(self) -> LogFormatter:
        return self.formatter