import time
import tests_data

from selenium.common.exceptions import TimeoutException


class Waiter:
    POLL_FREQUENCY = 0.5  # How long to sleep in between calls to the method
    IGNORED_EXCEPTIONS = (Exception,)  # exceptions ignored during calls to the method

    def __init__(self, obj=None, timeout=None, poll_frequency=None,
                 ignored_exceptions=IGNORED_EXCEPTIONS):
        self._obj = obj
        self._timeout = timeout if timeout is not None else tests_data.constants.TIMEOUT
        self._poll = poll_frequency or Waiter.POLL_FREQUENCY
        self._ignored_exceptions = ignored_exceptions

    def until(self, method, message=''):
        message = 'Wait {} seconds. {}\n'.format(self._timeout, message)
        last_exc = None
        end_time = time.time() + self._timeout
        while True:
            try:
                if self._obj:
                    value = method(self._obj)
                else:
                    value = method()
                if value:
                    return value
            except self._ignored_exceptions as exc:
                print('Exception {} {}'.format(type(exc), exc))
                last_exc = exc
            time.sleep(self._poll)
            if time.time() > end_time:
                break
        raise TimeoutException(message) from last_exc

    def until_not(self, method, message=''):
        """Calls the method provided with the driver as an argument until the \
        return value is False."""
        message = 'Wait {} seconds. {}\n'.format(self._timeout, message)
        end_time = time.time() + self._timeout
        while True:
            try:
                if self._obj:
                    value = method(self._obj)
                else:
                    value = method()
                if not value:
                    return value
            except self._ignored_exceptions as exc:
                print('Exception {} {}'.format(type(exc), exc))
                return True
            time.sleep(self._poll)
            if time.time() > end_time:
                break
        raise TimeoutException(message)


def wait_until(method, message='', obj=None, timeout=None, poll_frequency=None):
    return Waiter(obj, timeout, poll_frequency).until(method, message)

def wait_until_not(method, message='', obj=None, timeout=None, poll_frequency=None):
    return Waiter(obj, timeout, poll_frequency).until_not(method, message)