import abc

from broadway.display import IDisplay
from broadway.picture import IPicture
from broadway.font import IFont
from broadway.input.keys import Keyboard
from broadway.loop import IGameLoop
from broadway.types import FrameRate


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
        pass

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
