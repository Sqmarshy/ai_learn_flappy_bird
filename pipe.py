import pygame
import random
import os

pipe_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","pipe.png")).convert_alpha())

class Pipe():
    GAP = 200
    WIDTH = pipe_img.get_width()
    VEL = 6

    def __init__(self, x):
        self.x = x
        self.added = False

        self.PIPE_TOP = pygame.transform.flip(pipe_img, False, True)
        self.top = 0

        self.PIPE_BOTTOM = pipe_img
        self.bottom = 0

        self.set_height()

    def set_height(self):
        self.bottom = random.randrange(50 + self.GAP, 510)
        self.top = self.bottom - self.GAP - self.PIPE_TOP.get_height()

    def move(self):
        self.x -= self.VEL

    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))
