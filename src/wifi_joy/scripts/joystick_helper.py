"""
File name:  joystick_helper.py
Description:  Helper source code for Joystick
OS:  Windows or Linux
Author:  Tejas Anilkumar P.  <tpandara@andrew.cmu.edu>
Date:  08/24/2020
   
Carnegie Mellon University
"""


import pygame
from joystick_pb2 import *

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

#Create an instance of Joystick proto schema
joystick = Joystick()

#Pygame Textprint Function by pygame
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def print(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10


def initJoystick(number):
    global js
    pygame.init()
    textPrint = TextPrint()
    #[width,height]
    size = [100, 50]
    screen = pygame.display.set_mode(size)
    screen.fill(WHITE)
    textPrint.reset()
    pygame.display.set_caption("Wi-Fi Joystick")
    textPrint.print(screen, "Wi-Fi Joystick")
    textPrint.print(screen, "Do Not Close")
    pygame.display.flip()
    js = pygame.joystick.Joystick(number)
    js.init()

def stopJoystick():
    pygame.quit()
        

def updateJoystickData():
    pygame.event.get()
    #update joystick axes values
    
    joystick.axes.axis0 = round(-js.get_axis(0),2)
    joystick.axes.axis1 = round(-js.get_axis(1),2)
    joystick.axes.axis2 = round(-js.get_axis(2),2)
    joystick.axes.axis3 = round(-js.get_axis(3),2)
    joystick.axes.axis4 = round(-js.get_axis(4),2)

    #update joystick button values
    joystick.buttons.button0 = js.get_button(0)
    joystick.buttons.button1 = js.get_button(1)
    joystick.buttons.button2 = js.get_button(2)
    joystick.buttons.button3 = js.get_button(3)
    joystick.buttons.button4 = js.get_button(4)
    joystick.buttons.button5 = js.get_button(5)
    joystick.buttons.button6 = js.get_button(6)
    joystick.buttons.button7 = js.get_button(7)
    joystick.buttons.button8 = js.get_button(8)
    joystick.buttons.button9 = js.get_button(9)
    
    encoded_data = joystick.SerializeToString()
    
    return encoded_data


        
def decodeJoystickData(data):
    joy = Joystick()
    joy.ParseFromString(data)
    axes = [joy.axes.axis0,joy.axes.axis1,joy.axes.axis2,joy.axes.axis3,joy.axes.axis4]
    buttons = [joy.buttons.button0,joy.buttons.button1,joy.buttons.button2,joy.buttons.button3,joy.buttons.button4,joy.buttons.button5,joy.buttons.button6,joy.buttons.button7,joy.buttons.button8,joy.buttons.button9]
    return axes,buttons

    
