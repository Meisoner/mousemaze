from screens import *
from random import randrange as rand
from wall import Wall

mx, my = 0, 0
walls = pg.sprite.Group()
ext[0] = gamestart()
grid = size[0] // 10, size[1] // 10
for x in range(grid[0]):
    for y in range(grid[1]):
        if x <= 7 and y <= 7 or x >= grid[0] - 10 and y >= grid[1] - 10:
            continue
        if ext[1]:
            if x <= 20 and y <= 20 or x >= grid[0] - 20 and y >= grid[1] - 20:
                chance = 16
            else:
                chance = 11
        else:
            chance = 17
        if not rand(chance):
            Wall(walls, x * 10, y * 10, rand(2), 2 + rand(5))
while not ext[0]:
    clock.tick(240)
    scr.fill((150, 150, 150))
    walls.draw(scr)
    pg.display.flip()
    for i in pg.event.get():
        if i.type == pg.QUIT:
            ext = True
        if i.type == pg.MOUSEMOTION:
            mx, my = i.pos
            walls.update(mx, my)
            if mx == 0 or mx == size[0] - 1 or my == 0 or my == size[1] - 1:
                ext[0] = gameover()