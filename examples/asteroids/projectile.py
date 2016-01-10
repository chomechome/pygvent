# coding=utf-8
from pygvent.objects import VisibleGameObject
from pygvent.utils.image import convert_to_mask


class Projectile(VisibleGameObject):
    def __init__(self, position, image, **kwargs):
        super(Projectile, self).__init__(position, image,
                                         convert_to_mask(image), **kwargs)
        self.speed = 10

    def draw(self, screen):
        if self.has_left_screen():
            self.kill()
        else:
            super(Projectile, self).draw(screen)

    def has_left_screen(self):
        return self.rect.y < 0

    def update(self):
        if self._is_enabled:
            self.move((0, -self.speed))
