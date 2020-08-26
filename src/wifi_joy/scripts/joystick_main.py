"""
File name:  joystick_main.py
Description:  Main file for Wi-Fi Joystick Control. Run this File with Joystick connected
OS:  Windows or Linux
Author:  Tejas Anilkumar P.  <tpandara@andrew.cmu.edu>
Date:  08/24/2020
   
Carnegie Mellon University
"""

from joystick_helper import *
from time import sleep
from TCP_helper import *

initParser()
server = getServerFlag()
if server:
    initJoystick(0)
initTCP()


while True:
    
    try:
        #returns encoded data
        if server:
            data = updateJoystickData()
            #convert to bytes
            barr = bytearray(data)
            #send data via TCP
            sendData(barr)
        else:
            data = recvData()
            decodeJoystickData(data)
        sleep(0.1)
    except KeyboardInterrupt:
        stopJoystick()
        shutdownTCP()
        sys.exit()



