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

        self.player = Player()

    def start(self):
        while not self.quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True

            keys = pygame.key.get_pressed()

            self.player.keypress(keys)
            self.player.update()

            self.screen.fill(BACKGROUND)
            self.player.draw(self.screen)
            pygame.display.update()

            self.delta = self.clock.tick(30) / 1000


game = Game()
game.start()
