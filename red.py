import pygame
from settings import Settings


def load_image(self):
    image = pygame.image.load(self)
    return image


class Red:
    BRICK_SIZE = 15

    def __init__(self, screen, stats, player, sb, maze):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = Settings()
        self.stats = stats
        self.sb = sb
        self.maze = maze
        self.pacman = player
        self.filename = 'images/maze.txt'
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.deltax = self.deltay = Red.BRICK_SIZE

        self.centerx = 0
        self.centery = 0

        self.startx = 0
        self.starty = 0

        self.build()

        self.images = []
        self.images.append(load_image('images/Ghost/Red/RedD3.png'))
        self.images.append(load_image('images/Ghost/Red/RedD4.png'))
        self.images.append(load_image('images/Ghost/Red/RedL3.png'))
        self.images.append(load_image('images/Ghost/Red/RedL4.png'))
        self.images.append(load_image('images/Ghost/Red/RedR3.png'))
        self.images.append(load_image('images/Ghost/Red/RedR4.png'))
        self.images.append(load_image('images/Ghost/Red/RedU3.png'))
        self.images.append(load_image('images/Ghost/Red/RedU4.png'))

        self.images.append(load_image('images/Ghost/scared/scared3.png'))
        self.images.append(load_image('images/Ghost/scared/scared4.png'))

        self.index = self.settings.ghost_index
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        self.rect.centery = self.centery
        self.rect.centerx = self.centerx

        self.moving_right = True
        self.moving_left = False
        self.moving_down = True
        self.moving_up = False

        self.direction = 1

    def build(self):
        dx, dy = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'R':
                    self.centerx += ncol * dx
                    self.centery += nrow * dy

                    self.startx = self.centerx
                    self.starty = self.centery

    def reset(self):
        self.centery = self.starty
        self.centerx = self.startx

    def blitme(self):
            self.screen.blit(self.image, self.rect)

    def update(self):
        self.locate_pacman()
        self.move()

        collisions = pygame.Rect.colliderect(self.rect, self.pacman.rect)

        if collisions and not self.stats.BEAST_MODE:
            self.reset()
            self.pacman.reset()
            self.stats.pacman_lives -= 1
            self.sb.prep_lives(self.settings, self.screen, self.stats, self.maze)
            if self.stats.pacman_lives == 0:
                self.stats.game_active = False
                pygame.mouse.set_visible(True)

        if self.stats.BEAST_MODE:
            self.index = 8
            if collisions:
                self.reset()

        if not self.stats.game_active:
            self.reset()

        self.rect.centery = self.centery
        self.rect.centerx = self.centerx

        self.animate()

    def screen_animate(self):
        self.centerx += (self.settings.pac_man_speedfactor * 1.08)

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
        if self.index == 8:
            self.index = 6
        if self.index >= 10:
            self.index = 8
        self.image = self.images[self.index]

    def move(self):
        r = int((self.rect.centerx + 10) / 15)
        d = int((self.rect.centery + 10) / 15)
        l = int((self.rect.centerx - 10) / 15)
        u = int((self.rect.centery - 10) / 15)
        if self.moving_up and (self.rows[u-1][r] != 'X') and (self.rows[u-1][l] != 'X'):
            self.centery -= self.settings.ghost_speedfactor * self.direction
        if self.moving_down and (self.rows[d+1][r] != 'X') and (self.rows[d+1][l] != 'X'):
            self.centery += self.settings.ghost_speedfactor * self.direction
        if self.moving_right and (self.rows[u][r+1] != 'X') and (self.rows[d][r+1] != 'X'):
            self.centerx += self.settings.ghost_speedfactor * self.direction
        if self.moving_left and (self.rows[u][l-1] != 'X') and (self.rows[d][l-1] != 'X'):
            self.centerx -= self.settings.ghost_speedfactor * self.direction

        self.rect.centery = self.centery
        self.rect.centerx = self.centerx

    def locate_pacman(self):
        destinationx = self.pacman.rect.centerx
        destinationy = self.pacman.rect.centery

        if self.rect.centerx > destinationx:
            self.moving_left = True
            self.moving_right = False
        if self.rect.centerx < destinationx:
            self.moving_right = True
            self.moving_left = False
        if self.rect.centery > destinationy:
            self.moving_up = True
            self.moving_down = False
        if self.rect.centery < destinationy:
            self.moving_down = True
            self.moving_up = False
