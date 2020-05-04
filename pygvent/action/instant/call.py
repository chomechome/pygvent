from typing import Callable

from pygvent.action import InstantAction


class Call(InstantAction):
    def __init__(self, func: Callable[..., None], *args, **kwargs):
        super().__init__()
        self._func = func
        self._args = args
        self._kwargs = kwargs

    def do(self):
        self._func(*self._args, **self._kwargs)
