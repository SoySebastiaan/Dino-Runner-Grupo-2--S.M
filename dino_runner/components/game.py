import pygame
from dino_runner.components.clouds import Clouds
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.messages import make_message
from dino_runner.components.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.score import Score


from dino_runner.utils.constants import (BG, DINO_DEAD, DINO_START, GAME_OVER, HAMMER_TYPE, HEART_TYPE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD_TYPE, TITLE, FPS)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.clouds = Clouds()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.score = Score()
        self.death_count = 0
        self.executing = False

        

    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()

        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()      
        self.score.reset_score(self) 
        while self.playing:
            self.events()
            self.update()
            self.draw()
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self.heart_fly)
        self.clouds.update(self)
        self.obstacle_manager.update(self.game_speed, self.player, self.on_death)
        self.power_up_manager.update(self.game_speed, self.score.points, self.player)
        self.score.update(self)
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.clouds.draw(self.screen)
        self.player.draw(self.screen)
        self.player.draw_active_power_up(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed


    def show_menu(self):
        #Mensaje en la pantalla
        self.screen.fill((245,245,220))
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2

        if self.death_count == 0:
            make_message("Press any key to play...", self.screen)
            self.screen.blit(DINO_START, (half_screen_width -40, half_screen_height -120))
        else:
            self.restar_game()
        #Update
        pygame.display.update()
        #Escuchar
        self.handle_menu_events()

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def restar_game(self):
        self.screen.fill((0,255,255))
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2

        if self.death_count > 0:
            make_message("YOU LOSE...", self.screen)
            make_message("Press any key to restar...", self.screen, rect_y=half_screen_height + 50)
            make_message(f"Your Score: {self.score.points}", self.screen, rect_y=half_screen_height+100)
            make_message(f"Best Score: {self.score.high_score}", self.screen, rect_y=half_screen_height+150)
            make_message(f"Deaths: {self.death_count}", self.screen, rect_y=half_screen_height+200)
            self.screen.blit(DINO_DEAD, (half_screen_width -50, half_screen_height -150))
            self.screen.blit(GAME_OVER, (half_screen_width -200, half_screen_height -210))
            pygame.display.update()

    def on_death(self):
        has_shield = self.player.type == SHIELD_TYPE
        if not has_shield:
            self.player.on_dino_death()
            self.draw()
            self.death_count += 1
            self.playing = False

        return not has_shield

    def heart_fly(self):
        has_heart = self.player.type == HEART_TYPE
        return has_heart




