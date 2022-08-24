#congiguration file that holds global variables 
#i know this is not the most optimal way of doing this give me a break


import pygame

pygame.init()

width,heigth = 900,600



#
#misc setup
WIN=pygame.display.set_mode((width,heigth))
fpslimit=60
pygame.display.set_caption("tank game")



#colors
white= (255,255,255)
black = (0,0,0)
red=(255,0,0)

fire_rate=0.1#seaconds of delay between firing
dist=50#distance variable between the box that shows where you are aiming at. aslo used for moving the character please do not change 
#i have no clue what ^^ does but please dont change it it starts breaking things


#turnvalue=math.radians(0.1)#turn speed
movevalue=2#movement speed
bulletspeed=3#movement speed of bullets
playerlist=[]#list of all players
bullets=[]#list of all bullets
bullet_life=2#time a bullet is alive in seaconds
walls=[]#another global object, 









