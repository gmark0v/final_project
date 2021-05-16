from pygame import *
from random import randint
pl1numbr = 0
pl2numbr = 0
#?# окно и фпс
fpsiki = time.Clock()
FPS = 60
okno = display.set_mode((700, 500))
#?# фон
background = transform.scale(image.load("FON.png"), (700, 500))
#?# классы
#?# основной класс
class objekt(sprite.Sprite): 
    def __init__(self, pic, px, py, ph, pw):    
        super().__init__()
        self.image = transform.scale(image.load(pic), (pw, ph))
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
    def reset(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))
myach = objekt("ball4ik.png", 300, 200, 45, 45)
#?# игрок
class playir(objekt): 
    def update(self):
        keys_pressed = key.get_pressed()
        #?# вниз
        if keys_pressed[K_s] and self.rect.y < 480 - 50: 
            self.rect.y += 6
        #?# вверх
        if keys_pressed[K_w] and self.rect.y > 50 - 50: 
            self.rect.y -= 6
gg = playir("sprite2.png", 25, 100, 65, 65)
#?# игрок2
class playir2(objekt): 
    def update(self):
        keys_pressed = key.get_pressed()
        #?# вниз
        if keys_pressed[K_DOWN] and self.rect.y < 480 - 50:
            self.rect.y += 6
        #?# вверх
        if keys_pressed[K_UP] and self.rect.y > 50 - 50: 
            self.rect.y -= 6
g2g = playir2("sprite1.png", 625, 100, 65 ,65)
#?# усилители
wtrmln = objekt("wtrmln.png", 320, 245, 45, 45)
apl = objekt("apl.png", 345, 245, 45, 45)
mrr = objekt("mrr.png", 390, 200, 45, 45)
#?# скорость мяча
bsy = 3.5
bsx = -3.5
#?# шрифт
font.init() 
font = font.Font(None, 35)
#?# игровой цикл
gm = True
while gm:
    myach.rect.x += bsx
    myach.rect.y += bsy
    if myach.rect.y < 0:
        bsy *= -1
    if myach.rect.y > 435:
        bsy *= -1
    okno.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            gm = False
#?# функции
    #?# прорисовка мяча
    myach.update()
    myach.reset()
    #?# прорисовка игрока 1
    gg.update()
    gg.reset()
    #?# прорисовка игрока 2
    g2g.update()
    g2g.reset()
    #?# прорисовка заркала
    mrr.update()
    mrr.reset()
    #?# прорисовка яблока
    apl.update()
    apl.reset()
    #?# прорисовка арбуза
    wtrmln.update()
    wtrmln.reset()
    #?# счётчик сбитого
    txt = "Забито игроком 1: "+ str(pl1numbr)
    #?# счётчик сбитого но 2player
    antitxt = "Забито игроком 2: "+ str(pl2numbr) 
    ruwon = font.render(txt, True, (255, 255, 255))
    los = font.render(antitxt, True, (255, 255, 255))
    okno.blit(ruwon, (0, 0))
    okno.blit(los, (0, 30))
    #?# столкновение мяча и игрока (слево)
    if sprite.collide_rect(myach, gg): 
        bsx *= -1
        bsy *= -1
    #?# столкновение мяча и игрока2 (справо)
    if sprite.collide_rect(myach, g2g): 
        bsx *= -1
        bsy *= -1
    #?# столкновение мяча и зеркала
    if sprite.collide_rect(myach, mrr): 
        bsx *= -1
        bsy *= -1
        mrr.rect.x = randint(70, 600)
        mrr.rect.y = randint(70, 400)
    #?#столкновение мяча и арбуза
    if sprite.collide_rect(myach, wtrmln): 
        bsy *= 0.75
        bsx *= 0.75
        wtrmln.rect.x = randint(70, 600)
        wtrmln.rect.y = randint(70, 400)
    #?# столкновение мяча и яблока
    if sprite.collide_rect(myach, apl): 
        bsy *= 1.25
        bsx *= 1.25
        apl.rect.x = randint(70, 600)
        apl.rect.y = randint(70, 400)
    #?# попадание игркоа 2
    if myach.rect.x > g2g.rect.x + 75:
        myach.rect.x = 300
        myach.rect.y = 200
        pl1numbr += 1
    #?# попадание игрока 1
    if myach.rect.x < gg.rect.x - 75:
        myach.rect.x = 300
        myach.rect.y = 200
        pl2numbr += 1
    #?
    ulos = font.render("Игрок 1 проиграл", True, (255, 255, 255))
    ulos2 = font.render("Игрок 2 проиграл", True, (255, 255, 255))
    #?# победа игрока 1
    if pl1numbr == 3: 
        fin = True
        while fin:
            okno.fill((0, 0, 0))
            okno.blit(ulos, (100,100))
            display.update()
            for e in event.get():
                if e.type == QUIT:
                    gm = False
                    fin = False
    #?# проигрыш игркока 1
    if pl2numbr == 3: 
        game = False
        antifin = True
        while antifin:
            okno.fill((0, 0, 0))
            okno.blit(ulos, (100,100))
            display.update()
            for e in event.get():
                if e.type == QUIT:
                    gm = False
                    antifin = False
    #? конец
    display.update()
    fpsiki.tick(FPS) 