# requires
# - sprite.py

import pygame
import csv


class Tile:
    def __init__(self, rect, sprite):
        self.rect = rect
        self.mask = Tile._mask(rect, sprite)
        self.angle = self.mask.angle()  # <- change

    @staticmethod
    def _mask(rect, sprite):
        mask = pygame.mask.Mask(rect.size)
        colorkey = sprite.get_colorkey()

        for y in range(rect.height):
            for x in range(rect.width):
                color = sprite.get_at((rect.x + x, rect.y + y))

                if color != colorkey:
                    mask.set_at((x, y))

        return mask


class TileMap:
    def __init__(self, width, height, sprite):
        self.sprite = sprite
        self.tiles = []

        self.width = width
        self.height = height

        self.surface = None
        self.matrix = None

        for y in range(self.sprite.get_height() // height):
            for x in range(self.sprite.get_width() // width):
                self.tiles.append(
                    Tile(
                        pygame.Rect(x * width, y * height, width, height),
                        sprite
                    )
                )

    def from_matrix(self, matrix):
        self.matrix = matrix
        self.surface = pygame.Surface(
            (
                self.width * len(matrix[0]),
                self.height * len(matrix)
            )
        )

        self.surface.fill((255, 0, 255))
        self.surface.set_colorkey(self.sprite.get_colorkey())

        for y, row in enumerate(matrix):
            for x, col in enumerate(row):
                if col == -1:
                    continue

                tile = self.tiles[col]
                self.surface.blit(
                    self.sprite,
                    (x * 16, y * 16),
                    tile.rect
                )

    def from_csv(self, filename):
        file = open(filename)
        reader = csv.reader(file)
        matrix = []

        for y, row in enumerate(reader):
            matrix.append([])
            for col in row:
                matrix[y].append(int(col))

        self.from_matrix(matrix)
