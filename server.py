import socket
#from _thread import *
import threading
import json


p=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
p.connect(("8.8.8.8",80))
localip=p.getsockname()[0]
p.close()


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname( localip)
port=9999
mapdict={}
prot="utf_8"

clients=[]#list of both the clients



try:
    s.bind((ip,port))
    print("server is listening")
    print("hosting on ",ip)
except socket.error as e :
    print("error binding to port")
    print(e)


s.listen()


#we need to listen to 2 sources and be able to send data to 1 source at a time
#we can do the send function normally without threading and call it whenever
#this function just listenes to what the player sends i quess

def send_data(data,owner):
    if owner ==1:
        #clients[0].send(json.dumps(data).encode(prot))
        clients[0].send(data.encode(prot))
    else:
        #index out of range bc no other connection made yet
        #clients[1].send(json.dumps(data).encode(prot))
        clients[1].send(data.encode(prot))



def thread_connection(conn):#handler function hancles all connections seperately
    client=conn 
    print("conneciton has been made to :", client)
    print(" ")
    while True:
        try:
            data=client.recv(1024).decode(prot)
            send_data(data,clients.index(client))     #calls function to send data to the other player
        except:

            print("ending")
            clients.remove(client)
            #print("something has hapened and the server has terminated connection to: " conn)
            client.close
 

def mapload():
    with open("gamelevel.json","r") as filed:
        data=filed.read()
        obj= json.loads(data)
        mapdict=obj
        return mapdict




def main():
    run =True
    while run:
        client,addr=s.accept()
        client.send(json.dumps(mapload()).encode(prot))
        print("mapdata sent")
        clients.append(client)
        client.send(str(clients.index(client)).encode(prot))
        print(len(clients))
        if len(clients)==2:
            for person in clients:
                person.send("asd".encode(prot))
                #sets off players 
                thread=threading.Thread(target=thread_connection,args=(person,))
                thread.start()
    #pipe the client connection to the threaded connectiuon and make some function to send data between the two cunts



if __name__=="__main__":
    main()
