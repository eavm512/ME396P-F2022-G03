This directory contains group information on how we went about the project and handed off data to each other

# rack-class
- information on the contents of the Rack class, including an example log and example valid racks
- makes the note that True is "full" (there's a bike in the bay) and False is an open available bay

The Rack class initially logged a timestamp along with every change to the rack (not the entire rack) every update. The class was revised to generate a log such as [rack-log early nov 30.txt](/Standards/rack-class/rack-log_early_nov_30.txt), where each entry contains a timestamp with the entire rack's status.

The current iteration generates a single-line log such as [rack-log.txt](/Standards/rack-class/rack-log.txt) to simplify reading the log through code, and to add a rack name to support multiple racks. Rack.py will only generate a new log if there is a change to the status of the rack to prevent the log file from exploding in size.

# brainstorm data structure
- meeting images from our first large brainstorm on how to structure the project

# comm_simulation
- initial sketch on how to sort data from bluetooth from sensor
- the exact logistics would go on to change as the sanitize function was finally built

# sonar_demo_data
- an intial set of data that the ESP32 bluetooth board would feed to python (and sanitize)
- the data would later change, and example data is now stored in the emulator within ESP_BT_Handler.py

# mod_example_sonar_arduino_uno_version
- early arduino file that toggled and LED based on sonar readings
- proved we could sense bike

# John Nov 28 eg data.txt
- An old data format that was previously sent to sanitize.py This was superseded by a numbers only format (the words AVAILABLE and NOT AVAILABLE no long appear)
