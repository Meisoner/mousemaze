from screens import *
from random import randrange as rand
from wall import Wall

mx, my = 0, 0
walls = pg.sprite.Group()
ext[0] = gamestart()
for x in range(100):
    for y in range(60):
        if 0 <= x <= 5 and 0 <= y <= 5:
            continue
        if not rand(12):
            Wall(walls, x * 10, y * 10, rand(3), 2 + rand(5))
while not ext[0]:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            ext = True
        if i.type == pg.MOUSEMOTION:
            mx, my = i.pos
            walls.update(mx, my)
            if mx == 0 or mx == size[0] - 1 or my == 0 or my == size[1] - 1:
                ext[0] = gameover()
    scr.fill((150, 150, 150))
    walls.draw(scr)
    pg.display.flip()