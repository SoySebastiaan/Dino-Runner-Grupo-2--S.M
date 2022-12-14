import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        self.SMALL_CACTUS = 1
        self.LARGE_CACTUS = 2
        self.cactus = random.randint(self.SMALL_CACTUS, self.LARGE_CACTUS)
        if len(self.obstacles) == 0:
            if self.cactus % 2 == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            else:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if obstacle.rect.colliderect(game.player.rect):
                pygame.time.delay(500)
                game.playing = False

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            