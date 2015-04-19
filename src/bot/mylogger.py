from colorlog import ColoredFormatter
import logging

colored_formatter = ColoredFormatter(
    '%(log_color)s%(asctime)s %(name)s %(bold)s%(log_color)s%(levelname)s %(reset)s%(log_color)s%(message)s',
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    },
    secondary_log_colors={},
    style='%'
)


class SimpleHandler(logging.Handler):
    def emit(self, record: logging.LogRecord):
        print(self.format(record))


static_handler = SimpleHandler(logging.INFO)
static_handler.setFormatter(colored_formatter)


def get_logger(name: str, log_level: int=logging.INFO,
               handler: logging.Handler=static_handler,
               formatter: logging.Formatter=colored_formatter):
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    if len(logger.handlers) is 0:
        logger.addHandler(handler)
    if formatter is not None and handler is not static_handler:
        handler.setFormatter(formatter)
    return logger