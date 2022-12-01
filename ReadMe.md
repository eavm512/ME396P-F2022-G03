The purpose of this Repository is to store the Files for group G03 of ME 396P Fall 2022

Group Members: 
Kaya	Bayazitoglu
Matthew	Cassoli
John	Maweu
Enrique	Velasquez Morquecho

Link to slides of Nov 29, 2022 class presentation:
https://docs.google.com/presentation/d/1ecF_Bn3KfwUfmLmnrA_vp8SFRSO8M4qUiGO0ULjh6y4/edit#slide=id.p4

# HOW TO USE THIS REPO
- The primary subdirectories in this repo have more readme files that explain the contents of each folder, and in some caeses give instructions on how to use them.
- Below are our project team philosophy and a description of contents of this directory

# PROJECT PHILOSOPHY
Our project objective was to create a solution that could
- Sense a bike in a bay of a bike rack (or bays / or racks)
- Transmit that information to some user viewable location

We accomplished this via:
- Hardware, in the form of a NodeMCU ESP32 connected to an ultrasonic distance sensor in a 3D printed case
- The hardware transmitting its readings via bluetooth to a computer running python
- A python function to sanitize the incoming data and push it to a custom class called "Rack"
  -The Rack class accomodates multiple bike bays that could be present on a bike rack
- Having the Rack class automatically generate a log of the rack's status (based on sanitizer's input)
  - The logs are reasonably readable, and uniform for historical reading
- A flask application running on localhost that queried the logs made by Rack to display data to the user in near realtime
  
# Deliverables
- We delivered a hardware package to detect one bike in one slot on one rack and send data to python
  - this repository contains the code, enclosure, bill of materials, and circuit diagram for that hardware.
- We delivered python files to interpret the data from the hardware and present it via Flask.
- The design of the project is scalable:
  - The Rack class supports multiple bike bays on one rack
  - The Flask app supports multi-bay racks
  - The python data sanitizing function supports sending data regarding multiple bays on one rack to a given Rack
  - Because a Rack is an object, the sanitizing function could easily update data of two Racks in each loop instead of just one
  - The hardware is reasonably scalable, to a limit. We believe a maximum of 4 sensors could be coupled with the ESP32 board used
    - However the code could work in paralell with multiple MCU's
    - Or the code could be modified to work with a board with more GPIO's (and Arduino mega has 50+) and just use the ESP32 board for bluetooth communication
  
# Presentation of results:
- The project can be test driven in either "bluetooth" or "emulator mode.
  - in "emulator" mode, non external hardware is needed. The Sanitizer function uses a predefined set of data to simulate bikes entering and leaving a slot
  - in "bluetooth" mode, the actual hardware described to sense bikes is needed. Data actually comes from the ESP32 and ultrasonic sensor over bluetooth.
    - A computer will need bluetooth connectivity, be in range of the ESP32, be able to pair with it, and know the COM port used to get data
  - It is expected that observers of the repo will first work in "emulator" mode, so the relevant code defaults to being in "emulator" mode. Instructions to get to bluetooth mode are provided.
  
  
# CONTENTS OF THIS DIRECTORY
## Bike Arduino
- contains all code (python and arduino) to run the project in either "emulation mode" or with actual hardware.
- contains templates and resources for the final project
- Is the main directory users of this project will work in

## Hardware Info and CAD
- contains STL files for the 3D printed enclosure
- Fusion 360 files of the 3D printed models and the electronics
- A bill of materials, including where to potentially acquire components

## Standards
- contains files we shared among ourselves to help work together detailingn what modules would hand off what data formats to each other.

## Video and demo of hardware working
- Contains historical files and files of the final hardware product working so graders and observers can appreciate the hardware aspect of the project even if they only run in emulation mode

## Lightning Talk and Demo-test files
- Contains historical information from our lightning talk, and steps along the way in the project like proof of concepts, which helped develop the project, but whose code is not direclty used in the finanl product.

## Project Proposal.txt
- a historical log of the project proposal presented in October

## Final Project Rubric with notes.docx
- internal tracking document to compare our progress vs the rubric, as well as collect ideas for improvements

___________________________________
Group Assignments:
All group members contributed to each part of the project, but leaders of specific areas were:
Matthew: Arduino code / ESP32 programming, receiving bluetooth messages in python, hardware assembly
John: sanitization of incoming bluetooth data, data architecture
Kaya: implementation of Rack class (including logging, prep for flask)
Enrique: creation of flask interface
