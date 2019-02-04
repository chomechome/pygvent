import unittest

import pyglet


class PygletTestCase(unittest.TestCase):
    def setUp(self):
        self.window = pyglet.window.Window()

    def tearDown(self):
        self.window.close()
