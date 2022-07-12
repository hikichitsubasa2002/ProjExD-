from cmath import rect
import pygame as pg
import sys
import random

class Screen:
    def __init__(self,title, wh, image): 
         # 練習1：スクリーンと背景画像
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect

    def blit(self):    
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

class Bird:
    def __init__(self, image:str, size, xy):
        # 練習3：こうかとん
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy
    
    def blit(self,scr:Screen):
        # screen_sfc.blit(kkimg_sfc, kkimg_rct)
        scr.sfc.blit(self.sfc,self.rct)
    
    def update(self, scr:Screen):
        # 練習4
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]:
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]:
            self.rct.centery += 1
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]:
            self.rct.centerx += 1
        # 練習7
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]:
                self.rct.centery += 1
            if key_states[pg.K_DOWN]:
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]: 
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                self.rct.centerx -= 1
        self.blit(scr)

class Bomb:
    def __init__(self, color, size, vxy, scr):
            # 練習5：爆弾
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self, scr:Screen):
        # 練習6
        self.rct.move_ip(self.vx, self.vy)
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        # 練習5
        self.blit(scr)

"""花を打ち出すクラス"""
class Frowe_up:
    def __init__(self, chr: Bird):
        self.sfc = pg.image.load("fig/flower_syokudaiookonnyaku.png")
        self.sfc = pg.transform.rotozoom(self.sfc,0,0.6)
        self.rct = self.sfc.get_rect()
        self.rct.center = chr.rct.center
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr:Screen):
        self.rct.move_ip(0,-3)
        self.blit(scr)

class Frowe_d:
    def __init__(self, chr: Bird):
        self.sfc = pg.image.load("fig/nenga_mark03_ume.png")
        self.sfc = pg.transform.rotozoom(self.sfc,0,0.6)
        self.rct = self.sfc.get_rect()
        self.rct.center = chr.rct.center
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr:Screen):
        self.rct.move_ip(0,3)
        self.blit(scr)

class Frowe_l:
    def __init__(self, chr: Bird):
        self.sfc = pg.image.load("fig/flower_denfare.png")
        self.sfc = pg.transform.rotozoom(self.sfc,0,0.5)
        self.rct = self.sfc.get_rect()
        self.rct.center = chr.rct.center
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr:Screen):
        self.rct.move_ip(3,0)
        self.blit(scr)

class Frowe_r:
    def __init__(self, chr: Bird):
        self.sfc = pg.image.load("fig/flower_himawari_mark.png")
        self.sfc = pg.transform.rotozoom(self.sfc,0,0.7)
        self.rct = self.sfc.get_rect()
        self.rct.center = chr.rct.center
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr:Screen):
        self.rct.move_ip(3,0)
        self.blit(scr)

#音楽が流れる
def bgm():
    pg.mixer.music.load("fig/famipop3.mp3")
    pg.mixer.music.play(loops=-1,start=0.0)


def main():
    clock = pg.time.Clock()

    # # 練習1：スクリーンと背景画像
    scr = Screen("逃げろ！こうかとん",(1400,800),"fig/pg_bg.jpg")

    # # 練習3：こうかとん
    kkt = Bird("fig/6.png",2.0,(900,400))

    # # 練習5：爆弾
    # vx, vy = +1, +1 # 練習6
    bkb = Bomb((255,0,0),10,(+1,+1),scr)
    beams = Frowe_up(kkt)
    ume   = Frowe_d(kkt)
    dnf   = Frowe_l(kkt)
    hima  = Frowe_r(kkt)

    while True:
        scr.blit()
        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_w:
                beams  = Frowe_up(kkt)#上に打ち出す
            elif event.type == pg.KEYDOWN and event.key == pg.K_s:
                ume = Frowe_d(kkt)    #下に打ち出す
            elif event.type == pg.KEYDOWN and event.key == pg.K_d:
                dnf = Frowe_l(kkt)    #右に打ち出す
            elif event.type == pg.KEYDOWN and event.key == pg.K_a:
                hima = Frowe_r(kkt)   #左に打ち出す
        
        kkt.update(scr)
        bkb.update(scr)
        if beams !=0:
            beams.update(scr)
        if ume !=0:
            ume.update(scr)
        if ume !=0:
            dnf.update(scr)
        if ume !=0:
            hima.update(scr)
        
        
        # 練習8
        if kkt.rct.colliderect(bkb.rct):
            return
        pg.display.update()
        clock.tick(1000)


# 練習7
def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate



if __name__ == "__main__":
    pg.init()
    main()
    
    pg.quit()
    sys.exit()