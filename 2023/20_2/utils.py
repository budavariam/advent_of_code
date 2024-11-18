from time import perf_counter
import logging
import logging.config
import os


def profiler(method):
    def decorator_method(*arg, **kw):
        t = perf_counter()
        result = method(*arg, **kw)
        print(f"{method.__name__}: {perf_counter()-t:2.5f} sec")
        return result

    return decorator_method


def setup_logger():
    no_debug = os.getenv("NO_DEBUG", "") != ""  # default allow debug
    no_log = os.getenv("NO_LOG", "") != ""  # default allow logs

    logger = logging.getLogger()
    if no_log:
        logger.setLevel(logging.CRITICAL)
        return logger

    logger.setLevel(logging.INFO)
    info_handler = logging.StreamHandler()
    info_handler.setLevel(logging.INFO)
    info_handler.addFilter(lambda record: record.levelno == logging.INFO)
    info_formatter = logging.Formatter("%(message)s")
    info_handler.setFormatter(info_formatter)
    logger.addHandler(info_handler)
    if not no_debug:
        logger.setLevel(logging.DEBUG)
        debug_handler = logging.StreamHandler()
        debug_handler.setLevel(logging.DEBUG)
        debug_handler.addFilter(lambda record: record.levelno == logging.DEBUG)
        debug_formatter = logging.Formatter(
            "%(asctime)s: %(message)s", datefmt="%H:%M:%S"
        )
        debug_handler.setFormatter(debug_formatter)
        logger.addHandler(debug_handler)
    return logger


log = setup_logger()
