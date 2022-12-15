import pygame
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH


FONT_SIZE = 30
FONT_COLOR = (0,0,0)
FONT_STYLE = 'freesansbold.ttf'

def make_message (
    tetx, 
    screen, 
    font_size= FONT_SIZE, 
    font_color= FONT_COLOR, 
    font_style=FONT_STYLE,
    rect_x = SCREEN_WIDTH // 2,
    rect_y = SCREEN_HEIGHT // 2
):
    font = pygame.font.Font(font_style, font_size)
    message = font.render(tetx, True, font_color)
    message_rect = message.get_rect()
    message_rect.center = (rect_x, rect_y)
    screen.blit(message, message_rect)

