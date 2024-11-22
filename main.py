import pygame
from lib.sprite import Sprite
from utils import BACKGROUND, asset
from src.player import Player
from lib.tilemap import TileMap


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (256, 256), pygame.SCALED)  # 256,224

        self.quit = False
        self.delta = 0.0

        self.player = Player()
        self.tilemap = TileMap(
            16,
            16,
            Sprite.from_filename(asset('tilemap.bmp'), (255, 0, 255)),
        )

        self.tilemap.from_csv(asset('level.csv'))

    def start(self):
        while not self.quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True

            keys = pygame.key.get_pressed()

            self.player.keypress(keys)
            self.player.update()

            self.screen.fill(BACKGROUND)
            self.screen.blit(self.tilemap.surface, (0, 0))
            self.player.draw(self.screen)
            pygame.display.update()

            self.delta = self.clock.tick(30) / 1000


game = Game()
game.start()
