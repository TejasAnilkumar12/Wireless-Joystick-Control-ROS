#!/usr/bin/env python3

"""
File name: WiFiJoyNodeReceive.py
Description:  Main file for Wi-Fi Joy Node ROS Subscriber 
OS: Windows or Linux
Author:  Tejas Anilkumar P.  <tpandara@andrew.cmu.edu>
Date:  08/24/2020
   
Carnegie Mellon University
"""

import rospy
from wifi_joy.msg import Joy

def joy_callback(data):
    rospy.loginfo("Left: %s",data.axes[1])
    rospy.loginfo("Right: %s",data.axes[4])


def receive():
    rospy.init_node('joy_receive',anonymous=True)
    #rospy.Subscriber(topic_name,topic_type,handler)
    subscriber = rospy.Subscriber('wifi_joy',Joy,joy_callback)
     
    #initialise a spin loop of rospy which exits
    rospy.spin() 
  


if __name__ == "__main__":
    try:
        receive()
    except rospy.ROSInterruptException:
        pass