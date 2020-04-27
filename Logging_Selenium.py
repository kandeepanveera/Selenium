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
                    format='%(asctime)s: %(levelname)s: %(message)s',level=logging.DEBUG)# format for messages will will pring with time date ,level for to print form debug and infom messages

logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")
