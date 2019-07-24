import logging


def get_logger():
    formatter = '%(asctime)s %(levelname)-8s %(filename)s:%(lineno)-4d %(message)-80s'
    logging.basicConfig(format=formatter, datefmt='%m/%d/%Y %T')
    return logging.getLogger(__name__)
