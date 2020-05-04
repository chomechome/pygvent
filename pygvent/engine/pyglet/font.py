from pygvent.color import Color
from pygvent.engine.pyglet import utils
from pygvent.engine.pyglet.label import PygletLabel
from pygvent.font import IFont


class PygletFont(IFont):
    def __init__(self, path: str):
        self._path = path

        self._name: str = None

    def render(self, text: str, size: int, color: Color.RGBA):
        if self._name is None:
            self._name = utils.add_font(self._path)

        return PygletLabel(self._name, size, text, color)
