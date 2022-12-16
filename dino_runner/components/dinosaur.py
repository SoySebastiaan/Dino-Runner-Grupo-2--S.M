import pygame
from pygame.sprite import Sprite
from dino_runner.components.messages import make_message
from dino_runner.utils.constants import DEFAULT_TYPE, DINO_DEAD, DUCKING, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING, JUMPING, RUNNING_SHIELD, SHIELD_TYPE


JUMPING_ACTION = "jumping"
RUNNING_ACTION = "running"
DUCKING_ACTION = "ducking"
DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
class Dinosaur(Sprite):
    Y_POS = 310
    X_POS = 80
    Y_POS_DUCK = 340
    JUMP_VELOCITY = 8.5
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step = 0
        self.jump_velocity = self.JUMP_VELOCITY
        self.action = RUNNING_ACTION
        self.has_power_up = False
        self.power_up_time_up = 0


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
        self.image = RUN_IMG[self.type][self.step // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step += 1
    
    def jump (self):
        self.image = JUMP_IMG[self.type]
        self.rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.rect.y = self.Y_POS
            self.jump_velocity = self.JUMP_VELOCITY
            self.action = RUNNING_ACTION    

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = 340
        self.step += 1

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def on_pick_power_up(self, power_up):
        self.has_power_up = True
        self.power_up_time_up = power_up.start_time + (power_up.duration * 1000)
        self.type = power_up.type

    def draw_active_power_up(self, screen):
        if self.has_power_up:
            left_time = round((self.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
            if left_time >= 0:
                make_message(
                    f"{self.type.capitalize()} enabled for {left_time} seconds.", 
                    screen, 
                    font_size=18, 
                    rect_y=80
                )
            else:
                self.type = DEFAULT_TYPE
                self.has_power_up = False

    def on_dino_death(self):
        self.image = DINO_DEAD