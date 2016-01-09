# coding=utf-8
from functools import partial
from pygvent.events import Event, Handler
from tests.mocks import TestCaseWithPatch


class EventsTest(TestCaseWithPatch):
    def setUp(self):
        self.event = Event()

    def some_function(self, unused, another_unused):
        pass

    def another_function(self, unused):
        pass

    def test_add(self):
        self.event += self.some_function
        self.event.add(self.some_function)
        self.assertEqual(2, len(self.event.handlers))

        self.event += Handler(self.some_function, 1, 2)
        self.event.add(Handler(self.some_function, 1))
        self.assertEqual(4, len(self.event.handlers))

    def test_remove(self):
        self.event += self.some_function
        self.event += Handler(self.some_function, 1, 2)
        self.event += partial(self.some_function, 'apple')

        self.event += partial(self.another_function, 1)
        self.assertEqual(4, len(self.event.handlers))

        self.event.remove(self.some_function)
        self.assertEqual(1, len(self.event.handlers))

        self.event -= self.another_function
        self.assertEqual(0, len(self.event.handlers))

    def test_clear(self):
        self.event += self.some_function
        self.event += Handler(self.some_function, 1, 2)

        self.event.clear()
        self.assertEqual(0, len(self.event.handlers))

    def test_call(self):
        self.patch_object(self, 'some_function')
        self.patch_object(self, 'another_function')

        self.event += Handler(self.some_function, 'banana', 6)
        self.event += Handler(self.another_function, 18)

        self.event()
        self.some_function.assert_called_once_with('banana', 6)
        self.another_function.assert_called_once_with(18)

    def test_handler_convert(self):
        self.assertIsInstance(Handler.convert(self.some_function), Handler)
        self.assertIsInstance(
            Handler.convert(partial(self.some_function, 1, 2)), Handler)

        handler = Handler(self.some_function)
        self.assertIs(Handler.convert(handler), handler)
