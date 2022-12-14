from datetime import datetime


class Rack:
    def __init__(self, name='unnamed'):
        '''
        
        '''
        self.name = name
        self.bays = {} # Dict
        self.updated = 0 # Time stamp of last update
    
    def update_rack(self, status):
        '''
        
        '''
        self.updated = datetime.now() # set time to now
        
        should_log = False
        
        # Check each bay in the new status stored in status
        for bay, state in status.items():
            
            # Check whether the bay exists
            if bay in self.bays:
                # Check whether the bay's state has changed
                if self.bays[bay] != state:
                    # If the Bay has changed, flag should_log
                    should_log = True
            else:
                should_log = True
            
            
            self.bays[bay] = state
        
        if should_log:
            self.log()
        
        '''# If the bay does not already exist, add it and log the update
            if bay not in self.bays:
                self.bays[bay] = state
                self.log_bay(bay, state)
            
            # If the bay exists and its status has changed, record and log the change
            elif state is not self.bays[bay]:
                self.bays[bay] = state
                self.log_bay(bay, state)'''
    
    def log(self):
        '''
        
        '''

        f = open('rack-log.txt', 'a')
        f.write('{0};{1};{2}\n'.format(self.name, self.updated, self.bays))
        f.close()


