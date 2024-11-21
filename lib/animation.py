import pygame


class Animation:
    def __init__(self, sprite):
        self.sprite = sprite
        self.anims = {}

        self.frame = 0
        self.frames = []

        self._curr = 0
        self._prev = 0
        self._rate = 0

    def add(self, name, frames, rate):
        anim = self.anims[name] = {}
        anim['frames'] = []
        anim['rate'] = rate

        for frame in frames:
            anim['frames'].append(self.sprite.frame(frame, (255, 0, 255)))


    def play(self, name):
        frames = self.anims[name]['frames']

        if self.frames is not frames:
            self.frame = 0
            self.frames = frames

            self._curr = 0
            self._prev = 0
            self._rate = self.anims[name]['rate']

    def update(self):
        self._curr = pygame.time.get_ticks()

        if self._curr - self._prev > self._rate:
            self._prev = self._curr
            self.frame = (self.frame + 1) % len(self.frames)
