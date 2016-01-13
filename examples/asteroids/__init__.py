# coding=utf-8
import logging
from functools import partial
from random import random
from pygvent.display import Resolution
from pygvent.game import Game
from pygvent.controls import Button, TopDownMenu
from pygvent.structures import Layer, Scene
from examples.asteroids.asteroid import Asteroid
from examples.asteroids.player import Player
from examples.asteroids.score import Score


class AsteroidsGame(Game):
    BASE_MAX_ASTEROIDS = 5
    BASE_ASTEROID_POSSIBILITY = 0.01

    def __init__(self, *args, **kwargs):
        super(AsteroidsGame, self).__init__('Asteroids', *args, **kwargs)
        self.asteroid_possibility = None
        self.max_asteroids = None

    def _run_game(self):
        self.start()

        frame = 0

        background = self.engine.image('resource/background.png')

        scene = Scene()

        self.clock.on_tick += self.keyboard.update
        self.clock.on_tick += self.keyboard.handle_events
        self.clock.on_tick += partial(self.screen.blit, background, (0, 0))
        self.clock.on_tick += scene.update
        self.clock.on_tick += partial(scene.draw, self.screen)
        self.clock.on_tick += self.engine.display.update

        self.load_main_menu(scene)
        while self.is_running:
            self.clock.tick(self.frame_rate)

            frame += 1
            if frame % self.frame_rate == 0:
                logging.debug("FPS: {}".format(self.clock.get_fps()))
                logging.debug("Layers: {}".format(scene.layer_names))
                logging.debug("Objects total: {}".format(scene.object_count))

            for event in self.engine.event.get():
                if event.type == self.engine.QUIT:
                    self.stop()

    def clear_input_bindings(self):
        self.keyboard.keys.K_UP.on_press.clear()
        self.keyboard.keys.K_DOWN.on_press.clear()
        self.keyboard.keys.K_SPACE.on_press.clear()

    def load_main_menu(self, scene):
        menu_layer = Layer('MainMenu')
        scene.add(menu_layer)

        menu = TopDownMenu((self.resolution.width // 2 - 45,
                            self.resolution.height // 2 - 45))
        menu.add_to_layer(menu_layer)

        self.keyboard.keys.K_UP.on_press += menu.move_up
        self.keyboard.keys.K_DOWN.on_press += menu.move_down
        self.keyboard.keys.K_SPACE.on_press += menu.select

        menu.on_kill += self.clear_input_bindings

        start_button = self.create_button(menu, (0, 0), 'start')
        start_button.on_press += menu.kill
        start_button.on_press += partial(self.load_game_level, scene)
        menu.add_button(start_button)

        exit_button = self.create_button(menu, (0, 50), 'exit')
        exit_button.on_press += self.stop
        menu.add_button(exit_button)

    def create_button(self, menu, offset, button_name):
        idle = self.engine.image(
            'resource/{}_button_idle.png'.format(button_name))
        select = self.engine.image(
            'resource/{}_button_select.png'.format(button_name))
        press = self.engine.image(
            'resource/{}_button_press.png'.format(button_name))
        button_images = Button.Images(idle, select, press)
        return Button(menu.position + offset, button_images)

    def load_game_level(self, scene):
        player_layer = Layer('Player')
        scene.add(player_layer)

        player = self.create_player(player_layer)

        projectile_image = self.engine.image('resource/projectile.png')

        projectiles = Layer('Projectiles')
        scene.add(projectiles)

        self.keyboard.keys.K_LEFT.on_down += player.move_left
        self.keyboard.keys.K_RIGHT.on_down += player.move_right
        self.keyboard.keys.K_SPACE.on_press += partial(
            player.shoot, projectiles, projectile_image)

        asteroid_images = Asteroid.Images(
            self.engine.image('resource/asteroid.png'),
            self.engine.image('resource/asteroid_explosion.png')
        )

        asteroids = Layer('Asteroids')
        scene.add(asteroids)

        self.asteroid_possibility = self.BASE_ASTEROID_POSSIBILITY
        self.max_asteroids = self.BASE_MAX_ASTEROIDS

        score_layer = Layer('Score')
        scene.add(score_layer)

        score = self.create_score(score_layer)

        self.clock.on_tick.extend(
            [partial(self.create_random_asteroid, asteroids, asteroid_images),
             partial(self.handle_collisions, player, score, scene)]
        )

        player.on_kill.extend(
            [partial(self.clock.on_tick.remove, self.create_random_asteroid),
             partial(self.clock.on_tick.remove, self.handle_collisions),
             self.clear_input_bindings,
             partial(self.engine.time.wait, 1000),
             scene.clear,
             partial(self.load_main_menu, scene)]
        )

    def create_score(self, layer):
        font_size = 24
        font = self.engine.font.Font('resource/arial.ttf', font_size)
        color = self.engine.color.Color('white')
        message = 'Asteroids killed'
        score = Score(font, color, message, (20, 20))
        layer.add(score)
        return score

    def create_player(self, layer):
        player_images = Player.Images(
            self.engine.image('resource/ship.png'),
            self.engine.image('resource/ship_explosion.png')
        )

        width, height = player_images.normal.get_size()
        player = Player((self.resolution.width // 2 - width // 2,
                         self.resolution.height - height),
                        player_images)
        layer.add(player)

        return player

    def create_random_asteroid(self, asteroids, images):
        if len(asteroids) < self.max_asteroids:
            if random() < self.asteroid_possibility:
                position = (int((self.resolution.width - 20) * random()), -10)
                asteroid = Asteroid(position, images)
                asteroids.add(asteroid)
        self.increase_possibility()

    def increase_possibility(self):
        if random() < 0.5:
            if random() < 0.001:
                self.max_asteroids += 1
            else:
                self.asteroid_possibility += 0.0001

    def handle_collisions(self, player, score, scene):
        if player.state is not Player.State.DESTROYED:
            for asteroid in scene['Asteroids']:
                if self.engine.sprite.collide_mask(player, asteroid):
                    asteroid.state = Asteroid.State.DESTROYED
                    player.state = Player.State.DESTROYED
                    break
                for projectile in scene['Projectiles']:
                    if self.engine.sprite.collide_mask(asteroid, projectile):
                        asteroid.state = Asteroid.State.DESTROYED
                        projectile.kill()
                        score.increase(1)
                        break


def main():
    AsteroidsGame(resolution=Resolution.Custom(483, 483)).run()


if __name__ == "__main__":
    main()
