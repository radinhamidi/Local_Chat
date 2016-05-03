# -*- coding: utf-8 -*-
"""
..::/RADIN\::..

"""
import time 
from socket import *
#serverName = 'servername'
serverName = input("Enter Host's IP : ")
#serverName = '127.0.0.1'
serverPort = 12500
cs = socket(AF_INET, SOCK_STREAM)
cs.connect((serverName,serverPort))
print('you are now connected to the server')
time.sleep(0.2)
name = input('Create Username : ')
mode = input('________________________________________________________________________\n|Choose you mode : |1-Type in your own message|2-View other user messages|\n|__________________|__________________________|__________________________|\n')
ex_mode=mode
name=''.join(['$',name])
mode=''.join(['~',mode])
cs.send(bytes(name, 'UTF-8'))
resp = cs.recv(1024)
print ('\nServer:', resp.decode(encoding='UTF-8',errors='strict'))
print ('\nYou are now in mode %s\n'%ex_mode)
time.sleep(0.3)
cs.send(bytes(mode, 'UTF-8'))
while 1:
    if mode=="~1":
        msg = input('Enter your message :')
        if msg=='':
            msg='-'
        if msg=="#view":
            mode="~2"
            cs.send(bytes(mode, 'UTF-8'))    
            print ('You are in mode 2')
        elif msg=="#quite":
            print("Bye !")
            time.sleep(1.2)
            cs.close()
            exit()
        else:
            cs.send(bytes(msg, 'UTF-8'))  
            
    #######################################
            
    if mode=="~2":
        msg = input('Enter your quest (or just press enter for view unseen messages) :')
        if msg=='':
            msg='-'
        if msg=="e":
            mode="~1"
            cs.send(bytes(mode, 'UTF-8'))    
            print ('You are in mode 1')
        elif msg=="q":
            print("Bye !")
            time.sleep(1.2)
            cs.close()
            exit()
        else:
            msg="&fetch"
            cs.send(bytes(msg, 'UTF-8'))
            resp = cs.recv(1024)
            resp=int(resp.decode(encoding='UTF-8',errors='strict'))
            if resp == 0:
                print('No new message')
            for c in range(0,resp):
                umsg=cs.recv(1024)
                print(umsg.decode(encoding='UTF-8',errors='strict'))
                time.sleep(0.05)
				