import pygame
from utils import COLORKEY


class Animation:
    def __init__(self, entity):
        self.entity = entity

        self.anims = {}
        self.frame = 0
        self.frames = []

        self._curr = 0
        self._prev = 0
        self._rate = 0

    def add(self, name, frames, rate, default=False):
        anim = self.anims[name] = {}
        anim['frames'] = []
        anim['rate'] = rate

        for frame in frames:
            surface = pygame.Surface(frame.size)
            surface.blit(self.entity.sprite, (0, 0), frame)
            surface.set_colorkey(COLORKEY)
            anim['frames'].append(surface)

        if default:
            self.play(name)

    def play(self, name):
        if self.frames is not self.anims[name]['frames']:
            self.frame = 0
            self.frames = self.anims[name]['frames']

            self._curr = 0
            self._prev = 0
            self._rate = self.anims[name]['rate']

    def _update(self):
        self._curr = pygame.time.get_ticks()

        if self._curr - self._prev > self._rate:
            self._prev = self._curr
            self.frame = (self.frame + 1) % len(self.frames)


class Entity:
    def __init__(self, game, sprite, x, y) -> None:
        self.game = game
        self.sprite = game.sprites[sprite]

        self.pos = pygame.Vector2(x, y)
        self.vel = pygame.Vector2(0, 0)

        self.flipX = False
        self.flipY = False
        self.angle = 0

        self.anim = Animation(self)

    def _update(self):
        self.anim._update()

    def _draw(self):
        frame = self.anim.frames[self.anim.frame]

        if self.flipX or self.flipY:
            frame = pygame.transform.flip(frame, self.flipX, self.flipY)
        if self.angle != 0:
            frame = pygame.transform.rotate(frame, self.angle)

        self.game.screen.blit(frame, self.pos)
