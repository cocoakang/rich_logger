# rich_logger.py

import logging
from enum import Enum
from rich.logging import RichHandler
from rich.text import Text

class LogLevel(Enum):
    VERBOSE = 5
    DEBUG = 10
    DEPRECATED = 15
    INFO = 20
    ATTENTION = 25
    SUCCESS = 28
    WARNING = 30
    ERROR = 40
    CRITICAL = 50

STYLES = {
    'VERBOSE': 'dim',
    'DEBUG': 'cyan',
    'DEPRECATED': 'magenta',
    'INFO': '',
    'ATTENTION': 'bold',
    'SUCCESS': 'green bold',
    'WARNING': 'yellow',
    'ERROR': 'red bold',
    'CRITICAL': 'on red bold white'
}

for level_name, level_value in LogLevel.__members__.items():
    logging.addLevelName(level_value.value, level_name)

class CustomRichHandler(RichHandler):
    def emit(self, record: logging.LogRecord) -> None:
        """Emit a log record."""
        text = self.format(record)
        log_style = STYLES.get(record.levelname, "")
        message = Text.from_markup(text, style=log_style)
        self.console.print(message)

class RichLogger(logging.Logger):
    def __init__(self, name, level=LogLevel.INFO.value):
        super().__init__(name, level)
        if not self.hasHandlers():
            self.addHandler(CustomRichHandler())

    def verbose(self, message, *args, **kwargs):
        self.log(LogLevel.VERBOSE.value, message, *args, **kwargs)

    def debug(self, message, *args, **kwargs):
        self.log(LogLevel.DEBUG.value, message, *args, **kwargs)

    def deprecated(self, message, *args, **kwargs):
        self.log(LogLevel.DEPRECATED.value, message, *args, **kwargs)

    def info(self, message, *args, **kwargs):
        self.log(LogLevel.INFO.value, message, *args, **kwargs)

    def attention(self, message, *args, **kwargs):
        self.log(LogLevel.ATTENTION.value, message, *args, **kwargs)

    def success(self, message, *args, **kwargs):
        self.log(LogLevel.SUCCESS.value, message, *args, **kwargs)

    def warning(self, message, *args, **kwargs):
        self.log(LogLevel.WARNING.value, message, *args, **kwargs)

    def error(self, message, *args, **kwargs):
        self.log(LogLevel.ERROR.value, message, *args, **kwargs)

    def critical(self, message, *args, **kwargs):
        self.log(LogLevel.CRITICAL.value, message, *args, **kwargs)

    def done(self):
        self.info("done.")

# Setting the logger class to our custom logger
logging.setLoggerClass(RichLogger)

def get_logger(name="rich_custom", level=LogLevel.INFO.value):
    return logging.getLogger(name)

# This ensures that if someone imports this module, the logger is already set up.
logger = get_logger()
