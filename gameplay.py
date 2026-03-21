from screens import *
from random import randrange as rand
from wall import Wall

pg.display.set_caption('Mouse maze')
mx, my = 0, 0
walls = pg.sprite.Group()
grid = size[0] // 10, size[1] // 10
while status[0] != 3:
    if status[0] == 2:
        walls.empty()
        for x in range(grid[0]):
            for y in range(grid[1]):
                if x <= 7 and y <= 7 or x >= grid[0] - 10 and y >= grid[1] - 10:
                    continue
                if status[1]:
                    if x <= 20 and y <= 20 or x >= grid[0] - 20 and y >= grid[1] - 20:
                        chance = 16
                    else:
                        chance = 11
                else:
                    chance = 19
                if not rand(chance):
                    Wall(walls, x * 10, y * 10, rand(2), 2 + rand(5))
    status[0] = gamestart()
    while status[0] == 0:
        clock.tick(240)
        scr.fill((150, 150, 150))
        walls.draw(scr)
        pg.draw.ellipse(scr, (0, 0, 200), (size[0] - 50, size[1] - 50, 50, 50))
        pg.display.flip()
        for i in pg.event.get():
            if i.type == pg.QUIT:
                status[0] = 3
            if i.type == pg.MOUSEMOTION:
                mx, my = i.pos
                if mx >= size[0] - 50 and my >= size[1] - 50:
                    status[0] = gameover(True)
                walls.update(mx, my)
                if mx == 0 or mx == size[0] - 1 or my == 0 or my == size[1] - 1:
                    status[0] = gameover(False)