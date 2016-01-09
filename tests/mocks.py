# coding=utf-8
from unittest import TestCase
from unittest.mock import patch


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
