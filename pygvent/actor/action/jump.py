import math

from pygvent.action import IntervalAction, IReversible
from pygvent.actor import Actor
from pygvent.geometry import Point, Vector
from pygvent.types import Seconds


class JumpBy(IntervalAction, IReversible):
    def __init__(self,
                 target: Actor,
                 direction: Vector,
                 height: float,
                 *args,
                 jumps: int = 1,
                 **kwargs
                 ):
        super().__init__(*args, **kwargs)

        self._target = target
        self._direction = direction
        self._height = height
        self._jumps = jumps

        self._position = Point.zeros()

    def start(self):
        super().start()

        self._position = Point.zeros()

    def do(self, elapsed: Seconds):
        progress = self.progress
        factor = abs(math.sin(progress * math.pi * self._jumps))
        x = self._direction.x * progress
        y = self._direction.y * progress + self._height * factor
        position = Point(x, y)

        offset = position - self._position
        self._target.transform.translate(offset)
        self._position = position

    def reversed(self):
        return JumpBy(self._target, -self._direction, self._height,
                      jumps=self._jumps, duration=self._duration)
