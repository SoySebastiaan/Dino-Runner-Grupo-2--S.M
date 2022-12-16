import pygame
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

def make_message (
    tetx, 
    screen, 
    font_size= 30, 
    font_color= (0,0,0), 
    font_style='freesansbold.ttf',
    rect_x = SCREEN_WIDTH // 2,
    rect_y = SCREEN_HEIGHT // 2
):
    font = pygame.font.Font(font_style, font_size)
    message = font.render(tetx, True, font_color)
    message_rect = message.get_rect()
    message_rect.center = (rect_x, rect_y)
    screen.blit(message, message_rect)

