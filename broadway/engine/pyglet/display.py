import pyglet

from broadway.display import IDisplay
from broadway.resolution import Resolution


class PygletDisplay(IDisplay):
    def __init__(self, window: pyglet.window.Window):
        self._window = window

        # pyglet on Windows sets new resolution incorrectly, so we need to
        # track it manually
        width, height = window.get_size()
        self._resolution = Resolution(width, height)

    def get_caption(self) -> str:
        return self._window.get_caption()

    def set_caption(self, name: str):
        self._window.set_caption(name)

    def get_resolution(self) -> Resolution:
        return self._resolution

    def set_resolution(self, resolution: Resolution):
        self._window.set_size(resolution.width, resolution.height)
        self._resolution = resolution

    def clear(self):
        self._window.clear()
