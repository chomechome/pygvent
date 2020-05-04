import pyglet

from pygvent.loop import IGameLoop
from pygvent.structure import Scene
from pygvent.types import FrameRate


class PygletLoop(IGameLoop):
    def __init__(self, rate: FrameRate, window: pyglet.window.Window):
        self._rate = rate
        self._window = window

    def run(self, scene: Scene):
        window = self._window

        @window.event
        def on_draw():
            on_update.dispatch()

        pyglet.clock.set_fps_limit(self._rate)
        pyglet.clock.schedule(scene.update)

        pyglet.app.run()

    def stop(self):
        pyglet.app.exit()
