import abc

from broadway.action.abstract import IAction
from broadway.types import Seconds


class IntervalAction(IAction):
    def __init__(self, duration: Seconds):
        assert duration > 0

        self._duration = duration
        self._elapsed = 0

    @property
    def is_done(self) -> bool:
        return self._elapsed >= self._duration

    @property
    def progress(self) -> float:
        return min(1, self._elapsed / self._duration)

    def start(self):
        self._elapsed = 0

    def update(self, elapsed: Seconds) -> Seconds:
        if self.is_done:
            return elapsed

        overtime = max(0, self._elapsed + elapsed - self._duration)
        elapsed -= overtime

        self._elapsed += elapsed
        self.do(elapsed)

        return overtime

    @abc.abstractmethod
    def do(self, elapsed: Seconds):
        pass
