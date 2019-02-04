import abc

from broadway.geometry import Point
from broadway.resolution import Resolution
from broadway.types import Degrees


class IPicture(metaclass=abc.ABCMeta):
    __slots__ = ()

    @property
    @abc.abstractmethod
    def resolution(self) -> Resolution:
        pass

    @abc.abstractmethod
    def draw(self, position: Point):
        pass

    @abc.abstractmethod
    def scale(self, resolution: Resolution):
        pass

    @abc.abstractmethod
    def rotate(self, angle: Degrees):
        pass

    @abc.abstractmethod
    def copy(self):
        pass
