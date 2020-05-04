from pygvent.action.abstract import IAction
from pygvent.types import Seconds


class Loop(IAction):
    def __init__(self, action: IAction, iterations: int):
        self._action = action
        self._iterations = iterations

        self._iterated = 0

    @property
    def is_done(self):
        return self._iterated == self._iterations

    def start(self):
        self._iterated = 0
        self._action.start()

    def update(self, elapsed: Seconds) -> Seconds:
        action = self._action

        while elapsed > 0 and not self.is_done:
            elapsed = action.update(elapsed)
            if action.is_done:
                self._iterated += 1
                if not self.is_done:
                    action.start()

        return elapsed
