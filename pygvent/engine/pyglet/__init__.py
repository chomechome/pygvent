import logging

import pyglet

from pygvent.engine.abstract import GameEngine
from pygvent.engine.pyglet.display import PygletDisplay
from pygvent.engine.pyglet.font import PygletFont
from pygvent.engine.pyglet.keystate import PygletKeyState
from pygvent.engine.pyglet.loop import PygletLoop
from pygvent.engine.pyglet.picture import PygletPicture
from pygvent.input.keys import Keyboard
from pygvent.types import FrameRate

logger = logging.getLogger(__name__)


class PygletEngine(GameEngine):
    def __init__(self):
        super().__init__()

        self._window: pyglet.window.Window = None
        self._keys: pyglet.window.key.KeyStateHandler = None

    def __enter__(self):
        logger.debug('Initializing pyglet')

        self._window = pyglet.window.Window()
        self._keys = pyglet.window.key.KeyStateHandler()
        self._window.push_handlers(self._keys)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        logger.debug('Exiting pyglet')

        self._window: pyglet.window.Window = None
        self._keys: pyglet.window.key.KeyStateHandler = None

    def get_picture(self, path: str):
        image = pyglet.image.load(path)
        return PygletPicture(image)

    def get_font(self, path: str):
        return PygletFont(path)

    def get_display(self):
        return PygletDisplay(self._window)

    def get_keyboard(self):
        return Keyboard(PygletKeyState(self._keys), PygletKeyState(self._keys))

    def get_loop(self, rate: FrameRate):
        return PygletLoop(rate, self._window)
