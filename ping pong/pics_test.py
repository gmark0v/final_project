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
        
myach = objekt("ball4ik.png", 300, 200, 45, 45)
cherry = objekt("cherry.png", 345, 200, 45, 45)
wtrmln = objekt("wtrmln.png", 300, 245, 45, 45)
apl = objekt("apl.png", 345, 245, 45, 45)
mrr = objekt("mrr.png", 390, 200, 45, 45)

font.init() #шрифт
font = font.Font(None, 35)

#?игровой цикл
gm = True
while gm:
    okno.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            gm = False
#?функции
    myach.update()
    myach.reset()

    cherry.update()
    cherry.reset()

    mrr.update()
    mrr.reset()

    apl.update()
    apl.reset()

    wtrmln.update()
    wtrmln.reset()

    display.update()
    fpsiki.tick(FPS) 