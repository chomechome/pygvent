import unittest

from pygvent.action.chain import Chain
from tests.fakes import FakeInstantAction, FakeIntervalAction


class ChainTest(unittest.TestCase):
    def test_forward_time_in_update_to_interval_action(self):
        action = FakeIntervalAction(duration=2)
        chain = Chain(action)

        elapsed = 1

        overtime = chain.update(elapsed)

        self.assertEqual(0, overtime)
        self.assertEqual(elapsed, action._elapsed)

    def test_finish_single_instant_action(self):
        action = FakeInstantAction()
        chain = Chain(action)
        elapsed = 1

        overtime = chain.update(elapsed)

        self.assertEqual(elapsed, overtime)
        self.assertTrue(action.is_done)
        self.assertTrue(chain.is_done)

    def test_start_actions_in_a_row(self):
        first = FakeIntervalAction()
        second = FakeIntervalAction()
        chain = Chain(first, second)

        chain.start()
        first.start.assert_called_once()
        second.start.assert_not_called()

        chain.update(first._duration)
        second.start.assert_called_once()

    def test_finish_first_interval_action_but_not_second(self):
        first = FakeIntervalAction()
        second = FakeIntervalAction()
        elapsed = first._duration

        chain = Chain(first, second)
        self.assertEqual(0, chain.update(elapsed))

        self.assertFalse(chain.is_done)
        self.assertTrue(first.is_done)
        self.assertFalse(second.is_done)

    def test_instant_after_instant(self):
        first = FakeInstantAction()
        second = FakeInstantAction()
        expected_overtime = 1.3
        elapsed = expected_overtime

        self.check_chain(first, second, elapsed, expected_overtime)

    def test_instant_after_interval(self):
        first = FakeIntervalAction()
        second = FakeInstantAction()
        expected_overtime = 0.2
        elapsed = first._duration + expected_overtime

        self.check_chain(first, second, elapsed, expected_overtime)

    def test_interval_after_instant(self):
        first = FakeInstantAction()
        second = FakeIntervalAction()
        expected_overtime = 0.8
        elapsed = second._duration + expected_overtime

        self.check_chain(first, second, elapsed, expected_overtime)

    def test_interval_after_interval(self):
        first = FakeIntervalAction()
        second = FakeIntervalAction()
        expected_overtime = 0.1
        elapsed = first._duration + second._duration + expected_overtime

        self.check_chain(first, second, elapsed, expected_overtime)

    def check_chain(self, first, second, elapsed, expected_overtime):
        chain = Chain(first, second)
        actual_overtime = chain.update(elapsed)

        self.assertTrue(chain.is_done)
        self.assertTrue(first.is_done)
        self.assertTrue(second.is_done)
        self.assertAlmostEqual(expected_overtime, actual_overtime)
