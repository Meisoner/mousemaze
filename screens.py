import pygame as pg

ext = [False, True]
pg.init()
size = (1000, 600)
scr = pg.display.set_mode(size)
font = pg.font.Font(None, 50)
clock = pg.time.Clock()
def gameover():
    txt = font.render('Вы проиграли!', True, (0, 0, 0))
    while True:
        clock.tick(240)
        for i in pg.event.get():
            if i.type == pg.QUIT:
                return True
        scr.fill((150, 150, 150))
        scr.blit(txt, (size[0] // 2 - txt.get_width() // 2, 0))
        pg.display.flip()

def gamestart():
    global scr, size

    txt = font.render('мышку на красный кружочек', True, (0, 0, 0))
    while True:
        clock.tick(240)
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