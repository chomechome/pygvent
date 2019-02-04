import random

from broadway.action.interval.abstract import IntervalAction
from broadway.types import Seconds


class Delay(IntervalAction):
    @classmethod
    def random(cls, minimum: Seconds, maximum: Seconds):
        return cls(duration=random.uniform(minimum, maximum))

    def do(self, elapsed: Seconds):
        pass
