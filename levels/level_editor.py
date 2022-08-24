#!/bin/python3

import pygame
import json
pygame.init()

width,heigth=900,700


win=pygame.display.set_mode((width,heigth))
pygame.display.set_caption("level editor for tank game")


#colors
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
green=(0,255,0)
red=(255,0,0)


walls=[]#all walls in the map
savedict={}#walls that are saved when the s key is pressed 


class wall:
    def __init__(self,x,y,w,h,name):
        self.x=x
        self.y=y
        self.w=w#width
        self.h=h#height
        self.name=name
        self.xp=x#x and y placeholder 
        self.yp=y#for testing but if this works im not going to change any names


    def render(self):#renders 
        rect=pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(win,black,rect)



    def setsize(self,mousex,mousey,bol):
        #this entire function updates the walls position while the mouse is moving
        #
        #
        if bol==1:
            self.xp=mousex
            self.yp=mousey
        if bol==2:
            if self.xp-mousex>=0:#if we do a reverse
                self.x=mousex
                self.w=self.xp-mousex
            else:
                self.w=mousex-self.xp
                self.x=self.xp

            if self.yp-mousey>=0:
                self.y=mousey
                self.h=self.yp-mousey
            else:
                self.h=mousey-self.yp
                self.y=self.yp


    def adwal(self):#adds the wall object to savedict
        savedict[self.name]=[self.x, self.y, self.w, self.h, self.name]





class user_interface:
    def __init__(self):
        self.ChosenObject = "wall"
        #^^ this is what determines wheather we are placing a wall or a player spawn point
        self.BoxSize=35
        self.UiBg=pygame.Rect(0,600,width,100)
        
        self.p1_btn={"x":0,
                "y":600,
                "w":self.BoxSize,
                "h":self.BoxSize,
                }
 
        self.p2_btn={"x":width-self.BoxSize,
                "y":600,
                "w":self.BoxSize,
                "h":self.BoxSize,
                }

        self.wall_btn={"x":width/2-self.BoxSize,
                "y":600,
                "w":self.BoxSize,
                "h":self.BoxSize,
                }

        


        self.player1_btn=pygame.Rect(self.p1_btn["x"],self.p1_btn["y"],self.p1_btn["w"],self.p1_btn["h"])
        self.player2_btn=pygame.Rect(self.p2_btn["x"],self.p2_btn["y"],self.p2_btn["w"],self.p2_btn["h"])
        self.wall_btnrect=pygame.Rect(self.wall_btn["x"],self.wall_btn["y"],self.wall_btn["w"],self.wall_btn["h"])


    def render(self):
        #render buttons or something 
        pygame.draw.rect(win,green,self.UiBg)    

        pygame.draw.rect(win,red,self.player1_btn)
        pygame.draw.rect(win,blue,self.player2_btn)
        pygame.draw.rect(win,black,self.wall_btnrect)


    def use_buttons(self,x,y):
        #given x and y the function changes chosen object  
        if x>=self.p1_btn["x"] and x<=self.p1_btn["w"]:
            if  y>=self.p1_btn["y"] and y<=self.p1_btn["y"]+self.p1_btn["h"]:
                self.ChosenObject="p1"


        if x>=self.p2_btn["x"] and x<=self.p2_btn["x"]+self.p2_btn["w"]:
            if  y>=self.p2_btn["y"] and y<=self.p2_btn["y"]+self.p2_btn["h"]:
                self.ChosenObject="p2"

        if x>=self.wall_btn["x"] and x<=self.wall_btn["x"]+self.wall_btn["w"]:
            if  y>=self.wall_btn["y"] and y<=self.wall_btn["y"]+self.wall_btn["h"]:
                self.ChosenObject="wall"
        print(self.ChosenObject)
       




def obj_placement(ui):

    if ui.ChosenObject=="p1":
        print("p1")
        return
    if ui.ChosenObject=="p1":
        print("p2")
        return
    bol+=1#we should not add more wall objcts white we are trying to make the first one

    if bol ==1:
        runval+=1
        walls.append(runval)
        walls[walls.index(runval)]=wall(0,0,0,0,runval)



class playerObject:
    def __init__(self,x,y,color,name):
        self.name=name
        self.x=x
        self.y=y
        self.color=color
    def render(self):#renders
        player=pygame.Rect(self.x,self.y,35,35)
        pygame.draw.rect(win,self.color,player)

    def adPlayer(self):#adds the player object to savedict
        savedict[self.name]=[self.x, self.y,self.name]

def main():
    print("press the s key to save the game level to gamelevel.json")
    print("place the gamelevel.json to the same file as the main game file to play your map")

    ui=user_interface()

    player1=playerObject(225,150,red,"p1")
    player2=playerObject(675,150,blue,"p2")

    bol=0
    run=True
    win.fill(white)
    runval=0
    while run:
        win.fill(white)
        for obs in walls:
            obs.render()
        player1.render()
        player2.render()
        ui.render()
        pygame.display.update()



        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
    

                mx,my=pygame.mouse.get_pos()
                if my >=600:
                    ui.use_buttons(mx,my)
                    #mover these to else statement
                    if ui.ChosenObject=="p1":
                        print("p1")
                    if ui.ChosenObject=="p2":
                        print("p2")

                else:
                    if ui.ChosenObject=="p1":
                        player1.x=mx
                        player1.y=my
                    if ui.ChosenObject=="p2":
                        player2.x=mx
                        player2.y=my
                    if ui.ChosenObject=="wall":
                        bol+=1#we should not add more wall objcts white we are trying to make the first one

                        if bol ==1:
                            runval+=1
                            walls.append(runval)
                            walls[walls.index(runval)]=wall(0,0,0,0,runval)
                



            if event.type==pygame.KEYDOWN:
                if event.key ==pygame.K_s:
                    player1.adPlayer()
                    player2.adPlayer()
                    for thing in walls:
                        thing.adwal()
                        print(savedict,"has ben saved")
                    f=open("gamelevel.json","w")
                    jison=json.dumps(savedict)
                    f.write(jison)
                    f.close()
        if bol==3:
            bol =0

        if len(walls)>=1:
            mx,my=pygame.mouse.get_pos()
            walls[runval-1].setsize(mx,my,bol)

        if bol ==1:#dirty fix for less button presses.
            bol+=1


    pygame.quit()

if __name__=="__main__":
    main()
