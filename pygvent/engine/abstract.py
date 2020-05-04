import abc

from pygvent.display import IDisplay
from pygvent.picture import IPicture
from pygvent.font import IFont
from pygvent.input.keys import Keyboard
from pygvent.loop import IGameLoop
from pygvent.types import FrameRate


class GameEngine(metaclass=abc.ABCMeta):
    def __enter__(self):
        """
        Initialize external resources here
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Release external resources here
        """

    @abc.abstractmethod
    def get_picture(self, path: str) -> IPicture:
        pass

    @abc.abstractmethod
    def get_font(self, path: str) -> IFont:
        pass

    @abc.abstractmethod
    def get_display(self) -> IDisplay:
        pass

    @abc.abstractmethod
    def get_keyboard(self) -> Keyboard:
        pass

    @abc.abstractmethod
    def get_loop(self, rate: FrameRate) -> IGameLoop:
        pass
