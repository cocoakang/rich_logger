from rich_logger import logger

# logger.log(logger.VERBOSE, "This is a very detailed log message.")
# logger.log(logger.DEBUG, "This is a debug message.")
# logger.log(logger.DEPRECATED, "This feature is deprecated.")
logger.info("This is a general information message.")
logger.attention( "This message requires your attention.")
logger.success("Operation completed successfully!")
logger.warning("This is a warning message.")
logger.error("An error has occurred.")
logger.critical("Critical system failure!")
logger.done()
