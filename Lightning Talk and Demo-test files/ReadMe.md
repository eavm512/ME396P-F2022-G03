This directory contains historical code for reference, proofs of concept, and ligtning talk information

# Arduino egs for lightning
- contains the arduino sketches used in our lightning talk
- the arduinos read button pushes and communicated over serial to our computer, which was interpreted by python which sent a serial command to another arduino to turn on / off an LED

#Button-LED
- a schematic of the setup from our Lightning talk

# Basic arduino game
- was a serial project to read a potentiometer and spin a turtle from turtlegraphics around and fire cannons. 
- was discarded as a bit too unprofessional for the lightning talk
- kept becuase it contains an example of serial communication via USB

# blink
- an example arduino sketches

# USART ISP
- PDF's on serial communication protocols

#Bluetooth Com
- historical sketches for the ESP32 board getting it to communicate over bluetooth
- BT_Demo.py file that receives bluetooth data

#FlaskDemo
- and earlier version of the Flask portion of the project
- relied on being passed Rack object
- was later modified to final version which read logs instead of Rack objects so that Flask (which is constantly running) and the rest of the python project
		(which is constantly running to read bluetooth information)can both run at the same time via multiple kernels so as to not need multi threading.
		
#Templates
- support files for FlaskDemo