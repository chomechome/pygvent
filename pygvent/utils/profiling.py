import logging
import time

logger = logging.getLogger(__name__)


def timing(function):
    name = '{}.{}'.format(function.__module__, function.__name__)

    def timed(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        elapsed = time.time() - start
        print("'{}' took {:.4f} seconds".format(name, elapsed))
        return result

    return timed
