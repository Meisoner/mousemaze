import pygame as pg

# Переменная статуса игры
# Во второй ячейке указано, включён ли усложнённый режим
# Смысл значений в первой:
# 0 - игра запущена, 1 - повторить уровень заново, 2 - создать новый уровень, 3 - выйти из игры
status = [2, 2]
pg.init()
size = (1000, 600)
scr = pg.display.set_mode(size)
font = pg.font.Font(None, 50)
clock = pg.time.Clock()

# Экран окончания игры
def gameover(win):
    # Сразу две стены могут вызвать этот экран, из-за чего возникает баг поражения сразу после перехода на новый уровень
    # Так мы закрываем экран сразу, если игра уже остановлена
    if status[0]:
        return status[0]
    pg.mixer.music.stop()
    if win:
        title = 'Вы выиграли!'
    else:
        title = 'Вы проиграли :('
    txt = font.render(title, True, (0, 0, 0))
    buttons = ['', '', '']
    if win:
        buttons[0] = 'Следующий'
        buttons[1] = 'Выйти'
        if status[1] == 0:
            buttons[2] = 'Сложнее!'
        elif status[1] == 1:
            buttons[2] = 'Рандом!'
    else:
        if status[1] >= 2:
            buttons[0] = 'Пропустить'
            buttons[1] = 'Выйти'
        else:
            buttons[0] = 'Ещё раз'
            buttons[1] = 'Пропустить'
        if status[1]:
            buttons[2] = 'Легче'
        else:
            buttons[2] = 'Выйти'
    rend_buttons = []
    for i in buttons:
        rend_buttons += [font.render(i, True, (255, 255, 255))]
    levels = ''
    if status[1] >= 2:
        levels = 'Пройденных уровней: ' + str(status[1] - 2 + int(win))
    ltxt = font.render(levels, True, (0, 0, 0))
    while True:
        clock.tick(60)
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
            scr.blit(rend_buttons[2], (size[0] // 2 - 125 + (250 - rend_buttons[2].get_width()) // 2,
                                       320 + (60 - rend_buttons[2].get_height()) // 2))
        scr.blit(ltxt, (0, 300 + int(bool(buttons[2])) * 200))
        for i in pg.event.get():
            if i.type == pg.QUIT:
                return 3
            if i.type == pg.MOUSEBUTTONDOWN:
                mx, my = i.pos
                if 150 <= mx <= 400 and 200 <= my <= 260:
                    if status[1] >= 2:
                        if win:
                            status[1] += 1
                        return 2
                    if win:
                        return 2
                    return 1
                if size[0] - 400 <= mx <= size[0] - 150 and 200 <= my <= 260:
                    if win or status[1] >= 2:
                        return 3
                    return 2
                if buttons[2] and size[0] // 2 - 125 <= mx <= size[0] // 2 + 125 and 320 <= 380:
                    if buttons[2] == 'Выйти':
                        return 3
                    if win:
                        status[1] += 1
                    else:
                        if status[1] > 2:
                            status[1] = 2
                        status[1] -= 1
                    return 2
        pg.display.flip()

# Экран начала игры (чтобы пользователь поставил курсор в нужное положение)
def gamestart():
    global scr, size

    txt = font.render('Мышку на красный кружочек', True, (0, 0, 0))
    while True:
        clock.tick(60)
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
