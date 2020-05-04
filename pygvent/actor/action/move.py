from pygvent.action import IntervalAction, IReversible
from pygvent.actor import Actor
from pygvent.geometry import Vector
from pygvent.types import Seconds


class Move(IntervalAction):
    def __init__(self,
                 target: Actor,
                 velocity: Vector,
                 acceleration: Vector,
                 **kwargs
                 ):
        super().__init__(**kwargs)
        self._target = target
        self._velocity = velocity
        self._acceleration = acceleration

    def do(self, elapsed: Seconds):
        offset = (self._velocity + elapsed / 2 * self._acceleration) * elapsed
        self._velocity += self._acceleration * elapsed
        self._target.transform.translate(offset)


class MoveBy(IntervalAction, IReversible):
    def __init__(self,
                 target: Actor,
                 direction: Vector,
                 **kwargs
                 ):
        super().__init__(**kwargs)
        self._target = target
        self._direction = direction

    def do(self, elapsed: Seconds):
        offset = self._direction * (elapsed / self._duration)
        self._target.transform.translate(offset)

    def reversed(self):
        return MoveBy(self._target, -self._direction, duration=self._duration)
