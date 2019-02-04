from broadway.game import Game
from broadway.geometry import Point, Rectangle
from broadway.resolution import Resolution
from broadway.structure import Scene

from asteroids import AsteroidField
from background import Background
from score import AsteroidScore
from player import Player


class Asteroids(Game):
    def load(self):
        resolution = self.display.get_resolution()

        background = Background(
            image=self.engine.get_picture('resource/background.png'),
        )
        score = AsteroidScore(
            font=self.engine.get_font('resource/arial.ttf'),
            position=Point(0, resolution.height),
        )
        field = AsteroidField(
            image=self.engine.get_picture('resource/asteroid.png'),
            area=Rectangle(0, 0, resolution.width, resolution.height),
        )
        player = Player(
            keyboard=self.engine.get_keyboard(),
            image=self.engine.get_picture('resource/ship.png'),
            position=Point(resolution.width / 2, 0),
        )
        return Scene(nodes=[background, player, field, score])


if __name__ == "__main__":
    Asteroids(caption='Asteroids', resolution=Resolution(483, 483)).run()
