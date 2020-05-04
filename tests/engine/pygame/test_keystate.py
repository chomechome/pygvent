from pygvent.engine.pygame import PygameKeyState
from pygvent.input.keys import Key
from tests.engine.pygame.case import PygameTestCase


class PygameKeyStateTest(PygameTestCase):
    def setUp(self):
        super().setUp()
        self.state = PygameKeyState()

    def test_key_codes(self):
        for key in Key:
            with self.subTest(key=key):
                self.assertIn(key, self.state._KEY_CODES)
