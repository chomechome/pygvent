import abc

from pygvent.input.keys.key import Key


class IKeyState(metaclass=abc.ABCMeta):
    __slots__ = ()

    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def is_up(self, key: Key) -> bool:
        pass

    @abc.abstractmethod
    def is_down(self, key: Key) -> bool:
        pass
