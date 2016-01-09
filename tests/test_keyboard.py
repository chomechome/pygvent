from unittest import TestCase
from pygvent.keyboard import Keyboard, KeyboardState


def get_test_state(iterable):
    class MockKeyboardState(KeyboardState):
        def get_new_state(self):
            return iterable

    return MockKeyboardState()


class KeyboardTest(TestCase):
    def setUp(self):
        self.test_state = [False for _ in range(6)]
        self.keyboard = Keyboard(get_test_state(self.test_state))

    def test_is_down(self):
        key_id = 1
        self.assertFalse(self.keyboard.old_state.is_down(key_id))
        self.assertFalse(self.keyboard.new_state.is_down(key_id))

        self.test_state[key_id] = True
        self.keyboard.update()

        self.assertFalse(self.keyboard.old_state.is_down(key_id))
        self.assertTrue(self.keyboard.new_state.is_down(key_id))

    def test_is_pressed(self):
        key_id = 2
        self.assertFalse(self.keyboard.is_pressed(key_id))

        self.test_state[key_id] = True
        self.keyboard.update()

        self.assertTrue(self.keyboard.is_pressed(key_id))

    def test_is_released(self):
        key_id = 5
        self.assertFalse(self.keyboard.is_released(key_id))

        self.test_state[key_id] = True
        self.keyboard.update()

        self.assertFalse(self.keyboard.is_released(key_id))

        self.test_state[key_id] = False
        self.keyboard.update()

        self.assertTrue(self.keyboard.is_released(key_id))
