# sanitize: RX bike rack serial data cooked and pushed to Rack objects
#   per ME396P-F2022-G03/Standards/board-data-flow.jpeg

from ESP_BT_Handler import *
from Rack import *
#import Rack as Rack
import re

rack = None

def load_classifier_data():
    pass

def rack_init(rack_map_data):
    rack = Rack()
    

def sanitize(rack_map_data, port_baud_list=None):
    def parse_line(line):
        pass
    
    def grammar_is_good(ast):
        pass
   
    def classify(ast):
        return {0 : True}
    
    def push_to_rack(the_dict):
        rack.update(the_dict)
        pass
    
    def port_listnener(port):
        line = get_messages(port = 7)  ##### udpate port if necessary (unlikely)
        ast = parse_line(line)
        if grammar_is_good(ast):
            the_dict = classify(ast)
            push_to_rack(the_dict)
    
    port_listener()

def supervise():
    load_classifier_data()
    rack_init(rack_map_data)
    while True:
        sanitize()
  
if __name__ == '__main__':
    supervise()
