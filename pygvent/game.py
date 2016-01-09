# coding=utf-8
import logging
from abc import abstractmethod, ABCMeta
from pygvent.engine import PyGameEngine
from pygvent.display import Resolution


class Game(object):
    __metaclass__ = ABCMeta

    BASE_FRAME_RATE = 60

    def __init__(self, name, resolution=Resolution.HD,
                 frame_rate=BASE_FRAME_RATE, verbose=False):
        self.name = name
        self.resolution = resolution
        self.frame_rate = frame_rate

        self.is_running = False
        self.engine = None
        self.screen = None
        self.clock = None
        self.keyboard = None

        if verbose:
            logging.basicConfig(
                format='%(levelname)s : {} : %(message)s'.format(self.name),
                level=logging.DEBUG
            )

    def create_engine(self):
        return PyGameEngine(self.name, self.resolution)

    def run(self):
        with self.create_engine() as engine:
            self.engine = engine
            self.screen = engine.screen()
            self.clock = engine.clock()
            self.keyboard = engine.keyboard()

            self._run_game()

            self.engine = None
            self.screen = None
            self.clock = None
            self.keyboard = None

    def stop(self):
        self.is_running = False

    def start(self):
        self.is_running = True

    @abstractmethod
    def _run_game(self):
        pass
