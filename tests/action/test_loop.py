import unittest

from broadway.action.loop import Loop
from tests.fakes import FakeInstantAction, FakeIntervalAction


class LoopTest(unittest.TestCase):
    def test_instant(self):
        action = FakeInstantAction()
        iterations = 5
        expected_overtime = 1.3
        elapsed = expected_overtime

        self.check_loop(action, iterations, elapsed, expected_overtime)

    def test_interval(self):
        action = FakeIntervalAction()
        iterations = 7
        expected_overtime = 1.2
        elapsed = action._duration * iterations + expected_overtime

        self.check_loop(action, iterations, elapsed, expected_overtime)

    def check_loop(self, action, iterations, elapsed, expected_overtime):
        loop = Loop(action=action, iterations=iterations)
        actual_overtime = loop.update(elapsed)

        self.assertTrue(loop.is_done)
        self.assertTrue(action.is_done)
        self.assertEqual(iterations, loop._iterated)
        self.assertEqual(iterations, action.do.call_count)
        self.assertAlmostEqual(expected_overtime, actual_overtime)
