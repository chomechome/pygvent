import functools
from typing import Callable

import pyglet

from pygvent.color import Color
from pygvent.geometry import Point
from pygvent.picture import IPicture
from pygvent.resolution import Resolution


class PygletLabel(IPicture):
    def __init__(self,
                 font: str, 
                 size: int,
                 text: str,
                 color: Color.RGBA,
                 ):
        self._get_label: Callable[..., pyglet.text.Label] = functools.partial(
            pyglet.text.Label,
            text=text,
            font_name=font,
            font_size=size,
            color=color,
        )
        self._label: pyglet.text.Label = None

    @property
    def resolution(self):
        if self._label is None:
            self._label = self._get_label()

        return Resolution(
            self._label.content_width,
            self._label.content_height,
        )

    def draw(self, position: Point):
        x = position.x
        y = position.y
        label = self._label

        if label is None or label.x != x or label.y != y:
            self._label = self._get_label(x=x, y=y)
        self._label.draw()
