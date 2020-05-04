import abc

from pygvent.geometry import Point
from pygvent.resolution import Resolution
from pygvent.types import Degrees


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
