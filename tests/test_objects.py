# coding=utf-8
from unittest.mock import Mock
from pygvent.vector2d import Vector2D
from tests.mocks import MockGameObject, TestCaseWithPatch, \
    MockVisibleGameObject, MockImage


class GameObjectsTest(TestCaseWithPatch):
    def test_enable(self):
        test_object = MockGameObject(is_enabled=False)
        self.assertFalse(test_object.is_enabled)

        test_object.enable()
        self.assertTrue(test_object.is_enabled)

    def test_disable(self):
        test_object = MockGameObject(is_enabled=True)
        self.assertTrue(test_object.is_enabled)

        test_object.disable()
        self.assertFalse(test_object.is_enabled)

    def test_kill(self):
        test_object = MockGameObject()

        self.patch_object(test_object, 'on_kill')
        self.patch_object(test_object, 'clear_layers')

        test_object.kill()

        self.assertEqual(1, test_object.clear_layers.call_count)
        self.assertEqual(1, test_object.on_kill.call_count)


class VisibleGameObjectTest(TestCaseWithPatch):
    def setUp(self):
        self.test_screen = Mock()
        self.test_position = (10, 10)
        self.test_image = MockImage(5, 3, 10, 8)
        self.test_object = MockVisibleGameObject(
            image=self.test_image, position=self.test_position)

    def test_ensure_position_is_vector(self):
        self.assertIsInstance(self.test_object.position, Vector2D)
        self.assertEqual(self.test_position, self.test_object.position)

    def test_show(self):
        test_object = MockVisibleGameObject(is_visible=False)
        self.assertFalse(test_object.is_visible)

        test_object.show()
        self.assertTrue(test_object.is_visible)

    def test_hide(self):
        test_object = MockVisibleGameObject(is_visible=True)
        self.assertTrue(test_object.is_visible)

        test_object.hide()
        self.assertFalse(test_object.is_visible)

    def test_draw_visible(self):
        self.test_object.draw(self.test_screen)

        self.test_screen.blit.assert_called_once_with(
            self.test_object.image, self.test_object.position)

    def test_draw_invisible(self):
        self.test_object.hide()
        self.test_object.draw(self.test_screen)

        self.assertEqual(0, self.test_screen.blit.call_count)

    def test_draw_with_no_image(self):
        self.test_object.image = None
        self.test_object.draw(self.test_screen)

        self.assertEqual(0, self.test_screen.blit.call_count)

    def test_move(self):
        offset = (5, 5)
        expected = (self.test_position[0] + offset[0],
                    self.test_position[1] + offset[1])

        self.test_object.move(offset)
        self.assertEqual(expected, self.test_object.position)

    def test_rect(self):
        self.assertEqual(self.test_object.rect.x, self.test_object.position.x)
        self.assertEqual(self.test_object.rect.y, self.test_object.position.y)
        self.assertEqual(self.test_object.rect.width, self.test_image.width)
        self.assertEqual(self.test_object.rect.height, self.test_image.height)
