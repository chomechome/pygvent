import pygame
import logging
import pygame.constants
from lazy import lazy
from pygvent.events import Event
from pygvent.keyboard import KeyboardState, Keyboard


class PyGameEngine(object):
    def __init__(self, name, resolution):
        self.name = name
        self.resolution = resolution

    def __enter__(self):
        logging.debug('Initializing pygame')

        pygame.init()
        pygame.display.set_caption(self.name)
        pygame.display.set_mode(self.resolution)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        logging.debug('Exiting pygame')

        pygame.quit()

    def __getattr__(self, item):
        return getattr(pygame, item)

    @property
    def screen(self):
        return pygame.display.get_surface

    @property
    def keyboard(self):
        return PyGameKeyboard

    @property
    def image(self):
        return PyGameImage

    @property
    def sound(self):
        return PyGameSound

    @property
    def clock(self):
        return self.time.Clock

    @lazy
    def time(self):
        return PyGameTime()


class PyGameKeyboardState(KeyboardState):
    def get_new_state(self):
        return pygame.key.get_pressed()


class PyGameKeys(list):
    def __getattr__(self, item):
        if item.startswith('K_'):
            key_id = getattr(pygame.constants, item, None)
            if key_id is not None:
                return self[key_id]
        raise AttributeError("No key with name {}".format(item))


class PyGameKeyboard(Keyboard):
    def __init__(self):
        super(PyGameKeyboard, self).__init__(PyGameKeyboardState())

    @lazy
    def keys(self):
        return PyGameKeys(self.new_state.keys)


class PyGameClock(object):
    def __init__(self, *args, **kwargs):
        self._clock = pygame.time.Clock(*args, **kwargs)
        self.on_tick = Event()

    def __getattr__(self, item):
        return getattr(self._clock, item)

    def tick(self, *args, **kwargs):
        self._clock.tick(*args, **kwargs)
        self.on_tick()


class PyGameTime(object):
    def __getattr__(self, item):
        return getattr(pygame.time, item)

    Clock = PyGameClock


class PyGameImage(object):
    def __new__(cls, filename):
        return cls.load(filename)

    def __getattr__(self, item):
        return getattr(pygame.image, item)

    @staticmethod
    def load(filename):
        image = pygame.image.load(filename)
        if image.get_alpha() is None:
            return image.convert()
        return image.convert_alpha()


class PyGameSound(object):
    def __new__(cls, filename):
        return cls.load(filename)

    @staticmethod
    def load(filename):
        if not pygame.mixer or not pygame.mixer.get_init():
            raise pygame.error('Tried to load sound without initialized mixer')
        return pygame.mixer.Sound(filename)
