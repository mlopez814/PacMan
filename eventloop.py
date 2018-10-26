import sys

import pygame


# noinspection PyMethodMayBeStatic,PyPep8Naming
class EventLoop:

    def __init__(self, finished):
        self.finished = finished

    def __str__(self):
        return 'eventloop, finished=' + str(self.finished) + ')'

    def check_events(self, settings, screen, stats, sb, player, play_button, maze):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event, player)

            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event, player)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.check_play_button(settings, screen, stats, sb, play_button, mouse_x, mouse_y, maze)

    def check_keydown_events(self, event, player):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            player.moving_up = True
            player.index = 6
        elif event.key == pygame.K_DOWN:
            player.moving_down = True
            player.index = 0
        elif event.key == pygame.K_LEFT:
            player.moving_left = True
            player.index = 2
        elif event.key == pygame.K_RIGHT:
            player.moving_right = True
            player.index = 4

    def check_keyup_events(self, event, player):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            player.moving_up = False
        elif event.key == pygame.K_DOWN:
            player.moving_down = False
        elif event.key == pygame.K_LEFT:
            player.moving_left = False
        elif event.key == pygame.K_RIGHT:
            player.moving_right = False

    def check_play_button(self, settings, screen, stats, sb, play_button, mouse_x, mouse_y, maze):
        button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
        HS_clicked = play_button.rect2.collidepoint(mouse_x, mouse_y)

        if HS_clicked and not stats.game_active:
            stats.HS_active = True

        if button_clicked and not stats.game_active:
            pygame.mouse.set_visible(False)
            stats.reset_stats(settings)
            stats.game_active = True

            sb.prep_score()
            sb.prep_lives(settings, screen, stats, maze)

            maze.build()
