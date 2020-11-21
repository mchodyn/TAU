import time
import logging
time = time.strftime("%Y%m%d-%H%M%S")


def create_logger():
    logging.basicConfig(level=logging.INFO, filename="./logs/logfile_" + time + ".log")
    logging.log(logging.INFO, "Running test")


def log(log_level, message):
    logging.log(log_level, time + ' ' + message)
