from typing import Sequence

from broadway.action.abstract import IAction
from broadway.types import Seconds


class Chain(IAction):
    def __init__(self, *actions: Sequence[IAction]):
        assert actions

        self._actions = actions
        self._index = 0

    @property
    def is_done(self):
        return self._index == len(self._actions)

    @property
    def _current(self):
        return self._actions[self._index]

    def start(self):
        self._index = 0
        self._current.start()

    def update(self, elapsed: Seconds) -> Seconds:
        while elapsed > 0 and not self.is_done:
            action = self._current
            elapsed = action.update(elapsed)
            if action.is_done:
                self._index += 1
                if not self.is_done:
                    self._current.start()

        return elapsed
