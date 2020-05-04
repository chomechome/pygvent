import abc
import logging

from pygvent.display import IDisplay
from pygvent.engine import GameEngine, PygameEngine
from pygvent.resolution import Resolution, HD
from pygvent.structure import Scene
from pygvent.types import FrameRate


class Game(metaclass=abc.ABCMeta):
    def __init__(self,
                 caption: str = 'Game',
                 resolution: Resolution = HD,
                 rate: FrameRate = 60,
                 engine: GameEngine = None,
                 verbose: bool = False,
                 ):
        self.caption = caption
        self.resolution = resolution
        self.rate = rate

        self.engine: GameEngine = engine or PygameEngine()
        self.display: IDisplay = None

        if verbose:
            logging.basicConfig(
                format='%(levelname)s : {} : %(message)s'.format(self.caption),
                level=logging.DEBUG,
            )

    def run(self):
        with self.engine as engine:
            self.display = engine.get_display()

            self.display.set_caption(self.caption)
            self.display.set_resolution(self.resolution)

            try:
                scene = self.load()
                loop = engine.get_loop(self.rate)
                loop.run(scene)
            finally:
                self.display: IDisplay = None

    @abc.abstractmethod
    def load(self) -> Scene:
        pass
