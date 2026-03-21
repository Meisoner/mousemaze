import pygame as pg

ext = [False]
pg.init()
size = (1000, 600)
scr = pg.display.set_mode(size)

def gameover():
    return True

def gamestart():
    global scr, size

    font = pg.font.Font(None, 50)
    txt = font.render('мышку на красный кружочек', True, (0, 0, 0))
    while True:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                return True
            if i.type == pg.MOUSEMOTION:
                mx, my = i.pos
                if 0 <= mx <= 50 and 0 <= my <= 50:
                    return False
        scr.fill((150, 150, 150))
        scr.blit(txt, (0, 100))
        pg.draw.ellipse(scr, (255, 0, 0), (0, 0, 50, 50))
        pg.display.flip()