from pygvent.actor import Actor
from pygvent.geometry import Vector
from pygvent.input.keys import Key, Keyboard
from pygvent.types import Seconds


class Player(Actor):

    _SPEED = 6

    def __init__(self, keyboard: Keyboard, **kwargs):
        super().__init__(**kwargs)

        self._keyboard = keyboard

    def update(self, elapsed: Seconds):
        self._handle_input()

        super().update(elapsed)

    def _handle_input(self):
        keyboard = self._keyboard

        if keyboard.is_down(Key.A):
            self._move_left()
        if keyboard.is_down(Key.D):
            self._move_right()
        if keyboard.is_down(Key.SPACE):
            self._shoot()

    def _move_left(self):
        offset = Vector(-self._SPEED, 0)
        self.transform.translate(offset)

    def _move_right(self):
        offset = Vector(self._SPEED, 0)
        self.transform.translate(offset)

    def _shoot(self):
        pass
