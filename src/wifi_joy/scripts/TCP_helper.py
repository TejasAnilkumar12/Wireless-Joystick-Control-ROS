"""
File name:  TCP_helper.py
Description:  Helper source code for TCP Socket 
OS:  Windows or Linux
Author:  Tejas Anilkumar P.  <tpandara@andrew.cmu.edu>
Date:  08/10/2020
   
Carnegie Mellon University
"""

import os
import socket
import argparse
import sys
import platform
from time import *

def initParser():
    global args,fd_flag,no_file
    fd_flag = False
    parser = argparse.ArgumentParser()
    parser.add_argument("-m","--mode",required=True,help="MODE: Server or Client")
    parser.add_argument("-ip","--server_ip",required=True,help="SERVER_IP: e.g. 192.168.1.10")
    parser.add_argument("-p","--port",default = 5050,help="PORT: e.g. 5050")
    args = parser.parse_args()
    

def variablesInit():
    global SERVER_HOST,SERVER_PORT,BUFFER_SIZE,SEPARATOR
    SERVER_HOST = args.server_ip
    SERVER_PORT = int(args.port)
    BUFFER_SIZE = 150
    SEPARATOR = "-"
    
def getServerFlag():
    flag = False
    if args.mode == "Server":
        flag = True
    return flag


def initTCP():
    
    variablesInit()
    global sock,client
    try:
        print("Creating Socket\n")
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    except socket.error as err:
        print("Creating Socket Failed\n")
        print(err)
        sock.close()
            
    print("Socket Created\n")
    
    if args.mode == "Server" or args.mode == "s":
              
        print("Binding IP Address and Port\n")
        sock.bind((SERVER_HOST,SERVER_PORT))

        print("Server running at %s:%s\n"%(SERVER_HOST,SERVER_PORT))

        print("Waiting for Client")

        sock.listen()
        client,address = sock.accept()
        print("Client Connected %s:%s"%address)

        
    elif args.mode == "Client" or args.mode == "c":
        print("Connecting to Server %s:%s\n"%(SERVER_HOST,SERVER_PORT))
        
        result = sock.connect_ex((SERVER_HOST,SERVER_PORT))
        #print(result)
        if(result==0):
            print("Connected\n")
            
        else:
            print("Connecting Failed")
            sock.close()
            sys.exit('\nShutting Down')
        
        
    
def clearScreen():
    system = platform.system()
    if system == "Windows":
        os.system('cls')
    elif system == "Linux":
        os.system('clear')
        
    
def sendData(data):
    if(args.mode == "Server"):
        Socket = client
    else:
        Socket = sock
    Socket.send(data)
    
def recvData():
    if(args.mode == "Server"):
        Socket = client
    else:
        Socket = sock
    data = Socket.recv(BUFFER_SIZE)
    return data
    
            
def shutdownTCP():
    sock.close()
    if(args.mode == "Server"):
        client.close()
    sys.exit('\nShutting Down')

