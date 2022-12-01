# This directory contains the main files to run the project, and their critical support files.

# How to run the project

## Base requirements to run the project:
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
* If operating in bluetooth mode, your computer must have Bluetooth and the ability to pair with an ESP32 chip
* See how to run in emulation mode and How to run project with live Bluetooth Data for next steps
* If not running in DEBUG_MODE (see sanitize.py below) the program will run indefinitely.
* Move, delete, or rename rack-log.txt so that the Rack class can make a new log for your tests.
	* If you do not move delete or rename rack-log.txt, the Rack class will append data to the end of the current log.
* Go through the steps in either "How to run in emulation mode" or "How to run the project with live Bluetooth Data" below
* Run sanitize.py
	* Rack.py, FlaskBikeRackDisplay.py, ESP_BT_Handler.py, templates (folder) and rack-log.txt need to be in the same directory as sanitize.py. This is the case in the repo as cloned.
	* sanitize.py needs to have permission to create or edit rack-log.txt which it will attempt to make in the same directory sanitize.py is located in.
* Run FlaskBikeRackDisplay.py (see How to initialize and run the Flask application for more info)
* Navigate to the IP address printed by FlaskBikeRackDisplay.py
	* Only Rack 1 will contain data in the Flask UI. Rack 2 button exists to show what a disconnected Rack would be like.
	* See our video in /Video and demo of hardware working/Videos of Final Product/compressed Flask operation and scalibility demo.mp4 for a visualization of multiple racks being shown in Flask to see how the Flask application is scaleable.

## How to run in emulation mode (without bluetooth hardware) (EMULATE = 0, 1, 2, 3, 4 in sanitize.py)
* This is the expected mode most graders and casual viewers will run in.
* The cloned repository should be preset in Emulation mode, but you can modify the exact emulation parameters
* Modify the following parameters in sanitize.py
	* set EMULATE to 0, 1, 2, 3, or 4. See notes under Sanitize.py for details on what each setting does
* NOTE: the emulations run very quickly, and emulate one message from the ESP32. In DEBUG_MODE (DEBUG_MODE = True in sanitize.py) They will generate one line in the log. To generate multiple lines in the log, it is reccomended to repeatedly run the program with emulation mode 0 (which will randomly select between the four emulation data sets). Flask will still work even if the emulation stops running becuase it pulls data from the most recent log, which persists.
	* If in continuous mode, (DEBUG_MODE = False in sanitize.py) the emulation will run indefinitely. If any mode greater than EMULATE = 0 is selected, the log will only generate one line, because the rack status will not change and the Rack class only writes a new line to the log if the status changes. If EMULATE = 0 several lines will be appended to the log, as the emulated messages will be randomly sent and be read as status changes, as long as the program is allowed to run. 

## How to run project with live Bluetooth Data from ESP32 (Emulate = -1 in sanitize.py)
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
* First open FlaskBikeRackDisplay.py
* FlaskBikeRackDisplay.py should be in the directory with the othe .py files as it is in this repo (the "Bike Arduino" directory by default)
* The cloned repository should be structured in the format that there is a templates folder that contains the HTML files for the pages that flask will reference
* Once the Flask is opened and running a URL in the console will appear. Enter that into a browser to access the flask web application

# Directory Contents

### BT_with_info_string_ESP32
* is not strictly necessary to run the files, but contains the final code the ESP32 runs to communicate over bluetooth and sense bikes

### ESP_BT_handler.py 
* Is called by sanitize to receive data from the ESP32 and pass it along.
* In emulation mode, fake data is stored in this file, which is sent to sanitize. 
* In bluetooth mode, real data received over bluetooth from the ESP32 is sent to sanitize

### Sanitize.py
* Is the main python file that loops indefinitely.
* Calls ESP_BT_handler.get_messages() to get information from the ESP (or fake data)
* Parses information from ESP_BT_handler.get_messages()
* Will loop indefinitely unless DEBUG_MODE at the top of the file is False. If False, will only call 100 messages.
	* DEBUG_MODE is useful to debug creating a log file. Flask should still run if the log file has been created, even if it isn't being updated, but data will not update.
* To change between emulation and bluetooth modes, change the value of EMULATE global variable in sanitize.py
	* -1 results in bluetooth mode. 
	* 0 results in the main emulation mode (send premade fake data, but randomly select which data)
	* 1-4 sets up emulation mode, but allows the user to select which fake data will be sent. This results in a fairly static Flask and Rack log.
		* 1) no bikes present
		* 2) bike present
		* 3) no bike present
		* 4) bike present, but data is intentionally noisy
		
### Templates
* Contains templates used by the Flask application to generate and style HTML

### Rack.py
* Defines the Rack class. See Standards folder and readme for more information on Rack class.
* Defines the Rack class.
* Attributes
  * name: The name of the specific bike rack, default = "unnamed"
  * bays: Dictionary containing the status of each bay in the rack
  * updated: The timestamp of the most recent update
* Methods
  * update_rack: Accepts a dictionary containing the status of each bay, storing it in bays. If any change is made, calls log
  * log: appends a file named "rack-log.txt" with a new log entry.

### rack-log.txt
* An EXAMPLE of this log is included in the repo
* delete or rename this before running emulations (otherwise data will just be appended to the log)
* This is the log the Rack class makes when it detects a change in status

### FlaskBikeRackDisplay.py
* Is the main Flask python file that genrates the local hosted web application that displays the rack data.
* Calls formateBayData() to get information and produce a displayable information from the log-rack.txt
* Calls and executes the variouse HTML files located in the Templates folder
