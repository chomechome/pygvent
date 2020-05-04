import abc

from pygvent.action.abstract import IAction
from pygvent.types import Seconds


class InstantAction(IAction):
    def __init__(self):
        self._is_finished = False

    @property
    def is_done(self) -> bool:
        return self._is_finished

    def start(self):
        self._is_finished = False

    def update(self, elapsed: Seconds) -> Seconds:
        if not self._is_finished:
            self.do()
            self._is_finished = True

        return elapsed

    @abc.abstractmethod
    def do(self):
        pass
