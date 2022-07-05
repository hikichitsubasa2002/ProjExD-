import tkinter as tk
import tkinter.messagebox as tkm
import pygame as pg
import random
import sys



def main():
    global tmr,tms
    clock = pg.time.Clock()
    # 練習１
    pg.display.set_caption('にげろ')
    screen_sfc = pg.display.set_mode((1400,800))#Surface
    screen_rct = screen_sfc.get_rect()          #rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")  #Surface
    bgimg_rct = bgimg_sfc.get_rect()            #rect
    screen_sfc.blit(bgimg_sfc,bgimg_rct)
    #練習３
    kkimg_sfc = pg.image.load("fig/6.png")      #Surface
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc,0,2.0) #Surface
    kkimg_rct = kkimg_sfc.get_rect()            #rect
    kkimg_rct.center = 900, 400

    # 練習５　：　爆弾
    bmimg_sfc = pg.Surface((20,20))
    bmimg_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bmimg_sfc,(255,0,0),(10,10),10)
    bmimg_rct = bmimg_sfc.get_rect() #rect
    bmimg_rct.centery = random.randint(0,screen_rct.width)
    bmimg_rct.centery = random.randint(0,screen_rct.height)
    #練習６
    vx,vy = +1,+1

    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)
        #練習２
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        #練習4 移動
        key_states = pg.key.get_pressed()#辞書
        if key_states[pg.K_UP]    == True: kkimg_rct.centery -= 1
        if key_states[pg.K_DOWN]  == True: kkimg_rct.centery += 1
        if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx -= 1
        if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx += 1
        #練習７
        if check_bound(kkimg_rct,screen_rct) !=(1,1):#領域外
            if key_states[pg.K_UP]    == True: kkimg_rct.centery += 10
            if key_states[pg.K_DOWN]  == True: kkimg_rct.centery -= 10
            if key_states[pg.K_LEFT]  == True: kkimg_rct.centerx += 10
            if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx -= 10
        
        screen_sfc.blit(kkimg_sfc,kkimg_rct)
        screen_sfc.blit(bmimg_sfc,bmimg_rct)
        #練習６
        bmimg_rct.move_ip(vx,vy)
        #練習７
        yoko,tate = check_bound(bmimg_rct,screen_rct)
        vx *= yoko
        vy *= tate 

        #練習8
        if kkimg_rct.colliderect(bmimg_rct):return 
            

        pg.display.update()
        clock.tick(1000)

def check_bound(rct,scr_rct):
    '''

    '''
    yoko,tate = +1,+1
    if rct.left < scr_rct.left or scr_rct.right < rct.right: yoko *= -1.2 
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom: tate *= -1.2
    return yoko,tate

 

if __name__ == "__main__":
    pg.init()
    main()
    tkm.showerror(tkm.showerror("まけ","　　　　　　　　　　　　　　　 ,, -―-、\n　　　　　　　　　　　　　／　　　　 ヽ　　　　　　　／￣￣／　　／i⌒ヽ､|　　　　オエーー！！！！\n　　　　　　/　　（゜）/　　 ／　/\n　　　　　/　　　　 ト､.,../　,ー-､\n　　　　=彳　　　　　 ＼＼‘ﾟ。､｀ ヽ。、ｏ\n　　　　/ 　 　　　　　　　＼＼ﾟ。､。、ｏ\n      /                                       /⌒ ヽ ヽU     ｏ\n     /                                            │　    `ヽU  ∴ｌ\n    │　                                           │　        U  ：l\n|：!\n                                        Ｕ\n"))
    pg.quit()
    sys.exit()