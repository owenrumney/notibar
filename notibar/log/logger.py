# logger has the code for logging errors and info to a file
import logging

def setup_logger():
    logging.basicConfig(filename='/var/log/notibar.log', level=logging.INFO)
    return logging.getLogger('notibar')

logger = setup_logger()

def log_error(message):
    logger.error(message)

def log_info(message):
    logger.info(message)