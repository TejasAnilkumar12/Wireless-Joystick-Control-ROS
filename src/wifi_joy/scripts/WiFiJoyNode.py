#!/usr/bin/env python3

"""
File name:  WiFiJoyNode.py
Description:  Main file for Wi-Fi Joy Node ROS Publisher
OS: Windows or Linux
Author:  Tejas Anilkumar P.  <tpandara@andrew.cmu.edu>
Date:  08/24/2020
   
Carnegie Mellon University
"""

import rospy
from wifi_joy.msg import Joy
from joystick_helper import *
from TCP_helper import *

def sendData():
    initParser()
    server = getServerFlag()
    if server:
        initJoystick(0)
    initTCP()
    
    rospy.init_node('wifi_joy_node',anonymous=False)
    #rospy.Publisher(topic_name,topic_type,queue_size )
    publisher = rospy.Publisher('wifi_joy',Joy,queue_size = 10)
     
    #Rate of sending message
    #in Hz so time = 1/Hz
    #1 sec = 1 hz
    #2 sec = 0.5 hz and so on
    rate = rospy.Rate(10)
     
    #initialise a while loop till we receive 
    # interrupt exception 

    
    while not rospy.is_shutdown():
	#returns encoded data
        if server:
            joy_data = updateJoystickData()
            #convert to bytes
            barr = bytearray(joy_data)
            #send data via TCP
            sendData(barr)
        else:
            #Receive Data via TCP
            joy_data = recvData()
            axes,buttons = decodeJoystickData(joy_data)
            
        data = Joy()
        data.axes = axes
        data.buttons = buttons

        
        
        #print in terminal
        rospy.loginfo(data)
        #publish the data
        publisher.publish(data)
        #sleep for specified time i.e. rate
        rate.sleep()


if __name__ == "__main__":
    try:
        sendData()
    except rospy.ROSInterruptException:
        pass
    
