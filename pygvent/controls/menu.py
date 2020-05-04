from typing import Iterable

from pygvent.controls.button import Button
from pygvent.actor import Actor


class TopDownMenu(Actor):
    def __init__(self, *args, buttons: Iterable[Button] = (), **kwargs):
        super().__init__(*args, **kwargs)
        self._index = -1
        self._buttons = list(buttons)

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        if value < 0:
            value = len(self._buttons) - 1
        elif value >= len(self._buttons):
            value = 0
        self._index = value

    def add(self, button: Button):
        self._buttons.append(button)

    def remove(self, button: Button):
        self._buttons.remove(button)

    def draw(self, screen):
        for button in self._buttons:
            button.draw(screen)

    def move(self, offset):
        super(TopDownMenu, self).move(offset)
        for button in self._buttons:
            button.move(offset)

    def update(self):
        for button in self._buttons:
            button.update()

    def select(self):
        if 0 <= self.index < len(self._buttons):
            self._buttons[self.index].press()

    def up(self):
        self._shift(-1)

    def down(self):
        self._shift(1)

    def _shift(self, offset: int):
        self._buttons[self.index].deselect()
        self._index += offset
        self._buttons[self.index].select()
