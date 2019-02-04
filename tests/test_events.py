# coding=utf-8
from functools import partial
from unittest import TestCase
from unittest.mock import Mock
from broadway.event import Event, Handler


class CommandTest(TestCase):
    def setUp(self):
        self.some_function = Mock()

    def test_create_command_with_no_params(self):
        command = Handler(self.some_function)

        self.assertIs(self.some_function, command.func)
        self.assertFalse(command.args)
        self.assertFalse(command.keywords)

    def test_create_command_with_args(self):
        args = ['a', 'b', 'c']
        command = Handler(self.some_function, *args)

        self.assertSequenceEqual(args, command.args)

    def test_create_command_with_keywords(self):
        keywords = {'a': 1, 'b': 'c'}
        command = Handler(self.some_function, **keywords)

        self.assertDictEqual(keywords, command.keywords)

    def test_command_equal_function(self):
        self.assertEqual(self.some_function, Handler(self.some_function))

    def test_command_equal_partial(self):
        self.assertEqual(partial(self.some_function),
                         Handler(self.some_function))

    def test_command_equal_command(self):
        self.assertEqual(Handler(self.some_function),
                         Handler(self.some_function))

    def test_convert_function_to_command(self):
        converted = Handler.convert(self.some_function)

        self.assertIsInstance(converted, Handler)
        self.assertEqual(converted, Handler(self.some_function))

    def test_convert_partial_to_command(self):
        args = ['some', 'args']
        keywords = {'apple': 1, 'banana': 'orange'}
        partial_function = partial(self.some_function, *args, **keywords)
        converted = Handler.convert(partial_function)

        self.assertIsInstance(converted, Handler)
        self.assertEqual(partial_function, converted)
        self.assertSequenceEqual(partial_function.args, converted.args)
        self.assertDictEqual(partial_function.keywords, converted.keywords)

    def test_convert_command_to_command(self):
        command = Handler(self.some_function)

        self.assertIs(command, Handler.convert(command))

    def test_call_command(self):
        command = Handler(self.some_function, 'a', 'b', alpha=1)
        command()

        self.some_function.assert_called_once_with('a', 'b', alpha=1)


class EventsTest(TestCase):
    def setUp(self):
        self.event = Event()
        self.some_function = Mock()
        self.another_function = Mock()

    def test_add_function(self):
        self.event += self.some_function
        self.event.add(self.some_function)

        self.assertEqual(2, len(self.event._handlers))

    def test_add_command(self):
        self.event += Handler(self.some_function, 1, 2)
        self.event.add(Handler(self.some_function, 1))

        self.assertEqual(2, len(self.event._handlers))

    def test_remove(self):
        self.event += self.some_function
        self.event += Handler(self.some_function, 1, 2)
        self.event += partial(self.some_function, 'apple')

        self.event += partial(self.another_function, 1)
        self.assertEqual(4, len(self.event._handlers))

        self.event.remove(self.some_function)
        self.assertEqual(1, len(self.event._handlers))

        self.event -= self.another_function
        self.assertEqual(0, len(self.event._handlers))

    def test_clear(self):
        self.event += self.some_function
        self.event += Handler(self.some_function, 1, 2)

        self.event.clear()
        self.assertEqual(0, len(self.event._handlers))

    def test_call(self):
        self.event += Handler(self.some_function, 'banana', 6)
        self.event += Handler(self.another_function, 18)

        self.event()
        self.some_function.assert_called_once_with('banana', 6)
        self.another_function.assert_called_once_with(18)

    def test_convert_function(self):
        self.assertIsInstance(Handler.convert(self.some_function), Handler)

    def test_convert_partial(self):
        partial_function = partial(self.some_function, 1, 2)
        self.assertIsInstance(Handler.convert(partial_function), Handler)

    def test_convert_handler(self):
        handler = Handler(self.some_function)
        self.assertIs(Handler.convert(handler), handler)
