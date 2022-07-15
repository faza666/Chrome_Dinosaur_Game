import pygame
import random
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, SCREEN, RUNNING, SMALL_CACTUS, LARGE_CACTUS, BIRD
from game import GameMechanics
from dinosaur import Dinosaur
from cloud import Cloud
from obstacles import SmallCactus, LargeCactus, Bird

pygame.init()


def main_loop(game):
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud = Cloud()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill(WHITE)
        user_input = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(user_input)

        if len(game.obstacles) == 0:
            obstacle_type = random.randint(0, 5)
            if obstacle_type == 0:
                game.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif obstacle_type == 1:
                game.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif obstacle_type == 2:
                game.obstacles.append(Bird(BIRD))
            else:
                pass

        for obstacle in game.obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(game)
            if game.get_collided(player, obstacle):
                pygame.time.delay(2000)
                run = False
                game.obstacles.pop()

        game.background()
        game.score()

        cloud.draw(SCREEN)
        cloud.update(game)

        clock.tick(30)
        pygame.display.update()


def menu():

    game = GameMechanics()
    death_count = 0
    run = True
    while run:
        SCREEN.fill(WHITE)
        font = pygame.font.Font('freesansbold.ttf', 30)

        text = font.render('Press any key to RUN', True, BLACK)
        if death_count > 0:
            score = font.render(f'Your Score: {game.points}', True, BLACK)
            score_rect = score.get_rect()
            score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, score_rect)

        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, text_rect)
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                game.points = 0
                main_loop(game)
                death_count += 1


if __name__ == '__main__':
    menu()
