import pygame
from lib.object import Object
from lib.sprite import Sprite
from lib.animation import Animation


class Player(Object):
    def __init__(self):
        self.sprite = Sprite.from_filename('sonic.bmp')
        self.animation = Animation(self.sprite)

        super().__init__(56, 64, self.sprite, self.animation)

        self.animation.add(
            'idle',
            (
                pygame.Rect(0, 0, 16, 16),
                pygame.Rect(16, 0, 16, 16)
            ),
            400,
        )

        self.animation.add(
            'walk',
            (
                pygame.Rect(0, 16,  16, 16),
                pygame.Rect(16, 16, 16, 16),
                pygame.Rect(32, 16, 16, 16),
                pygame.Rect(48, 16, 16, 16)
            ),
            200
        )

        self.animation.add(
            'run',
            (
                pygame.Rect(0, 32,  16, 16),
                pygame.Rect(16, 32, 16, 16),
                pygame.Rect(32, 32, 16, 16),
                pygame.Rect(48, 32, 16, 16)
            ),
            100
        )

        self.animation.play('idle')

    def keypress(self, keys):
        if keys[pygame.K_RIGHT]:
            self.position.x += 1
            self.flipX = False
            self.animation.play('walk')
        elif keys[pygame.K_LEFT]:
            self.position.x -= 1
            self.flipX = True
            self.animation.play('walk')
        else:
            self.animation.play('idle')

    def update(self):
        super().update()

    def draw(self, screen):
        super().draw(screen)
