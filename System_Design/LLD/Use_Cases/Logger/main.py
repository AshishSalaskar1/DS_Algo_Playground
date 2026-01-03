import sys
import os
import time

# # Add src directory to path
# sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.log_level import LogLevel
from src.log_appender import ConsoleLogAppender, FileLogAppender
from src.log_formatter import SimpleLogFormatter
from src.logger import Logger
from src.logger_chain import create_logger_chain

console_appender = ConsoleLogAppender()  # Uses default SimpleLogFormatter
logger = Logger("SimpleApp", level=LogLevel.WARNING)  # Set minimum level to DEBUG
logger.add_appender(console_appender)

logger.log(LogLevel.DEBUG, "This is a debug message")
logger.log(LogLevel.INFO, "Application started successfully")
logger.log(LogLevel.WARNING, "Low memory warning")
logger.log(LogLevel.ERROR, "Database connection failed")
logger.log(LogLevel.CRITICAL, "System shutdown initiated")
