this is a simple multiplayer pvp game made in python

this project is work in progress so everything does not work yet


in the levels folder there is level_editor.py
you can use this to make simple levels by click and dragging your mouse



server.py has to be running before you try to connect clients to it


main.py is the client. 



if server is hosted from the same computer as one of the players the player must type "localhost" (remove the ")when prompted ip address
other player must type what ever local ipv4 address the host computer is running on. this can be found with ipconfig/ifconfig






NEEDED PIP PACKAGES

just run "pip3 install *package_name*"

json
sockets
pygame
threading







KNOWN ISSUES

player2 starts running to player1's starting location as soon as the game starts
this happens player2 whinks they are player1. which it tecnically is

"minor" desync issues

