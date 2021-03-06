# coding=utf-8
from unittest import TestCase
from unittest.mock import patch
from pygvent.objects import GameObject, VisibleGameObject
from pygvent.vector2d import Vector2D


class TestCaseWithPatch(TestCase):
    def patch(self, *args, **kwargs):
        patcher = patch(*args, **kwargs)
        patcher.start()
        self.addCleanup(patcher.stop)
        return patcher

    def patch_object(self, *args, **kwargs):
        patcher = patch.object(*args, **kwargs)
        patcher.start()
        self.addCleanup(patcher.stop)
        return patcher


class MockGameObject(GameObject):
    def update(self):
        pass


class MockVisibleGameObject(VisibleGameObject):
    def __init__(self, position=Vector2D.zeros(), *args, **kwargs):
        super(MockVisibleGameObject, self).__init__(position, *args, **kwargs)

    def update(self):
        pass


class MockImage(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_rect(self):
        return self

    def get_size(self):
        return self.width, self.height
