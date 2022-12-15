import pygame
import random
from dino_runner.components.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager:
    Y_POS_LARGE = 330

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        self.type_obstacle = random.randint(0,2)
        if len(self.obstacles) == 0:
            if self.type_obstacle == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif self.type_obstacle == 2:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            else:
                self.obstacles.append(Bird(BIRD))


            

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if obstacle.rect.colliderect(game.player.rect):
                pygame.time.delay(500)
                game.playing = False
                game.death_count +=1

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            

    def reset_obstacles(self):
        self.obstacles = []