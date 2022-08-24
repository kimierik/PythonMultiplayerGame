#!/bin/python3
#
#
#


import pygame
import math
import time
import json
#from _thread import *
import threading
from modules import client
from modules import assets
from modules import config
#assents has all classes
#config has global cariables


class p2data:
    def __init__(self):
        self.playerOutputData={'Mpos':[0,0],'fire':0,'MovingTo':[0,0]}


#todo
#clean unused code
#add server feature afterward when everything is more clean

#ip port protocoll
client=client.client(input("give ip addres of server : "),9999,"utf-8")
user2=p2data()



def stopwatch(input_time,refrence_time):#this sees if refrence time has passed since input time was last updated
    if time.time()-input_time>=refrence_time:
        return True
    return False

def checkvalue(value):
    if int(value)==0:
        return 0
    if int(value)>0:
        return 1
    return -1






def load_map():
    #gets mapdata from server
    msg=client.s.recv(1024).decode(client.proto)
    mapdict=json.loads(msg)
    playerdata=[[0,0],[0,0]]
    runval=0

    #parses data
    for thing in mapdict:
        #if it is player
        if thing.isnumeric():

            var=mapdict[str(thing)]
            thing =assets.wall(var[0],var[1],var[2],var[3])
            config.walls.append(thing)
        else:
            playerdata[runval]=mapdict[thing]
            runval=runval+1
    return playerdata





def send_inputs(data):
    client.s.send(json.dumps(data).encode(client.proto))




def ReceiveInput():
    rUn =True
    while rUn:
        try:
            commands=client.s.recv(1024).decode(client.proto)
            #print(commands)
            #print(len(commands),len(json.dumps(user2.playerOutputData))*1.5)
            if len(commands)<len(json.dumps(user2.playerOutputData))*1.5:
     
                command=json.loads(commands)
                #print("update")
                user2.playerOutputData=command
            else:
                pass
        except:
            print("something has failed while processing data, conn terminate by client")
            client.s.close()
            rUn=False



#something is severely fucked with movement
#something takes realtime mouse x,y when moving on multiplayer
#stops moving when y or x is correct otherwise keeps moving realtime
#does not happen on client it self so something is wrong
#idk what


#it migth be calling Goto in realtime and not on mouse press
#but moving to should only be updated when the other client presses mouse
#problem is most likely in modules/assets tank class implementation
#



def main():#main game loop duh

    #setting up random stuff 
    playerInputData={"Mpos":[0,0],"fire":0,"MovingTo":[0,0]}


    playerdata=load_map()
    p1=playerdata[0]#player 1 position is index 0 of playerdata
    p2=playerdata[1]
    user2.playerOutputData["MovingTo"]=p2
    run =True
    config.WIN.fill(config.white)
    test1=assets.tank(p1[0],p1[1],90)
    test2=assets.tank(p2[0],p2[1],180)
    config.playerlist.append(test1)
    config.playerlist.append(test2)
    clock=pygame.time.Clock()

    
    commands=client.s.recv(1024).decode(client.proto)


    thread=threading.Thread(target=ReceiveInput)
    thread.start()

    while run:
        clock.tick(config.fpslimit)


        Mx,My=pygame.mouse.get_pos()
        playerInputData["Mpos"]=[Mx,My]

        config.WIN.fill(config.white)
        for ammo in config.bullets:#calls all bullet functions

            ammo.fly()
            ammo.render()
            ammo.playercollision()
            ammo.terminate()

        for wall in config.walls:
            wall.render()

        for guy in config.playerlist:
            guy.move()    
            guy.render()
            guy.view()


        pygame.display.update()
    

    ## TAKE INPUTS
        #vv takes mouse cpords
        test1.MouseLookAngle([Mx,My])


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
            if event.type==pygame.MOUSEBUTTONUP:
                test1.goto([Mx,My])
                playerInputData["MovingTo"]=[Mx,My]

        pressed=pygame.key.get_pressed()




        if pressed[pygame.K_f]:
            playerInputData["fire"]=1

            test1.fire()
        else:
            playerInputData["fire"]=0




        send_inputs(playerInputData)

        if user2.playerOutputData["fire"]==1:
            test2.fire()
        test2.server_goto(user2.playerOutputData["MovingTo"])
        test2.MouseLookAngle(user2.playerOutputData["Mpos"])
#this "if" monstrosity checks when buttons are pressed
        """"
        if pressed[pygame.K_a]:
            test1.turn(-turnvalue)
        if pressed[pygame.K_d]:
            test1.turn(turnvalue)
        if pressed[pygame.K_w]:
            test1.move(movevalue)
        if pressed[pygame.K_s]:
            test1.move(-movevalue)
        if pressed[pygame.K_f]:
            test1.fire()
            
        
        if pressed[pygame.K_RIGHT]:
            test2.turn(turnvalue) 
        if pressed[pygame.K_LEFT]:
            test2.turn(-turnvalue)
        if pressed[pygame.K_UP]:
            test2.move(movevalue)
        if pressed[pygame.K_DOWN]:
            test2.move(-movevalue)
        if pressed[pygame.K_l]:
            test2.fire()
        """

    pygame.quit()



if __name__ =="__main__":
    main()
