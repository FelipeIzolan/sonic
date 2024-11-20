import pygame
from lib.entity import Entity


class Player(Entity):
    def __init__(self, game):
        super().__init__(game, 'player', 56, 64)

        self.anim.add(
            'idle',
            (
                pygame.Rect(0, 0, 16, 16),
                pygame.Rect(16, 0, 16, 16)
            ),
            400,
            True
        )

        self.anim.add(
            'walk',
            (
                pygame.Rect(0, 16,  16, 16),
                pygame.Rect(16, 16, 16, 16),
                pygame.Rect(32, 16, 16, 16),
                pygame.Rect(48, 16, 16, 16)
            ),
            200
        )

        self.anim.add(
            'run',
            (
                pygame.Rect(0, 32,  16, 16),
                pygame.Rect(16, 32, 16, 16),
                pygame.Rect(32, 32, 16, 16),
                pygame.Rect(48, 32, 16, 16)
            ),
            100
        )

    def _keypress(self, keys):
        if keys[pygame.K_RIGHT]:
            self.pos.x += 1
            self.flipX = False
            self.anim.play('walk')
        elif keys[pygame.K_LEFT]:
            self.pos.x -= 1
            self.flipX = True
            self.anim.play('walk')
        else:
            self.anim.play('idle')

    def _update(self):
        super()._update()

    def _draw(self):
        super()._draw()
