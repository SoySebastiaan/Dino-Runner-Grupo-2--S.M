import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import DUCKING, RUNNING, JUMPING


JUMPING_ACTION = "jumping"
RUNNING_ACTION = "running"
DUCKING_ACTION = "ducking"
class Dinosaur(Sprite):
    Y_POS = 310
    X_POS = 80
    Y_POS_DUCK = 340
    JUMP_VELOCITY = 8.5
    def __init__(self):
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step = 0
        self.jump_velocity = self.JUMP_VELOCITY
        self.action = RUNNING_ACTION


    def update(self, user_input):
        if self.action == RUNNING_ACTION:
            self.run()
        elif self.action == JUMPING_ACTION:
            self.jump()
        elif self.action == DUCKING_ACTION:
            self.duck()

        if self.action != JUMPING_ACTION:
            if user_input[pygame.K_UP]: 
                self.action = JUMPING_ACTION
            else:
                self.action = RUNNING_ACTION

        if self.action != DUCKING_ACTION:
            if user_input[pygame.K_DOWN]:
                self.action = DUCKING_ACTION
            
                
        if self.step >= 9:
            self.step = 0

    def run (self):
        self.image = RUNNING[0] if self.step < 5 else RUNNING[1]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step += 1
    
    def jump (self):
        self.image = JUMPING
        self.rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.rect.y = self.Y_POS
            self.jump_velocity = self.JUMP_VELOCITY
            self.action = RUNNING_ACTION    

    def duck(self):
        self.image = DUCKING[0] if self.step < 5 else DUCKING[1]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = 340
        self.step += 1

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))