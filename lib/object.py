import pygame


class Object:
    def __init__(self, x, y, sprite, animation) -> None:
        self.position = pygame.math.Vector2(x, y)
        self.speed = pygame.math.Vector2(0, 0)

        self.angle = 0
        self.flipX = False
        self.flipY = False

        self.sprite = sprite
        self.animation = animation

    def update(self):
        if self.animation:
            self.animation.update()

    def draw(self, screen):
        sprite = \
            self.sprite if not self.animation else \
            self.animation.frames[self.animation.frame]
        sprite = sprite.surface

        if self.flipX or self.flipY:
            sprite = pygame.transform.flip(sprite, self.flipX, self.flipY)

        if self.angle != 0:
            sprite = pygame.transform.rotate(sprite, self.angle)

        screen.blit(sprite, self.position)
