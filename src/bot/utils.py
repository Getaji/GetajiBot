__author__ = 'Margherita'


def range_some(n: int, x):
    """n回ぶんxを返すジェネレーターです。

    :param n: 回数
    :param x: 返す値
    :return: n回のx
    """
    for i in range(0, n):
        yield x


def is_integer(s: object):
    try:
        int(s)
        return True
    except ValueError:
        return False


def ternary(b: bool, obj_true: object, obj_false: object):
    return obj_true if b else obj_false


def shuffle_f(lis):
    from random import shuffle
    return shuffle(lis) or lis


def trim(text: str, from_begin: int=0, from_end: int=0):
    return text[from_begin:len(text) - from_end]


from logging import INFO


def get_logger(name: str, log_level: int=INFO):
    import logging
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    return logger