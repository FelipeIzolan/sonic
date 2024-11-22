import pygame


class Sprite(pygame.Surface):
    def __init__(self, size, colorkey=None):
        super().__init__(size)
        if colorkey:
            self.set_colorkey(colorkey, pygame.RLEACCEL)

    def frame(self, rect):
        colorkey = self.get_colorkey()
        sprite = Sprite(rect.size, colorkey)
        sprite.fill(colorkey, sprite.get_rect())
        sprite.blit(self, (0, 0), rect)

        return sprite

    @staticmethod
    def from_filename(filename, colorkey=None):
        surface = pygame.image.load(filename).convert()
        sprite = Sprite(surface.get_size(), colorkey)
        sprite.blit(surface, (0, 0))
        return sprite
