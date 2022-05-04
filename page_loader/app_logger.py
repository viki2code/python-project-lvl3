import logging

_LOG_FORMAT = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"


def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.ERROR)
    stream_handler.setFormatter(logging.Formatter(_LOG_FORMAT))
    return stream_handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.addHandler(get_stream_handler())
    return logger
