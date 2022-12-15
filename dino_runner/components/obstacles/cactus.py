from random import randint
from dino_runner.components.obstacles.obstacle import Obstacle

class Cactus(Obstacle):
    
    def __init__(self, images, y_pos):
        cactus_type = randint(0,2)
        super().__init__(images[cactus_type])
        self.rect.y = y_pos
        
    