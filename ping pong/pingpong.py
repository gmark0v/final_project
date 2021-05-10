from pygame import *
from random import randint
pl1numbr = 0
pl2numbr = 0
#?окно и фпс
fpsiki = time.Clock()
FPS = 60
okno = display.set_mode((700, 500))
#?фон
background = transform.scale(image.load("FON.png"), (700, 500))
#?классы
class objekt(sprite.Sprite): #*основной класс
    def __init__(self, pic, px, py, ph, pw):    
        super().__init__()
        self.image = transform.scale(image.load(pic), (pw, ph))
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
    def reset(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))
mph = 45
mpw = 45
myach = objekt("ball4ik.png", 300, 200, mpw, mph)
#?
class playir(objekt): #*игрок
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < 480 - 50: #вниз
            self.rect.y += 6
        if keys_pressed[K_w] and self.rect.y > 50 - 50: #вверх
            self.rect.y -= 6
gg = playir("sprite2.png", 25, 100, 65, 65)
#?
class playir2(objekt): #*игрок2
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < 480 - 50: #вниз
            self.rect.y += 6
        if keys_pressed[K_UP] and self.rect.y > 50 - 50: #вверх
            self.rect.y -= 6
g2g = playir2("sprite1.png", 625, 100, 65 ,65)
#?
#cherry = objekt("cherry.png", 345, 200, 45, 45)
#wtrmln = objekt("wtrmln.png", 300, 245, 45, 45)
#apl = objekt("apl.png", 345, 245, 45, 45)
#mrr = objekt("mrr.png", 390, 200, 45, 45)
#! можно вывести надпись с эффектом который сейчас идёт.
#?
bsy = 3.5
bsx = -3.5
#?
font.init() #шрифт
font = font.Font(None, 35)
#?игровой цикл
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
#?функции
    #?
    myach.update()
    myach.reset()
    #?
    gg.update()
    gg.reset()
    #?
    g2g.update()
    g2g.reset()
    #?
    #cherry.update()
    #cherry.reset()
    #?
    #mrr.update()
    #mrr.reset()
    #?
    #apl.update()
    #apl.reset()
    #?
    #wtrmln.update()
    #wtrmln.reset()
    #?
    display.update()
    #?
    txt = "Забито игроком 1: "+ str(pl1numbr) #счётчик сбитого
    antitxt = "Забито игроком 2: "+ str(pl2numbr) #счётчик сбитого но телом
    ruwon = font.render(txt, True, (255, 255, 255))
    los = font.render(antitxt, True, (255, 255, 255))
    okno.blit(ruwon, (0, 0))
    okno.blit(los, (0, 30))
    #?
    if sprite.collide_rect(myach, gg): #столкновение мяча и игрока (слево)
        bsx *= -1
        bsy *= -1
    if sprite.collide_rect(myach, g2g): #столкновение мяча и игрока2 (справо)
        bsx *= -1
        bsy *= -1
    #?
    #if sprite.collide_rect(myach, mrr): #столкновение мяча и зеркала
    #    bsx *= -1
    #    bsy *= -1
    #if sprite.collide_rect(myach, wtrmln): #столкновение мяча и арбуза
    #    mph *= 1.25
    #    mph *= 1.25
    #    bsy *= 0.75
    #    bsx *= 0.75
    #if sprite.collide_rect(myach, alp): #столкновение мяча и яблока
    #    mph *= 0.75
    #    mph *= 0.75
    #    bsy *= 1.25
    #    bsx *= 1.25
    #?
    if myach.rect.x > g2g.rect.x + 75:
        myach.rect.x = 300
        myach.rect.y = 200
        pl1numbr += 1
    if myach.rect.x < gg.rect.x - 75:
        myach.rect.x = 300
        myach.rect.y = 200
        pl2numbr += 1
    #?
    ulos = font.render("Игрок 1 проиграл", True, (255, 255, 255))
    ulos2 = font.render("Игрок 2 проиграл", True, (255, 255, 255))
    #?
    if pl1numbr == 3: #победа игрока 1
        fin = True
        while fin:
            okno.fill((0, 0, 0))
            okno.blit(ulos, (100,100))
            display.update()
            for e in event.get():
                if e.type == QUIT:
                    gm = False
                    fin = False
    #?
    if pl2numbr == 3: #проигрыш игркока 1
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
    #?
    display.update()
    fpsiki.tick(FPS) 