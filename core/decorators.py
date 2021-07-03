import logging
import time

from selenium.common.exceptions import TimeoutException

import shared_vars


def retry(func):
    """ Decorator

    :param func: метод, который будет повторно исполняться в случае ошибки
    :return: возвращаемое значение метода или пустое значение
    """

    def func_wrapper(*args, **kwargs):

        end = time.time() + int(shared_vars.APPLICATION_PROPERTIES.get("timeout"))

        while end > time.time():
            try:
                return func(*args, **kwargs)
            except Exception as exc:
                logging.getLogger().debug(exc)

        raise TimeoutException(func)

    return func_wrapper
