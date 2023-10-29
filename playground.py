from rich_logger import logger

logger.log(logger.INFO, "This is a general information message.")
logger.log(logger.ATTENTION, "This message requires your attention.")
logger.log(logger.SUCCESS, "Operation completed successfully!")
logger.log(logger.WARNING, "This is a warning message.")
logger.log(logger.ERROR, "An error has occurred.")
logger.log(logger.CRITICAL, "Critical system failure!")
