"""

"""
from datetime import datetime


class Rack:
    def __init__(self):
        '''
        
        '''
        self.bays = {} # Dict
        self.updated = 0 # Time stamp of last update
    
    def update_rack(self, status):
        '''
        
        '''
        self.updated = datetime.now() # set time to now
        
        for bay, state in status.items():
            if bay not in self.bays:
                self.bays[bay] = status
                self.log(bay, state, self.updated)
            elif state != self.bays[bay]:
                self.bays = status
                self.log(bay, state, self.updated)
    
    def log(bay, status, time):
        '''
        
        '''
        # print the change to a file
        f = open('rack-log', 'a')
        f.write('')