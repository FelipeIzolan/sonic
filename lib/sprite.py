import pygame
from utils import asset


class Sprite:
    def __init__(self, surface, colorkey=None) -> None:
        self.surface = surface

        if colorkey:
            self.surface.set_colorkey(colorkey, pygame.RLEACCEL)

    def frame(self, rect, colorkey=None):
        surface = pygame.Surface(rect.size)
        surface.blit(self.surface, (0, 0), rect)

        return Sprite(surface, colorkey)

    @staticmethod
    def from_filename(filename, colorkey=None):
        surface = pygame.image.load(asset(filename)).convert()
        return Sprite(surface, colorkey)
