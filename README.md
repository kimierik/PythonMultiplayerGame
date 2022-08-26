## intro

this is a simple multiplayer 1v1 pvp game made in python
  
this project is work in progress so everything does not work yet
  
other features
  
level editor  


  


  


  

  



# playing the game
  

## making a map

<p>
<img src="images/leveldemo1.png" width ="500" alt="">
</p>
  
this is the level editor
it is in leves/level_editor.py
  
by pressing the buttons on the ui you can choose to move the player starting points or add and remove walls  
when you are ready press the "s" key to save your map to gamelevel.json
move this json file to the same folder as server.py  
  
  


## getting the game working
first you must start server.py, then connect the clients, when you start client.py you will get an empty window  
and the terminal will prompt you to enter an ip address. if the server is hosted on the same network as the clients  
you need to type the local ipv4 address of the server, which can be gotten from ipconfig/ifconfig  
if you are hosting the server on the same computer as one of the clients you need to enter "localhost"
when both players are connected you can styart playing  
mouse click to move and "f" to fire
  

  









  
## NEEDED PIP PACKAGES

just run "pip3 install *package_name*"

json  
sockets  
pygame  
threading  

  





## KNOWN ISSUES
    
  
"minor" desync issues

