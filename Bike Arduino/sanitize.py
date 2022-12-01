# sanitize: RX bike rack serial data cooked and pushed to Rack objects
#   per ME396P-F2022-G03/Standards/board-data-flow.jpeg
#   per "<'Available '> + <distance> <'\n'>" in Bike Arduino/ESP_BT_Handler.py
#   per DIST_THRESH in Bike Arduino/BT_with_info_string_ESP32/BT_with_info_string_ESP32.ino
#   per "Eg_dict = {0 : True, 1: False, 2 : True, 3 : True, 4 : False}" in Standards/Rack_Dict_convention
#   per Bike Arduino/mod_example_sonar_arduino_uno_version/mod_example_sonar_arduino_uno_version.ino

import ESP_BT_Handler as bt
import Rack as rack
import re
from collections import namedtuple

EMULATE = 3 #-1: use bluetooth, 0: emulate random choice, 1: no bike, 2: bike, 3: no bike, 4: noisy but bike.
PORT = 7
DEBUG_MODE = True

classifier_data = {'DIST_THRESH': 15}
r = rack.Rack()
PORT = 7


def parse_setup():
    distance_pat = '(0|[1-9][0-9]*)'
    return re.compile(r'' + distance_pat + '\r\n')

line_re = parse_setup()
LineData = namedtuple('LineData', ['distance'])

def parse_raw_lines(raw_lines):
    rx_matching_lines = []
    for raw_line in raw_lines:
        match = line_re.match(raw_line)
        if match:
            distance = int(match[0])
            rx_matching_lines.append(LineData(distance=distance))
    return rx_matching_lines

def grammar_is_good(line_data):
    return len(line_data)  # using truthiness
   
def classify(line_data):
    bike_present = False
    bikes_found = 0
    no_bikes = 0
    
    for reading in line_data:
        if reading.distance < classifier_data['DIST_THRESH']:
            bikes_found += 1
        else:
            no_bikes += 1
    
    if bikes_found > len(line_data)*.25:
        bike_present = True

    # return {0 : line_data[0].distance < classifier_data['DIST_THRESH']}
    return {0 : bike_present}

def push_to_rack(the_dict):
    r.update_rack(the_dict)

def port_listener(PORT):
    raw_lines = bt.get_messages(port = PORT, fake = EMULATE)  ##### udpate port if necessary (unlikely)
    line_data = parse_raw_lines(raw_lines)
    # print('line data is: ', line_data)
    if grammar_is_good(line_data):
        the_dict = classify(line_data)
        push_to_rack(the_dict)

def sanitize(): 
    port_listener(PORT)

def supervise():
    count = 0
    if DEBUG_MODE:
        while count < 100:
            count += 1
            sanitize()
    else:
        while True:
            sanitize()
  
if __name__ == '__main__':
    # print('running main!')
    supervise()
 
