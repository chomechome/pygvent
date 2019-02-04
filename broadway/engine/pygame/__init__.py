import logging

import pygame

from broadway.engine.abstract import GameEngine
from broadway.engine.pygame.display import PygameDisplay
from broadway.engine.pygame.font import PygameFont
from broadway.engine.pygame.keystate import PygameKeyState
from broadway.engine.pygame.loop import PygameLoop
from broadway.engine.pygame.picture import PygamePicture
from broadway.input.keys import Keyboard
from broadway.types import FrameRate

logger = logging.getLogger(__name__)


class PygameEngine(GameEngine):
    def __init__(self):
        self._screen: pygame.Surface = None
        self._keyboard: Keyboard = None

    def __enter__(self):
        logger.debug('Initializing pygame')

        pygame.init()
        pygame.display.set_mode((1, 1))
        self._screen = pygame.display.get_surface()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        logger.debug('Exiting pygame')

        self._screen = None
        pygame.quit()

    def get_picture(self, path: str):
        image = pygame.image.load(path)
        return PygamePicture(self._screen, image)

    def get_font(self, path: str):
        return PygameFont(self._screen, path)

    def get_display(self):
        return PygameDisplay(self._screen)

    def get_keyboard(self):
        return Keyboard(previous=PygameKeyState(), current=PygameKeyState())

    def get_loop(self, rate: FrameRate):
        return PygameLoop(rate)
