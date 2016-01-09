# coding=utf-8
from collections import namedtuple
from pygvent.objects import VisibleGameObject
from utils.image import convert_to_mask


class Asteroid(VisibleGameObject):
    class State(object):
        NORMAL = 'normal'
        DESTROYED = 'destroyed'

    Images = namedtuple('AsteroidImages', [State.NORMAL, State.DESTROYED])

    def __init__(self, position, images, **kwargs):
        super(Asteroid, self).__init__(position, **kwargs)
        self.images = images
        self.state = Asteroid.State.NORMAL
        self.image = getattr(self.images, self.state)
        self.mask = convert_to_mask(self.image)
        self.speed = 6

        self._destroyed_animation_frames = 10
        self._is_destroyed = False

    def draw(self, screen):
        if self.has_left_screen(screen):
            self.kill()
        else:
            super(Asteroid, self).draw(screen)

    def has_left_screen(self, screen):
        height, _ = screen.get_size()
        return self.rect.y - self.rect.height >= height

    def update(self):
        if self._is_destroyed:
            if self._destroyed_animation_frames == 0:
                self.kill()
            else:
                self._destroyed_animation_frames -= 1
        elif self._is_enabled:
            self.move((0, self.speed))

            if self.state is Asteroid.State.DESTROYED:
                self.image = getattr(self.images, self.state)
                self._is_destroyed = True
