import pygame
import os

from utils import ADIR, BACKGROUND
from src.player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((256, 224), pygame.SCALED)

        self.quit = False
        self.delta = 0.0

        self.sprites = {}
        self.load('player', 'sonic.bmp')

        self.player = Player(self)

    def load(self, key, filename):
        ext = os.path.splitext(filename)[1]

        if ext in ('.bmp'):
            path = os.path.join(ADIR, filename)
            self.sprites[key] = pygame.image.load(path).convert()
#             self.sprites[key].set_colorkey(COLORKEY, pygame.RLEACCEL)

    def start(self):
        while not self.quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True

            keys = pygame.key.get_pressed()

            self.player._keypress(keys)
            self.player._update()

            self.screen.fill(BACKGROUND)
            self.player._draw()
            pygame.display.update()

            self.delta = self.clock.tick(30) / 1000


game = Game()
game.start()
