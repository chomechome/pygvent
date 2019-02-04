from typing import Callable

from broadway.action import InstantAction


class Call(InstantAction):
    def __init__(self, function: Callable[..., None], *args, **kwargs):
        super().__init__()
        self._function = function
        self._args = args
        self._kwargs = kwargs

    def do(self):
        self._function(*self._args, **self._kwargs)
