from .log_level import LogLevel
from .log_message import LogMessage
from .log_appender import LogAppender, ConsoleLogAppender, FileLogAppender
from .log_formatter import LogFormatter, SimpleLogFormatter
from .log_processor import LogProcessor, AsyncLogProcessor
from .logger_chain import AbstractLogger, create_logger_chain


class Logger:
    """
    Logger with Chain of Responsibility support.
    If logger_chain is provided, uses it. Otherwise creates default chain: DEBUG -> INFO -> WARNING -> ERROR -> CRITICAL
    Appenders should already have their formatters set.
    """
    _instance = None
    _isinitialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(
        self, 
        name: str, 
        appenders: list[LogAppender] = None,
        logger_chain: AbstractLogger = None,
        level: LogLevel = LogLevel.DEBUG
    ) -> None:
        
        if self._isinitialized:
            return
        
        self._isinitialized = True
        self.name = name
        self.processor = AsyncLogProcessor()
        self.appenders = appenders or []
        self.custom_chain = logger_chain
        self.level = level
        
        # Use provided chain OR create default chain with all levels using same appenders
        if logger_chain:
            self.logger_chain = logger_chain
        else:
            self.logger_chain = create_logger_chain(appenders_list=self.appenders)
    
    def log(self, level: LogLevel, message: str) -> None:
        """Log a message using Chain of Responsibility"""
        # Only log if the message level is >= the logger's minimum level
        if level.value >= self.level.value:
            self.logger_chain.log(level, message)
    
    def set_processor(self, processor: LogProcessor) -> None:
        """Set the log processor"""
        self.processor = processor
    
    def set_level(self, level: LogLevel) -> None:
        """Set the minimum log level"""
        self.level = level

    def add_appender(self, appender: LogAppender) -> None:
        """Add an appender and recreate the chain if using default chain"""
        self.appenders.append(appender)
        self.logger_chain = create_logger_chain(appenders_list=self.appenders)
    
    def remove_appender(self, appender: LogAppender) -> None:
        """Remove an appender and recreate the chain if using default chain"""
        self.logger_chain = create_logger_chain(appenders_list=self.appenders)


