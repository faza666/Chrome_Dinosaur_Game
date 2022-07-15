import pygame
from constants import BG, SCREEN, BLACK


class GameMechanics:
    def __init__(self):
        self.game_speed = 14
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.points = 0
        self.obstacles = []
        self.font = pygame.font.Font('freesansbold.ttf', 20)

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1

        text = self.font.render(f'Points: {self.points}', True, BLACK)
        text_rect = text.get_rect()
        text_rect.center = (1000, 40)
        SCREEN.blit(text, text_rect)

    def background(self):
        image_width = BG.get_width()
        SCREEN.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        SCREEN.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    @classmethod
    def get_collided(cls, dinosaur, obstacle):
        dino_mask = dinosaur.get_mask()
        obstacle_mask = obstacle.get_mask()
        offset = (dinosaur.dino_rect.x - obstacle.rect.x, dinosaur.dino_rect.y - obstacle.rect.y)
        collision_point = dino_mask.overlap(obstacle_mask, offset)
        if collision_point:
            return True
        return False
