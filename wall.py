import pygame as pg
from screens import gameover, status


class Wall(pg.sprite.Sprite):
    def __init__(self, group, x, y, vert, length):
        super().__init__(group)
        if vert:
            self.image = pg.Surface((10, length * 10))
        else:
            self.image = pg.Surface((length * 10, 10))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self, mx, my):
        if self.rect[0] <= mx <= self.rect[0] + self.rect[2] and self.rect[1] <= my <= self.rect[1] + self.rect[3]:
            status[0] = gameover(False)