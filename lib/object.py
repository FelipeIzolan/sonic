# requires
# - sprite.py
# - animation.py (optional)

import pygame


class Object:
    def __init__(self, x, y, sprite, animation):
        self.position = pygame.math.Vector2(x, y)

        self.flipX = False
        self.flipY = False
        self.angle = 0

        self.sprite = sprite
        self.animation = animation

    def update(self):
        if self.animation:
            self.animation.update()

    def draw(self, screen):
        sprite = \
            self.sprite if not self.animation else \
            self.animation.frames[self.animation.frame]

        if self.flipX or self.flipY:
            sprite = pygame.transform.flip(sprite, self.flipX, self.flipY)

        if self.angle != 0:
            sprite = pygame.transform.rotate(sprite, self.angle)

        screen.blit(sprite, self.position)
