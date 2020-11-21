import time
import logging
time = time.strftime("%Y%m%d-%H%M%S")


def create_logger(dir_name):
    logging.basicConfig(level=logging.INFO, filename="./logs/logfile_" + time + ".log")
    logging.log(logging.INFO, "Started logging for " + dir_name)


def log(log_level, message):
    logging.log(log_level, message)
