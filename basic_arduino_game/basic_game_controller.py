# -*- coding: utf-8 -*-
"""
Python 3.7
Created on Sat Oct  8 10:24:00 2022

@author: casso
"""

import serial
import turtle
import time

# ser = serial.Serial('COM3', 9600)

# ser
# Out[5]: Serial<id=0x254b51f4c70, open=True>(port='COM3', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)

# ser.readline()
# Out[6]: b'17697\r\n'

#go get some test input lines
# ser = serial.Serial('COM3', 9600)
# lines = []
# while len(lines) < 10:
#     lines.append(ser.readline())
    
# #parse the lines
# messages = []
# for line in lines:
#     message = ''
#     decoded = bytes.decode(line)
    
#     for char in decoded:
#         if char != '\n' and char != '\r':
#             message = message + char
    
#     messages.append(message)
    
# #see how we did
# print(messages)
#   ['108', 'FIRE!', '153', '133', '147', '233', 'FIRE!', '273', '290', 'FIRE!']
# ser.close()

def test_serial(ser):
    lines = []
    while len(lines) < 10:
        lines.append(ser.readline())
        
    #parse the lines
    messages = []
    for line in lines:
        message = ''
        decoded = bytes.decode(line)
        
        for char in decoded:
            if char != '\n' and char != '\r':
                message = message + char
        
        messages.append(message)
    
    return messages

def parse_msg(msg_str):
    msg_str = bytes.decode(msg_str)
    msg = ''
    for char in msg_str:
        if char != '\n' and char != '\r':
            msg += char
    return msg

def shoot(current_angle):
    '''shoot a projectile
    '''
    missile = turtle.Turtle()
    missile.settiltangle(current_angle)
    missile.penup()
    
    return missile

def draw(msg, missiles, last_heading):
    '''
    rotate the player
    advance any missiles
    remove any missiles that have gone too far
    '''
    print(msg)    
    
    if msg != 'FIRE!':
        last_heading = int(msg)
        player.settiltangle(last_heading)
    else: #we're firing a missile!
        new_missile = shoot(last_heading)
        missiles.append(new_missile)
        print('pew!')
    
    #advance existing missiles
    for miss in missiles:
        miss.forward(MISSILE_SPEED)
    
    #remove missiles that are far away:
    #someone help me with a better way to do this!
    to_remove = []
    for idx in range(0, len(missiles)):
        if missiles[idx].distance(0,0) > MISSILE_DELETE:
            to_remove.append(idx)
            
    to_remove.reverse()
    for remove_idx in to_remove:
        del missiles[remove_idx]
    
    
    return missiles, last_heading

#--------------------------------------------------
MISSILE_DELETE = 220
MISSILE_SPEED  = 10

ser =serial.Serial('COM3', 9600)

player = turtle.Turtle()
player.shape('turtle')
player.color('green')
missiles = [] #a list of turtle missiles
window = turtle.Screen()
last_heading = 0

while(True):
    missiles, last_heading = draw(parse_msg(ser.readline()), missiles, last_heading)
    time.sleep(.05)
    
    if len(missiles) > 5:
        print("so many missiles! goodbye")
        break


turtle.bye()
ser.close()
