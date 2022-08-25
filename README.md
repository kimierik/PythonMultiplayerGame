##intro

this is a simple multiplayer pvp game made in python
  
this project is work in progress so everything does not work yet
  

in the levels folder there is level_editor.py
you can use this to make simple levels by click and dragging your mouse

  

server.py has to be running before you try to connect clients to it

  
main.py is the client. 


  
if server is hosted from the same computer as one of the players the player must type "localhost" (remove the ")when prompted ip address
other player must type what ever local ipv4 address the host computer is running on. this can be found with ipconfig/ifconfig

  



  
##NEEDED PIP PACKAGES

just run "pip3 install *package_name*"

json  
sockets  
pygame  
threading  

  





##KNOWN ISSUES
    
your model runs off on the other client.
this can be "fixed" by trying to sync the models, by looking at the other players screen and trying to move approprietly
  
  
  
"minor" desync issues

