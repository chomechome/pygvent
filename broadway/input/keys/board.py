from broadway.input.keys.key import Key
from broadway.input.keys.state import IKeyState


class Keyboard:
    def __init__(self, previous: IKeyState, current: IKeyState):
        self._previous = previous
        self._current = current

    def update(self):
        self._previous, self._current = self._current, self._previous
        self._current.update()

    def is_up(self, key: Key) -> bool:
        return self._current.is_up(key)

    def is_down(self, key: Key) -> bool:
        return self._current.is_down(key)

    def is_pressed(self, key: Key) -> bool:
        return self._current.is_down(key) and self._previous.is_up(key)

    def is_released(self, key: Key) -> bool:
        return self._current.is_up(key) and self._previous.is_down(key)

    def is_any_pressed(self) -> bool:
        return any(self.is_pressed(key) for key in Key)
