import pyglet

from pygvent.engine.pyglet.keystate import PygletKeyState
from pygvent.input.keys import Key
from tests.engine.pyglet.case import PygletTestCase


class PygletKeyStateTest(PygletTestCase):
    def setUp(self):
        super().setUp()
        keys = pyglet.window.key.KeyStateHandler()
        self.window.push_handlers(keys)
        self.state = PygletKeyState(keys)

    def test_key_codes(self):
        for key in Key:
            with self.subTest(key=key):
                self.assertIn(key, self.state._KEY_CODES)
