import pygame
from pygame.sprite import Sprite


def load_image(self):
    image = pygame.image.load(self)
    return image


# noinspection PyMethodMayBeStatic,PyPep8Naming
class Player(Sprite):
    BRICK_SIZE = 15

    def __init__(self, settings, screen, stats, sb, maze):
        super(Player, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.stats = stats
        self.maze = maze
        self.sb = sb
        with open('images/maze.txt', 'r') as f:
            self.rows = f.readlines()

        self.deltax = self.deltay = Player.BRICK_SIZE

        self.centerx = 0
        self.centery = 0

        self.startx = 0
        self.starty = 0

        self.build()

        self.images = []
        self.images.append(load_image('images/pacman/pacmanD1.png'))
        self.images.append(load_image('images/pacman/pacmanD2.png'))
        self.images.append(load_image('images/pacman/pacmanL1.png'))
        self.images.append(load_image('images/pacman/pacmanL2.png'))
        self.images.append(load_image('images/pacman/pacmanR1.png'))
        self.images.append(load_image('images/pacman/pacmanR2.png'))
        self.images.append(load_image('images/pacman/pacmanU1.png'))
        self.images.append(load_image('images/pacman/pacmanU2.png'))
        self.index = self.settings.pac_man_index
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        self.rect.centery = self.centery
        self.rect.centerx = self.centerx

        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def build(self):
        dx, dy = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'P':
                    self.centerx += (ncol + .5) * dx
                    self.centery += (nrow + .5) * dy

                    self.startx = self.centerx
                    self.starty = self.centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def reset(self):
        self.centery = self.starty
        self.centerx = self.startx

    def update(self, maze):
        if self.stats.game_active:
            self.move()

        if self.stats.BEAST_MODE:
            self.settings.pac_man_speedfactor = 10
            self.settings.ghost_direction = -1

        self.animate()

        self.increment_score(self.maze, self.settings, self.stats, self.sb)

    def move(self):
        r = int((self.rect.centerx + 10) / 15)
        d = int((self.rect.centery + 10) / 15)
        l = int((self.rect.centerx - 10) / 15)
        u = int((self.rect.centery - 10) / 15)
        if self.moving_up and (self.rows[u-1][r] != 'X') and (self.rows[u-1][l] != 'X'):
            self.centery -= self.settings.pac_man_speedfactor
        if self.moving_down and (self.rows[d+1][r] != 'X') and (self.rows[d+1][l] != 'X'):
            self.centery += self.settings.pac_man_speedfactor
        if self.moving_right and (self.rows[u][r+1] != 'X') and (self.rows[d][r+1] != 'X'):
            self.centerx += self.settings.pac_man_speedfactor
        if self.moving_left and (self.rows[u][l-1] != 'X') and (self.rows[d][l-1] != 'X'):
            self.centerx -= self.settings.pac_man_speedfactor

        self.rect.centery = self.centery
        self.rect.centerx = self.centerx

    def screen_animate(self):
        self.centerx += self.settings.pac_man_speedfactor

        if self.centerx >= self.screen_rect.right:
            self.centerx = self.screen_rect.left

        self.rect.centerx = self.centerx

        self.animate()

    def animate(self):
        self.index += 1
        if self.index == 2:
            self.index = 0
        if self.index == 4:
            self.index = 2
        if self.index == 6:
            self.index = 4
        if self.index >= 8:
            self.index = 6
        self.image = self.images[self.index]

    def increment_score(self, maze, settings, stats, sb):
        for x in maze.dots:
            dot_collision = pygame.Rect.colliderect(self.rect, x)
            if dot_collision:
                maze.dots.remove(x)
                stats.score += settings.dot_score
                sb.prep_score()
                self.check_high_score(stats, sb)
                if len(maze.dots) == 0:
                    stats.dots_clear = True
        for x in maze.DOTS:
            DOT_collision = pygame.Rect.colliderect(self.rect, x)
            if DOT_collision:
                maze.DOTS.remove(x)
                stats.score += settings.DOT_SCORE
                sb.prep_score()
                self.check_high_score(stats, sb)
                stats.BEAST_MODE = True
                if len(maze.DOTS) == 0:
                    stats.DOTS_CLEAR = True
        if stats.dots_clear and stats.DOTS_CLEAR:
            stats.level += 1
            sb.prep_level()
            maze.build()
            self.reset()
            stats.dots_clear = False
            stats.DOTS_CLEAR = False

    def check_high_score(self, stats, sb):
        if stats.score > stats.high_score:
            stats.high_score = stats.score
            sb.prep_high_score()
