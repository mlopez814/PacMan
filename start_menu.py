import pygame.font

from player import Player
from red import Red
from pink import Pink
from blue import Blue
from orange import Orange

from settings import Settings


# noinspection PyAttributeOutsideInit,SpellCheckingInspection
class Menu:

    def __init__(self, screen, stats, sb, play_button, maze):
        self.settings = Settings()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.button = play_button
        self.stats = stats
        self.sb = sb

        self.maze = maze

        self.menu_color = (0, 0, 0)
        self.text_color = (250, 250, 210)
        self.font = pygame.font.SysFont(None, 150)

        self.title = "Pac-man"

        self.prep_screen()

    def prep_screen(self):
        self.title_image = self.font.render(self.title, True, self.text_color, self.menu_color)
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.centerx = self.screen_rect.centerx
        self.title_image_rect.centery = self.screen_rect.top + 100

        self.create_pacman()
        self.create_ghost()

    def draw_menu(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.title_image, self.title_image_rect)
        self.button.draw_button()
        self.animate_pacman()
        self.animate_ghost()

    def create_pacman(self):
        self.pacman = Player(self.settings, self.screen, self.stats, self.sb, self.maze)

        self.pacman.centerx = self.screen_rect.left
        self.pacman.rect.centery = self.screen_rect.centery

        self.pacman.index = 4

    def create_ghost(self):
        self.red = Red(self.screen, self.stats, self.pacman, self.sb, self.maze)

        self.red.centerx = self.screen_rect.left - 100
        self.red.rect.centery = self.screen_rect.centery

        self.red.index = 4

        self.blue = Blue(self.screen, self.stats, self.pacman)

        self.blue.centerx = self.screen_rect.left - 125
        self.blue.rect.centery = self.screen_rect.centery

        self.blue.index = 4

        self.orange = Orange(self.screen, self.stats, self.pacman)

        self.orange.centerx = self.screen_rect.left - 150
        self.orange.rect.centery = self.screen_rect.centery

        self.orange.index = 4

        self.pink = Pink(self.screen, self.stats, self.pacman)

        self.pink.centerx = self.screen_rect.left - 175
        self.pink.rect.centery = self.screen_rect.centery

        self.pink.index = 4

    def animate_pacman(self):
        self.pacman.screen_animate()
        self.pacman.blitme()

    def animate_ghost(self):
        self.red.screen_animate()
        self.red.blitme()

        self.blue.screen_animate()
        self.blue.blitme()

        self.orange.screen_animate()
        self.orange.blitme()

        self.pink.screen_animate()
        self.pink.blitme()
