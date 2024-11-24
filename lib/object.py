# requires
# - sprite.py
# - animation.py (optional)
# - tilemap.py (sensor) (optional)

import pygame


class Object:
    def __init__(self, x, y, hitbox, sprite, animation):
        self.position = pygame.math.Vector2(x, y)

        self.angle = 0
        self.flipX = False
        self.flipY = False
        self.hitbox = hitbox

        self.sprite = sprite
        self.animation = animation

        if animation:
            animation.sprite = sprite

    def update(self):
        if self.animation:
            self.animation.update()

    def draw(self, surface):
        sprite = \
            self.sprite if not self.animation else \
            self.animation.frames[self.animation.frame]

        if self.flipX or self.flipY:
            sprite = pygame.transform.flip(sprite, self.flipX, self.flipY)

        if self.angle != 0:
            sprite = pygame.transform.rotate(sprite, self.angle)

        surface.blit(sprite, self.position)
