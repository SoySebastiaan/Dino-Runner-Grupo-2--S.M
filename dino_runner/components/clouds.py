
from random import randint
from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH


class Clouds:
    def __init__(self):
        self.width_screen = SCREEN_WIDTH
        self.pos_x = self.width_screen + randint(800, 1000)
        self.pos_y = randint(50, 190)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self, game):
        self.pos_x -= game.game_speed
        if self.pos_x < -self.width:
            self.pos_x = self.width_screen + randint(1000, 2000)
            self.pos_y = randint(50, 100)

    def draw(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))