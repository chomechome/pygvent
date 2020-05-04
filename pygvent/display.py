import abc

from pygvent.resolution import Resolution


class IDisplay(metaclass=abc.ABCMeta):
    __slots__ = ()

    @abc.abstractmethod
    def get_caption(self) -> str:
        pass

    @abc.abstractmethod
    def set_caption(self, name: str):
        pass

    @abc.abstractmethod
    def get_resolution(self) -> Resolution:
        pass

    @abc.abstractmethod
    def set_resolution(self, resolution: Resolution):
        pass

    @abc.abstractmethod
    def clear(self):
        pass
