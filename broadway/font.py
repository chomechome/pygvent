import abc

from broadway.color import Color
from broadway.picture import IPicture


class IFont(metaclass=abc.ABCMeta):
    __slots__ = ()

    @abc.abstractmethod
    def render(self, text: str, size: int, color: Color.RGBA) -> IPicture:
        pass
