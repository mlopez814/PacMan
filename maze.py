import pygame
from imagerect import ImageRect


class Maze:
    RED = (255, 0, 0)
    BRICK_SIZE = 15

    def __init__(self, screen, mazefile, cubefile, gatefile, dotfile):
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.bricks = []
        sz = Maze.BRICK_SIZE
        self.brick = ImageRect(screen, cubefile, sz, sz)
        self.deltax = self.deltay = Maze.BRICK_SIZE

        self.gates = []
        self.gate = ImageRect(screen, gatefile, sz, sz)

        self.dots = []
        self.dot = ImageRect(screen, dotfile, sz, sz)

        self.DOTS = []
        self.DOT = ImageRect(screen, dotfile, (sz * 2), (sz * 2))

        self.build()

    def build(self):
        r = self.brick.rect
        w, h = r.width, r.height
        dx, dy = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'X':
                    self.bricks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                if col == 'g':
                    self.gates.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                if col == 'D':
                    self.dots.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                if col == 'd':
                    self.DOTS.append(pygame.Rect((ncol-.5) * dx, (nrow-.5) * dy, w, h))

    def blitme(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)
        for rect in self.gates:
            self.screen.blit(self.gate.image, rect)
        for rect in self.dots:
            self.screen.blit(self.dot.image, rect)
        for rect in self.DOTS:
            self.screen.blit(self.DOT.image, rect)
