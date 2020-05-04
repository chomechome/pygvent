from pygvent.action.abstract import IAction
from pygvent.types import Seconds


class Parallel(IAction):
    def __init__(self, *actions: IAction):
        assert actions

        self._actions = actions

    @property
    def is_done(self):
        return all(action.is_done for action in self._actions)

    def start(self):
        for action in self._actions:
            action.start()

    def update(self, elapsed: Seconds) -> Seconds:
        if not self.is_done:
            elapsed = min(action.update(elapsed) for action in self._actions)

        return elapsed
