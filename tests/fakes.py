import unittest.mock

from broadway.action.instant.abstract import InstantAction
from broadway.action.interval.abstract import IntervalAction
from broadway.actor import Actor
from broadway.geometry import Point
from broadway.input.keys import Key, IKeyState
from broadway.types import Seconds


class FakeActor(Actor):
    def __init__(self, position: Point = None, **kwargs):
        super().__init__(anchor=position or Point.zeros(), **kwargs)


class FakeInstantAction(InstantAction):
    def __init__(self):
        super().__init__()

        self.do = unittest.mock.Mock(side_effect=self.do)

    def do(self):
        pass


class FakeIntervalAction(IntervalAction):
    def __init__(self, duration: Seconds = 1):
        super().__init__(duration=duration)

        self.start = unittest.mock.Mock(side_effect=self.start)
        self.do = unittest.mock.Mock(side_effect=self.do)

    def do(self, elapsed: Seconds):
        pass


class FakeKeyState(IKeyState):
    def __init__(self):
        self.mapping = {key: False for key in Key}

        self.update = unittest.mock.Mock(side_effect=self.update)

    def is_up(self, key: Key) -> bool:
        return not self.mapping[key]

    def is_down(self, key: Key) -> bool:
        return self.mapping[key]

    def update(self):
        pass
