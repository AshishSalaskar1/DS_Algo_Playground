from abc import ABC, abstractmethod
from .log_message import LogMessage
from .log_appender import LogAppender    

from queue import Queue
import threading
from concurrent.futures import ThreadPoolExecutor


class LogProcessor(ABC):
    @abstractmethod
    def process(self, message: LogMessage, appenders: list[LogAppender]) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass



class AsyncLogProcessor(LogProcessor):
    def __init__(self, worker_count: int = 1, queue_size: int = 10):
        self.queue = Queue(maxsize=queue_size)
        self.executor = ThreadPoolExecutor(max_workers=worker_count)
        self.stop_signal = threading.Event()
        
        # Submit worker tasks to the executor -> runs in the background
        for _ in range(worker_count):
            self.executor.submit(self._worker)
    
    # background worker method -> runs and waits for log messages to get added in the queue
    def _worker(self):
        while not self.stop_signal.is_set() or not self.queue.empty():
            try:
                message, appenders = self.queue.get(timeout=0.1)
                for appender in appenders:
                    appender.append(message)
                self.queue.task_done() # tell the queue that the task is done
            except Exception:
                continue
    
    def process(self, message: LogMessage, appenders: list[LogAppender]) -> None:
        self.queue.put((message, appenders))
    
    def stop(self) -> None:
        self.stop_signal.set()
        self.executor.shutdown(wait=True)