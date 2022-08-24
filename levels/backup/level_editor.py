#!/bin/python3

import pygame
import json
pygame.init()

width,heigth=900,600


win=pygame.display.set_mode((width,heigth))
pygame.display.set_caption("level editor for tank game")

#colors
white=(255,255,255)
black=(0,0,0)


walls=[]
savedict={}


class wall:
    def __init__(self,x,y,w,h,name):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.name=name
        #savedict[str(name)]=[self.x,self.y,self.w,self.h]


    def render(self):
        rect=pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(win,black,rect)



    def setsize(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h



    def adwal(self):
        savedict[self.name]=[self.x, self.y, self.w, self.h, self.name]




def main():
    bol=False
    run=True
    win.fill(white)
    runval=0
    x1=0
    y1=0

    while run:
        for obs in walls:
            obs.render()
        

        jison=json.dumps(savedict)
        pygame.display.update()


           


        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                runval+=1#dont use waiting wall or anythng like that 
                #just add it into the wall list and update its w,h when mouse buttonup is triggered.
                mousex,mousey=pygame.mouse.get_pos()
                x1=mousex
                y1=mousey




            if event.type==pygame.MOUSEBUTTONUP:# redo this
                #do calculation to see if width or hiehgt is a minus number
                mousex,mousey=pygame.mouse.get_pos()
                x=0
                w=0
                y=0
                h=0
                if mousex-x1<=0:
                    x=mousex
                    w=x1-mousex
                else:
                    x=x1
                    w=mousex-x1

                if mousey-y1<=0:
                    y=mousey
                    h=y1-mousey
                else:
                    y=y1
                    h=mousey-y1
                    
                walls.append(runval)
                walls[walls.index(runval)]=wall(x,y,w,h,runval)
                #walls[runval-1].setsize(mousex,mousey)
                walls[runval-1].adwal()
                


            if event.type==pygame.KEYDOWN:
                if event.key ==pygame.K_s:


                    f=open("gamelevel.json","w")

                    f.write(jison)
                    f.close()


                #print(savedict)
            if event.type==pygame.QUIT:
                #print(savedict)
                run=False


    pygame.quit()

if __name__=="__main__":
    main()
