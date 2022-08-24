import math
import pygame
import time
from . import config


#WIN=pygame.display.set_mode((900,600))

#white=(255,255,255)
#black=(0,0,0)
#red=(255,0,0)



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







class wall:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y#most of these could have been inherited
        self.width=w
        self.height=h

    def render(self):
        rect=pygame.Rect(self.x,self.y,self.width,self.height)
        pygame.draw.rect(config.WIN,config.black,rect)

    def collide_with_wall(self,x,y,h,w):#return true if object at x,y with width and heigth of w,h has collided w/self
        if x - self.x <= self.width and (x+w) >= self.x:
            if y - self.y <= self.height and (y+h) >= self.y:
                return True
        return False






class bullet:#ammo
    def __init__(self,x,y,angle,host):
        self.x=int(x)
        self.y=int(y)
        self.host=host
        self.angle=angle
        self.lifespan =time.time()#alot of repeated code lines could be made easier
        self.width=15
        self.height=15

    def fly(self):#this moves the bullet
        x=math.cos(self.angle)*config.dist
        y=math.sin(self.angle)*config.dist
        self.x=self.x+((x/50)*config.bulletspeed)
        self.y=self.y+((y/50)*config.bulletspeed)
        #50 is a random number that i used to slow down the projectile this is an useless calculation but it worksa so....

    def render(self):#renders bullet
        rect=pygame.Rect(self.x-self.width/2,self.y-self.width/2,self.width,self.height)
        pygame.draw.rect(config.WIN,config.red,rect)
        #print("asd")

    def terminate(self):#commints seppoku when time is up
        timelived=time.time()-self.lifespan
        if timelived >= config.bullet_life:
            del config.bullets[config.bullets.index(self)]
        else:
            for wall in config.walls:
                if wall.collide_with_wall(self.x-self.width/2,self.y-self.height/2,self.width,self.height):#check collision from all walls
                    try:#literally an error i did not know how to fix but this works just as i wanted it to work
                        del config.bullets[config.bullets.index(self)]#delete self
                    except:#but lmao no were not actually deleting anything were just not processing them
                        pass#this is computer memory memory hell

    def playercollision(self):
        #loop through all the players see if collision see if not host
        for tank in config.playerlist:
            if tank==self.host:
                pass
                #print("false")
                #return False
            else:
                if tank.x-self.x<=self.width and (tank.x+tank.w)>=self.x:
                    if tank.y-self.y<=self.height and (tank.y+tank.h)>=self.y:
                        del config.playerlist[config.playerlist.index(tank)]#what the fuck?
                        del tank
                        #return True
                #print("end false")
                return False
                
           



class tank:#players

    def __init__(self, x,y,angle,):
        self.x=int(x)
        self.y=int(y)
        self.angle=(angle*math.pi/180)
        self.bullet_variable=0
        self.h=35
        self.w=35
        self.collisionlist=[]#there has to be a better way to do this
        self.commandlist=[]
        self.last_fire=time.time()
        self.topos=[self.x,self.y]
        self.difference=1
        self.movedir=0
    def turn(self,val):
        self.angle =self.angle+val


    def MouseLookAngle(self,mpos):
        #mx,my=pygame.mouse.:wqget_pos()#mx anbd my is mouse x and mouase y
        #rewritten to be what is the difference between tank and mouise pos
        mx=mpos[0]-self.x-self.w/2
        my=mpos[1]-self.y-self.h/2
        try:
            self.angle=math.atan(my/mx) #division by zero
        except:
            pass
        if mx<0:#this is a hack to fix angle flipping out when x goes negative
            angdiff=(math.pi/2)+self.angle
            self.angle=angdiff+(math.pi/2)


    def MouseLookAngle_server(self,x,y):#copy of mouse look angle, user for server test
        #mx,my=pygame.mouse.get_pos()#mx anbd my is mouse x and mouase y
        #rewritten to be what is the difference between tank and mouise pos
        mx=mx-self.x-self.w/2
        my=my-self.y-self.h/2
        try:
            self.angle=math.atan(my/mx) #division by zero
        except:
            pass
        if mx<0:#this is a hack to fix angle flipping out when x goes negative
            angdiff=(math.pi/2)+self.angle
            self.angle=angdiff+(math.pi/2)



    def gox(self):
        #self.x=self.x+(x*val)
        if self.topos[0] <= int(self.x)+1 and self.topos[0]>=int(self.x)-1:
            pass
        else:
            x=math.cos(self.movedir)*config.dist
            self.x=self.x+((x/50)*config.movevalue)

    def goy(self):
        #self.y=self.y+(y*val)
        if self.topos[1] <= int(self.y)+1 and self.topos[1]>=int(self.y)-1:
            pass
        else:
            y=math.sin(self.movedir)*config.dist    
            self.y=self.y+((y/50)*config.movevalue)




    def server_goto(self,gotopos):#goto function for player 2
    #function needs to exist bc original goto is only called on mouse click and server goto is called every cycle
        if self.topos ==[gotopos[0]-self.w/2,gotopos[1]-self.h/2]:
            pass
        else:

            self.topos=[gotopos[0]-self.w/2,gotopos[1]-self.h/2]#self w and h is halved  so that tank goes to the centre of mouse click

            self.movedir=self.angle

    def goto(self,gotopos):#MOUSE MOVE FUNCTION 
        #gotopos is [x,y]
        self.topos=[gotopos[0]-self.w/2,gotopos[1]-self.h/2]#self w and h is halved  so that tank goes to the centre of mouse click
        #self.movedir=math.atan((self.topos[1]-self.y)/(self.topos[0]-self.x))

        #i think this fucks everything up when called repeatedly
        #we are updating self.angle constantly so the direction we move in will change
        self.movedir=self.angle
    







    def move(self):#moves the tank and sees if there are walls in the way
        self.collisionlist=[]
        self.commandlist=["gox","goy"]
        x=math.cos(self.movedir)*config.dist
        y=math.sin(self.movedir)*config.dist
        #*val
        xdir=x >= 0 #true =we are going rigth false means left
        ydir= y >=0 #true we are going down false means up


        for wall in config.walls:#if you were to ask me how this works i would not know how to answer
            if wall.collide_with_wall(self.x, self.y, self.w, self.h):#this code is shit
                self.collisionlist.append(wall)#add collided wall to list of walls we collide with
            #i do not know why writing this was so hard at first. this is over engineered
            #
            #this is to see what side is nearest to 0.
            #we probably do not need to loop through all walls twice and calculate collisions twice

        if len(self.collisionlist)>=1:
            for wall in self.collisionlist:#go through all collided walls
                tankbottom=abs(wall.y-(self.y+self.h))
                tanktop=abs(self.y-(wall.y+wall.height))
                tankrigth=abs(wall.x-(self.x+self.w))#tank rigth side dist to wal
                tankleft=abs(self.x-(wall.x+wall.width))#tank left to wall
                wlist=[tankbottom, tanktop, tankrigth, tankleft]
                #bottmo=0   top=1   right=2     left=3
                side=wlist.index(min(wlist))
                #finds out witch of the 4 tank sides is nearest to 0

         
                if ydir:
                #we need to pass all movement after we determine where the tank can move
                    if side==0:
                        self.commandlist.remove("goy")
                    else:
                        pass
                if not ydir:
                    if side==1:
                        try:#try loop
                            self.commandlist.remove("goy")
                        except:
                            pass
                    else:
                        pass
                if xdir:
                    if side==2:
                        self.commandlist.remove("gox")
                    else:
                        pass
                if not xdir:
                    if side ==3:
                        try:#another try loop. this prevents double delete of gox and goy if you collide to 2 walls on the same axis
                            #this try loop could be an if statement but i think this is good
                            self.commandlist.remove("gox")
                        except:
                            pass
                    else:
                        pass


        if len(self.commandlist)>=1:
            for command in self.commandlist:
                comd=getattr(self,str(command))
                if command=="goy":
                    comd()
                if command=="gox":
                    comd()
#end of move def




    def fire(self):#creates a bullet entity, this function has 2 functions so its kinda shit.
        #we have a list of active bullets then we just append a number to the list then we make it a bullet object with proper stats it needs. idk if bullet name is useful
        if stopwatch(self.last_fire,config.fire_rate):
            config.bullets.append(self.bullet_variable)
            config.bullets[config.bullets.index(self.bullet_variable)] =bullet((self.x+self.w/2), (self.y+self.h/2), self.angle,self) #spagetti
            self.bullet_variable =self.bullet_variable+1
            self.last_fire=time.time()



    def render(self):#tank itself
        rect=pygame.Rect(self.x,self.y,self.w,self.h)
        pygame.draw.rect(config.WIN,config.black,rect)


    def view(self):#this is the rectangle we spin around the tank
        x=math.cos(self.angle)*config.dist
        y=math.sin(self.angle)*config.dist
        x=x+self.x+(self.w/2)
        y=y+self.y+(self.h/2)
        rect=pygame.Rect(x-2.5,y-2.5,5,5)
        pygame.draw.rect(config.WIN,config.black,rect)







