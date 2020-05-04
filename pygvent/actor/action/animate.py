from pygvent.action import IntervalAction
from pygvent.actor import Actor
from pygvent.animation import Animation
from pygvent.types import Seconds


class Animate(IntervalAction):
    def __init__(self, target: Actor, animation: Animation):
        super().__init__(animation.duration)

        self._target = target
        self._animation = animation

        self._index = 0
        self._frame_duration: Seconds = self._frame.duration

    @property
    def _frame(self):
        return self._animation[self._index]

    def start(self):
        super().start()

        self._index = 0
        self._frame_duration: Seconds = self._frame.duration

    def do(self, elapsed: Seconds):
        self._frame_duration -= elapsed

        while self._frame_duration <= 0:
            self._index += 1
            if self._index < len(self._animation):
                frame = self._frame
                self._frame_duration += frame.duration
                self._target.image = frame.image
