# This directory contains the main files to run the project, and their critical support files.

# Base requirements to run the project:
* Clone this repository and navigate to the Bike Arduino directory
* By default, the files are in Emulation mode (use pre-generated data, no bluetooth data being transmitted)
* Ensure you have at least Python 3.7 and the following libraries:
	* re (regular expression)
	* collections
	* Flask
	* datetime
	* serial
	* time
	* random
* If operating in bluetooth mode, your computer must have Bluetooth and the ability to pair with and ESP32 chip
* See how to run in emulation mode and How to run project with live Bluetooth Data for next steps

# How to run in emulation mode (without bluetooth hardware)
* This is the expected mode graders and casual viewers will run in
* The cloned repository should be preset in Emulation mode, but you can modify the exact emulation parameters
* Modify the following parameters in sanitize.py
	* set EMULATE to 0, 1, 2, 3, or 4. See notes under Sanitize.py for details on what each setting does

# How to run project with live Bluetooth Data from ESP32
* Requirements for Bluetooth Mode:
	* User must first pair with the ESP32. If using arduino sketches from this repo, the device's name will be ESPTEST.
	* After pairing, user must know what COM Port is used for bluetooth reception. To figure out your COM port, either:
		* run main from ESP_BT_Handler in the console. Your available ports will be printed to the console along with their number. Go through each port and guess which is the Bluetooth port until you get signal back.
		* run ESP_BT_Handler.port_info() in the consol, which will just list your ports. 
	* Confirm you've selected the correct port by running ESP_BT_Handler main and entering the correct port. You should receive a data printout if you selected the correct port and are paired with the ESP32.
	* After determining which port is appropriate, set the port number in the PORT variable at the top of sanitize.py
	* Set DEBUG_MODE to False in sanitize.py
	* Set EMULATE to -1 in sanitize.py

## How to initialize and run the Flask application

## Contents

### BT_with_info_string_ESP32
* is not strictly necessary to run the files, but contains the final code the ESP32 runs to communicate over bluetooth and sense bikes
### ESP_BT_handler.py 
* Is called by sanitize to receive data from the ESP32 and pass it along.
* In emulation mode, fake data is stored in this file, which is sent to sanitize. 
* In bluetooth mode, real data received over bluetooth from the ESP32 is sent to sanitize




### Sanitize.py

* To change between emulation and bluetooth modes, change the value of EMULATE global variable in sanitize.py
	* -1 results in bluetooth mode. 
	* 0 results in the main emulation mode (send premade fake data, but randomly select which data)
	* 1-4 sets up emulation mode, but allows the user to select which fake data will be sent. This results in a fairly static Flask and Rack log.
		* 1) no bikes present
		* 2) bike present
		* 3) no bike present
		* 4) bike present, but data is intentionally noisy
			
