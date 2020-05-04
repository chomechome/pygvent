import collections
import enum

from pygvent.event import Event
from pygvent.actor import Actor


class Button(Actor):

    class State(str, enum.Enum):
        IDLE = 'idle'
        SELECTED = 'selected'
        PRESSED = 'pressed'

    Images = collections.namedtuple('ButtonImages',
                                    [State.IDLE.value, State.SELECTED.value,
                                     State.PRESSED.value])

    def __init__(self, images: Images, *args,
                 state: State = State.IDLE, **kwargs):
        super(Button, self).__init__(*args, **kwargs)

        self._state = state
        self._new_state = state

        self.images = images
        self.image = getattr(self.images, self._state)
        self.on_press = Event()

    def select(self):
        self._new_state = self.State.SELECTED

    def deselect(self):
        self._new_state = self.State.IDLE

    def press(self):
        self._new_state = self.State.PRESSED

    def update(self):
        if self._is_enabled and self._new_state is not self._state:
            self._state = self._new_state
            self.image = getattr(self.images, self._state)
            if self._state is self.State.PRESSED:
                self.on_press()
