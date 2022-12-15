import pygame
from dino_runner.utils.constants import FONT_STYLE


class Score:
    def __init__(self):
        self.points = 0
        self.high_score = 0

    def update(self, game):
        self.points += 1
        if self.points % 100 == 0:
            game.game_speed += 3

        if self.points > self.high_score:
            self.high_score = self.points
        
    def draw(self, screen):
        font = pygame.font.Font(FONT_STYLE, 22)
        message = font.render(f"Score: {self.points}    High Score: {self.high_score} ", True, (0,0,0))
        message_rect = message.get_rect()
        message_rect.center = (900, 40)
        screen.blit(message, message_rect)

    def reset_score(self, game):
        self.points = 0
        game.game_speed = 20