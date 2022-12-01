#This directory contains the main files to run the project, and their critical support files.

##How to run with the emulation

##How to initialize run the Flask application

##Contents
> BT_wtih_info_string_ESP32
	>>is not strictly necessary to run the files, but contains the final code the ESP32 runs to communicate over bluetooth and sense bikes
>ESP_BT_handler.py 
	>>is called by sanitize to receive data from the ESP32 and pass it along.
	>>In emulation mode, fake data is stored in this file, which is sent to sanitize. 
	>>In bluetooth mode, real data received over bluetooth from the ESP32 is sent to sanitize


>Sanitize.py
	>>To change between emlation and bluetooth modes, change the value of EMULATE global variable in sanitize.py
		>>>-1 results in bluetooth mode. 
		>>>0 results in the main emulation mode (send premade fake data, but randomly select which data)
		>>> 1-4 sets up emulation mode, but allows the user to select which fake data will be sent. This results in a fairly static Flask and Rack log.
			>>>>1) no bikes present
			>>>>2) bike present
			>>>>3) no bike present
			>>>>4) bike present, but data is intentionally noisy
			
