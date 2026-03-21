import pygame as pg

# Переменная статуса игры
# Во второй ячейке указано, включён ли усложнённый режим
# Смысл начений в первой:
# 0 - игра запущена, 1 - повторить уровень заново, 2 - создать новый уровень, 3 - выйти из игры
status = [2, False]
pg.init()
size = (1000, 600)
scr = pg.display.set_mode(size)
font = pg.font.Font(None, 50)
clock = pg.time.Clock()
def gameover(win):
    if win:
        title = 'Вы выиграли!'
    else:
        title = 'Вы проиграли :('
    txt = font.render(title, True, (0, 0, 0))
    buttons = ['', 'Выйти', '']
    if win:
        buttons[0] = 'Следующий'
        if not status[1]:
            buttons[2] = 'Сложнее!'
    else:
        buttons[0] = 'Ещё раз'
        if status[1]:
            buttons[2] = 'Легче'
    rend_buttons = []
    for i in buttons:
        rend_buttons += [font.render(i, True, (255, 255, 255))]
    while True:
        clock.tick(240)
        scr.fill((150, 150, 150))
        scr.blit(txt, (size[0] // 2 - txt.get_width() // 2, 0))
        pg.draw.rect(scr, (50, 50, 50), (150, 200, 250, 60))
        scr.blit(rend_buttons[0],
                 (150 + (250 - rend_buttons[0].get_width()) // 2, 200 + (60 - rend_buttons[0].get_height()) // 2))
        pg.draw.rect(scr, (50, 50, 50), (size[0] - 400, 200, 250, 60))
        scr.blit(rend_buttons[1],(size[0] - 400 + (250 - rend_buttons[1].get_width()) // 2,
                  200 + (60 - rend_buttons[1].get_height()) // 2))
        if buttons[2]:
            pg.draw.rect(scr, (50, 50, 50), (size[0] // 2 - 125, 320, 250, 60))
            scr.blit(rend_buttons[2], (size[0] - 400 + (250 - rend_buttons[2].get_width()) // 2,
                                       200 + (60 - rend_buttons[2].get_height()) // 2))
        for i in pg.event.get():
            if i.type == pg.QUIT:
                return 3
            if i.type == pg.MOUSEBUTTONDOWN:
                mx, my = i.pos
                if 150 <= mx <= 400 and 200 <= my <= 260:
                    if win:
                        return 2
                    else:
                        return 1
                if size[0] - 400 <= mx <= size[0] - 150 and 200 <= my <= 260:
                    return 3
                if buttons[2] and size[0] // 2 - 125 <= mx <= size[0] // 2 + 125 and 320 <= 380:
                    status[1] = not status[1]
                    return 2
        pg.display.flip()

def gamestart():
    global scr, size

    txt = font.render('мышку на красный кружочек', True, (0, 0, 0))
    while True:
        clock.tick(240)
        for i in pg.event.get():
            if i.type == pg.QUIT:
                return 3
            if i.type == pg.MOUSEMOTION:
                mx, my = i.pos
                if 0 <= mx <= 50 and 0 <= my <= 50:
                    return 0
        scr.fill((150, 150, 150))
        scr.blit(txt, (0, 100))
        pg.draw.ellipse(scr, (255, 0, 0), (0, 0, 50, 50))
        pg.display.flip()