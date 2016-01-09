# coding=utf-8
from pygvent.objects import VisibleGameObject


class Score(VisibleGameObject):
    def __init__(self, font, color, message, position, **kwargs):
        super(Score, self).__init__(position, **kwargs)
        self.font = font
        self.color = color
        self.message = message
        self.value = 0

    def update(self):
        if self._is_enabled:
            message = '{}: {}'.format(self.message, self.value)
            self.image = self.font.render(message, 0, self.color)

    def increase(self, value):
        self.value += value
