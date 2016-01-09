# coding=utf-8
from pygvent.events import Event
from collections import namedtuple
from pygvent.objects import VisibleGameObject


class Button(VisibleGameObject):
    class State(object):
        IDLE = 'idle'
        SELECTED = 'selected'
        PRESSED = 'pressed'
        DESELECTED = 'deselected'

    Images = namedtuple('ButtonImages', [State.IDLE, State.SELECTED,
                                         State.PRESSED, State.DESELECTED])

    def __init__(self, position, images, state=State.IDLE, **kwargs):
        """

        :type images: core.controls.Button.Images
        :type state: str
        """
        super(Button, self).__init__(position, **kwargs)
        self.images = images
        self.state = state
        self.new_state = self.state
        self.image = getattr(self.images, self.state)
        self.on_press = Event()

    def update(self):
        if self._is_enabled and self.new_state is not self.state:
            self.state = self.new_state
            self.image = getattr(self.images, self.state)
            if self.state is Button.State.PRESSED:
                self.on_press()


class TopDownMenu(VisibleGameObject):
    def __init__(self, position, **kwargs):
        super(TopDownMenu, self).__init__(position, **kwargs)
        self._index = -1
        self._buttons = []

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

    def add_button(self, button):
        self._buttons.append(button)

    def remove_button(self, button):
        if button in self._buttons:
            self._buttons.remove(button)

    def draw(self, screen):
        if self._is_visible:
            for button in self._buttons:
                button.draw(screen)

    def move(self, offset):
        super(TopDownMenu, self).move(offset)
        for button in self._buttons:
            button.move(offset)

    def update(self):
        for button in self._buttons:
            button.update()

    def move_up(self):
        self._buttons[self.index].new_state = Button.State.DESELECTED
        self.index -= 1
        self._buttons[self.index].new_state = Button.State.SELECTED

    def move_down(self):
        self._buttons[self.index].new_state = Button.State.DESELECTED
        self.index += 1
        self._buttons[self.index].new_state = Button.State.SELECTED

    def select(self):
        if 0 <= self.index < len(self._buttons):
            self._buttons[self.index].new_state = Button.State.PRESSED
