import unittest

from pygvent.input.keys import Key, Keyboard
from tests.fakes import FakeKeyState


class KeyboardTest(unittest.TestCase):
    def setUp(self):
        self.key = Key.ZERO
        self.previous = FakeKeyState()
        self.current = FakeKeyState()
        self.keyboard = Keyboard(previous=self.previous, current=self.current)

    def press(self):
        self.current.mapping[self.key] = True

    def release(self):
        self.previous.mapping[self.key] = True

    def test_is_up(self):
        self.assertTrue(self.keyboard.is_up(self.key))
        self.press()
        self.assertFalse(self.keyboard.is_up(self.key))

    def test_is_down(self):
        self.assertFalse(self.keyboard.is_down(self.key))
        self.press()
        self.assertTrue(self.keyboard.is_down(self.key))

    def test_is_pressed(self):
        self.assertFalse(self.keyboard.is_pressed(self.key))
        self.press()
        self.assertTrue(self.keyboard.is_pressed(self.key))

    def test_is_any_pressed(self):
        self.assertFalse(self.keyboard.is_any_pressed())
        self.press()
        self.assertTrue(self.keyboard.is_any_pressed())

    def test_is_released(self):
        self.assertFalse(self.keyboard.is_released(self.key))
        self.release()
        self.assertTrue(self.keyboard.is_released(self.key))

    def test_update(self):
        self.keyboard.update()

        self.assertIs(self.previous, self.keyboard._current)
        self.assertIs(self.current, self.keyboard._previous)
        self.previous.update.assert_called_once()
        self.current.update.assert_not_called()
