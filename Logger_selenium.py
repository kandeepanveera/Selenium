"""
Logging
logging and log levels
-debug
-info
-warning
-error
-critical

datefmt='%m/%d/%Y %I:%M:%S %P'

"""
import logging
logging.basicConfig(filename="C://Users//kandeepx//Pictures//Camera Roll//test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s')# format for messages will will pring with time date ,level for to print form debug and infom messages

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is debug message")
logger.info("This is info message")
logger.warning("This is warning message")
logger.error("This is error message")
logger.critical("This is critical message")
