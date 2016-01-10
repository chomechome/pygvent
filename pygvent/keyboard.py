from abc import abstractmethod, ABCMeta
from pygvent.events import Event
from lazy import lazy


class Key(int):
    def __new__(cls, key_id):
        key = super(Key, cls).__new__(cls, key_id)
        key.on_down = Event()
        key.on_press = Event()
        key.on_release = Event()
        return key


class KeyboardState(list):
    """
    Abstract bitmap keyboard state, stores True if key is down
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        super(KeyboardState, self).__init__(self.get_new_state())

    @lazy
    def keys(self):
        """

        :rtype: list[Key]
        """
        return [Key(key_id) for key_id in range(len(self))]

    @abstractmethod
    def get_new_state(self):
        return []

    def update(self):
        self.__init__()

    def copy(self):
        """
        Create an empty state instance, then initialize it with current state
        :rtype: KeyboardState
        """
        copy = super(KeyboardState, self).__new__(type(self))
        super(KeyboardState, copy).__init__(self)
        return copy

    def is_down(self, key):
        return self[key]

    def is_up(self, key):
        return not self[key]

    def is_any_down(self):
        return any(self.is_down(key) for key in self.keys)


class Keyboard(object):
    def __init__(self, keyboard_state):
        """

        :type keyboard_state: KeyboardState
        """
        self.old_state = keyboard_state
        self.new_state = self.old_state

    def __iter__(self):
        return iter(self.keys)

    @property
    def keys(self):
        return self.new_state.keys

    def update(self):
        self.old_state = self.new_state.copy()
        self.new_state.update()

    def is_up(self, key):
        return self.new_state.is_up(key)

    def is_down(self, key):
        return self.new_state.is_down(key)

    def is_any_down(self):
        return self.new_state.is_any_down()

    def is_pressed(self, key):
        return self.new_state.is_down(key) and self.old_state.is_up(key)

    def is_released(self, key):
        return self.old_state.is_down(key) and self.new_state.is_up(key)

    def is_any_pressed(self):
        return any(self.is_pressed(key) for key in self.keys)

    def handle_events(self):
        for key in self.keys:
            if self.is_down(key):
                key.on_down()
            if self.is_pressed(key):
                key.on_press()
            if self.is_released(key):
                key.on_release()
