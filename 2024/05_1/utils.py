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
    suppress_debug = os.getenv("NO_DEBUG", "") != ""
    debug_level = "INFO" if suppress_debug else "DEBUG"

    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "info": {
                "format": "%(message)s",
            },
            "debug": {
                "format": "%(asctime)s: %(message)s",
                "datefmt": "%H:%M:%S",
            },
        },
        "handlers": {
            "info_handler": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "info",
                "stream": "ext://sys.stdout",
            },
            "debug_handler": {
                "class": "logging.StreamHandler",
                "level": debug_level,
                "formatter": "debug",
                "stream": "ext://sys.stdout",
            },
        },
        "root": {
            "level": "DEBUG",
            "handlers": ["info_handler", "debug_handler"],
        },
    }

    logging.config.dictConfig(config)
    return logging.getLogger()


log = setup_logger()
