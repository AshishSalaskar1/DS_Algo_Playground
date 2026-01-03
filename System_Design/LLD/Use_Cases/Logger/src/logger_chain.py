from abc import ABC, abstractmethod
from .log_level import LogLevel
from .log_message import LogMessage
from .log_appender import LogAppender


class AbstractLogger(ABC):
    """Base class for Chain of Responsibility logger"""
    
    def __init__(self, level_threshold: LogLevel, appenders: list[LogAppender] = None):
        self.level_threshold = level_threshold
        self.appenders = appenders or []
        self.next_logger = None

    
    def set_next_logger(self, logger: 'AbstractLogger') -> 'AbstractLogger':
        """Set the next logger in the chain"""
        self.next_logger = logger
        return logger
    
    def log(self, level: LogLevel, message: str) -> None:
        """Process log if level matches, then pass to next in chain"""
        if level == self.level_threshold:
            self.write(level, message)
        
        # Pass to next logger in chain
        if self.next_logger:
            self.next_logger.log(level, message)
    
    @abstractmethod
    def write(self, level: LogLevel, message: str) -> None:
        """Actual logging implementation"""
        pass


class DebugLogger(AbstractLogger):
    """Handles DEBUG level logs"""
    
    def __init__(self, appenders: list[LogAppender] = None):
        super().__init__(LogLevel.DEBUG, appenders)
    
    def write(self, level: LogLevel, message: str) -> None:
        if level == LogLevel.DEBUG:
            log_message = LogMessage(level, message)
            for appender in self.appenders:
                appender.append(log_message)


class InfoLogger(AbstractLogger):
    """Handles INFO level logs"""
    
    def __init__(self, appenders: list[LogAppender] = None):
        super().__init__(LogLevel.INFO, appenders)
    
    def write(self, level: LogLevel, message: str) -> None:
        if level == LogLevel.INFO:
            log_message = LogMessage(level, message)
            for appender in self.appenders:
                appender.append(log_message)


class WarningLogger(AbstractLogger):
    """Handles WARNING level logs"""
    
    def __init__(self, appenders: list[LogAppender] = None):
        super().__init__(LogLevel.WARNING, appenders)
    
    def write(self, level: LogLevel, message: str) -> None:
        if level == LogLevel.WARNING:
            log_message = LogMessage(level, message)
            for appender in self.appenders:
                appender.append(log_message)


class ErrorLogger(AbstractLogger):
    """Handles ERROR level logs"""
    
    def __init__(self, appenders: list[LogAppender] = None):
        super().__init__(LogLevel.ERROR, appenders)
    
    def write(self, level: LogLevel, message: str) -> None:
        if level == LogLevel.ERROR:
            log_message = LogMessage(level, message)
            for appender in self.appenders:
                appender.append(log_message)


class CriticalLogger(AbstractLogger):
    """Handles CRITICAL level logs"""
    
    def __init__(self, appenders: list[LogAppender] = None):
        super().__init__(LogLevel.CRITICAL, appenders)
    
    def write(self, level: LogLevel, message: str) -> None:
        if level == LogLevel.CRITICAL:
            log_message = LogMessage(level, message)
            for appender in self.appenders:
                appender.append(log_message)


def create_logger_chain(
    appenders_list: list[LogAppender] = None,
    debug_appenders: list[LogAppender] = None,
    info_appenders: list[LogAppender] = None,
    warning_appenders: list[LogAppender] = None,
    error_appenders: list[LogAppender] = None,
    critical_appenders: list[LogAppender] = None
) -> AbstractLogger:
    """
    Create a chain of loggers for different levels with specified appenders.
    
    If appenders_list is provided, all levels use the same appenders.
    Otherwise, use specific appenders for each level.
    """
    # If a single appenders list is provided, use it for all levels
    if appenders_list is not None:
        debug_appenders = appenders_list
        info_appenders = appenders_list
        warning_appenders = appenders_list
        error_appenders = appenders_list
        critical_appenders = appenders_list
    
    debug = DebugLogger(debug_appenders)
    info = InfoLogger(info_appenders)
    warning = WarningLogger(warning_appenders)
    error = ErrorLogger(error_appenders)
    critical = CriticalLogger(critical_appenders)
    
    # Chain them together: DEBUG -> INFO -> WARNING -> ERROR -> CRITICAL
    debug.set_next_logger(info).set_next_logger(warning).set_next_logger(error).set_next_logger(critical)
    
    return debug
