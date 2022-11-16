# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 18:37:49 2022

@author: casso

worekd Nov 15 with COM18
"""

import serial.tools.list_ports


if __name__ == __main__:
    ports = serial.tools.list_ports.comports()
    serialInst = serial.Serial()
    
    portsList = []
    
    for onePort in ports:
        portsList.append(str(onePort))
        print(str(onePort))
    
    val = input("Select Port: COM")
    
    for x in range(0,len(portsList)):
        if portsList[x].startswith("COM" + str(val)):
            portVar = "COM" + str(val)
            print(portVar)
    
    serialInst.baudrate = 115200
    serialInst.port = portVar
    serialInst.open()
    
    messages = []
    print('Listening')
    
    while len(messages) < 10:
    	if serialInst.in_waiting:
    		packet = serialInst.readline()
    		messages.append((packet.decode('utf').rstrip('\n')))
            
    print(messages)
    
    serialInst.close()