import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):

    def __init__(self, images):
        super().__init__(images[0])
        self.rect.y = random.randint(210,340)
        self.step = 0

    def draw(self, screen):
        if self.step >= 9:
            self.step = 0
        screen.blit(BIRD[self.step//5], self.rect)
        self.step += 1