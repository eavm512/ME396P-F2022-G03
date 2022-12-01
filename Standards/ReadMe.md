This directory contains group information on how we want to go about the project

# rack-class
- information on the contents of the Rack class, including an example log and example valid racks
- makes the note that True is "full" (there's a bike in the bay) and False is an open available bay

The Rack class initially logged a timestamp along with every change to the rack (not the entire rack) when an update was passed. This was revised such that a log like the one in [placeholder](/Standards/rack-class/)

# brainstorm data structure
- meeting images from our first large brainstorm on how to structure the project

# comm_simulation
- initial sketch on how to sort data from bluetooth from sensor
- the exact logistics would go on to change as the sanitize function was finally built

# sonar_demo_data
- an intial set of data that the ESP32 bluetooth board would feed to python (and sanitize)
- the data would later change, and example data is now stored in the emulator within ESP_BT_Handler.py

#mod_example_sonar_arduino_uno_version
- early arduino file that toggled and LED based on sonar readings
- proved we could sense bike
