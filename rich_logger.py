# rich_logger.py

import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.text import Text

class CustomRichHandler(RichHandler):
    def emit(self, record: logging.LogRecord) -> None:
        """Emit a log record."""
        text = self.format(record)
        log_style = STYLES.get(record.levelname, "")

        message = Text.from_markup(text, style=log_style)
        self.console.print(message)

# Define custom log levels as a dictionary for easy expansion
LEVELS = {
    'VERBOSE': 5,
    'DEBUG': 10,
    'DEPRECATED': 15,
    'INFO': 20,
    'ATTENTION': 25,
    'SUCCESS': 28,
    'WARNING': 30,
    'ERROR': 40,
    'CRITICAL': 50
}

# Define corresponding styles for each log level
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

for level_name, level_value in LEVELS.items():
    logging.addLevelName(level_value, level_name)

def get_logger(name="rich_custom", level=LEVELS['INFO']):
    """Return a logger instance set up with the custom rich handler."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.hasHandlers():
        logger.addHandler(CustomRichHandler())

    # Add the levels as attributes of the logger
    for level_name, level_value in LEVELS.items():
        setattr(logger, level_name, level_value)

    return logger

# This ensures that if someone imports this module, the logger is already set up.
logger = get_logger()
