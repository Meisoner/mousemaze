from screens import *
from random import randrange as rand
from wall import Wall

icon = pg.image.load("banana.png").convert_alpha()
pg.display.set_icon(icon)
pg.display.set_caption('Mouse maze')
walls = pg.sprite.Group()
grid = size[0] // 10, size[1] // 10
while status[0] != 3:
    if status[1] >= 2:
        pg.mixer.music.load('music/random.mp3')
    elif status[1] == 1:
        pg.mixer.music.load('music/hard.mp3')
    else:
        pg.mixer.music.load('music/easy.mp3')
    pg.mixer.music.play(-1)
    vol = 0.3
    if status[1] >= 2:
        vol = 0.7
    pg.mixer.music.set_volume(vol)
    if status[0] == 2:
        # Создаём новый уровень
        walls.empty()
        for x in range(grid[0]):
            for y in range(grid[1]):
                if x <= 7 and y <= 7 or x >= grid[0] - 10 and y >= grid[1] - 10:
                    continue
                if status[1] == 1:
                    # В сложном режиме в начале вероятность появления стены 1/16, потом 1/11
                    if x <= 20 and y <= 20 or x >= grid[0] - 20 and y >= grid[1] - 20:
                        chance = 16
                    else:
                        chance = 11
                elif status[1] >= 2:
                    chance = max(16 - status[1], 9)
                    chch = max(50 - status[1] * 5, 25)
                else:
                    # Если режим лёгкий, то сена появляется с вероятностью 1/19
                    # Оптимальные значения были найдены экспериментально
                    chance = 19
                if not rand(chance):
                    Wall(walls, x * 10, y * 10, rand(2), 2 + rand(5))
    status[0] = gamestart()
    mx, my = -1, -1
    while status[0] == 0:
        tick = clock.tick(240)
        scr.fill((150, 150, 150))
        # Рисуем стены
        walls.draw(scr)
        # Рисуем синий кружок
        pg.draw.ellipse(scr, (0, 0, 200), (size[0] - 50, size[1] - 50, 50, 50))
        pg.display.flip()
        if status[1] >= 2:
            # Шанс изменения увеличивается со временем
            chch -= tick / max(900 - status[1] * 100, 150)
            # В случайном режиме карта меняется прямо во время игры
            if not rand(max(int(chch), 2 + int(status[1] < 8))):
                if rand(2):
                    x, y = rand(grid[0]) * 10, rand(grid[1]) * 10
                    w = Wall(walls, x, y, rand(2), 2 + rand(5))
                    # Проверяем, что новая стена не заставит игрока тут же проиграть
                    if w.inside(mx, my):
                        walls.remove(w)
                elif walls:
                    walls.remove(walls.sprites()[rand(len(walls))])
        for i in pg.event.get():
            if i.type == pg.QUIT:
                status[0] = 3
            if i.type == pg.MOUSEMOTION:
                # Если мышка быстро далеко переместилась, это странно
                if mx != -1 and (abs(i.pos[0] - mx) > 20 or abs(i.pos[1] - my) > 20):
                    status[0] = gameover(False)
                    break
                mx, my = i.pos
                # Случай поражения - выход за пределы экрана
                if mx <= 0 or mx >= size[0] - 1 or my <= 0 or my >= size[1] - 1:
                    status[0] = gameover(False)
                # Случай победы - попадание в синий кружок
                elif mx >= size[0] - 50 and my >= size[1] - 50:
                    status[0] = gameover(True)
                elif status[0] != 2:
                    # Если по результатам предыдущих не надо перерисовывать уровень, передаём координаты стенам
                    walls.update(mx, my)