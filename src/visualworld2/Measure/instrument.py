from time import time, clock

class Instrument(object):
    """Base class for instruments used to measure particpant responses.
    """
    
    def __init__(self):
        """
        """
        self.start_time = None
        self.stop_time = None
        self.start_clock = None
        self.stop_clock = None
        self.resonse = None
        pass
        
    def start(self):
        """Start the meaurement process.
        
        Arguments:
        - `self`:
        """
        self.start_time = time.time()
        self.start_clock = time.clock()
        pass

    def update(self):
        """Update the measurement process.
        
        Arguments:
        - `self`:
        """
        pass

    def stop(self):
        """Stop the measurement process.
        
        Arguments:
        - `self`:
        """
        self.stop_time = time.time()
        self.stop_clock = time.clock()
        pass

    def log(self, message):
        """Send a message from the measurement process to the log.
        
        Arguments:
        - `self`:
        """
        pass

    def store(self, filename):
        """Write the results of the measurement to a file.
        
        Arguments:
        - `self`:
        - `filename`:
        """
        pass
