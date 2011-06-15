import instrument 
import pyxid

class VoiceKey(Instrument):
    """Methods for collecting data from a Cedrus SV-1 Voice Key
    """
    
    def __init__(self):
        """Find the device on the system and initialize it
        """

        ## declare some variables that are used to interact with the
        ## voice key
        self.vk = None
        self.response = None

        ## assume that the voice key is the only XID device currently
        ## plugged in
        devices = pyxid.get_xid_devices()
        ## According to documentation, Windows machines may have to
        ## check twice
        if len(devices) > 0:
            self.vk = devices[0]
        else:
            devices = pyxid.get_xid_devices()
            self.vk = devices[0]

        ## reset the experiment timer
        self.vk.reset_base_timer()

    def start(self):
        """Start a new trial on the voice key
        
        Arguments:
        - `self`:
        """
        self.vk.reset_rt_timer()
        self.start_time = time()
        self.start_clock = clock()

    def update(self):
        """Check for a response on the voice key
        
        Arguments:
        - `self`:
        """
        self.vk.poll_for_response()
        if dev.response_queue_size() > 0:
            self.response = dev.get_next_response()

    def stop(self):
        """Record the time the voice key stops
        
        Arguments:
        - `self`:
        """
        self.stop_time = time()
        self.stop_clock = clock()

    def log(self, message):
        """Log the most recent event
        
        Arguments:
        - `self`:
        - `message`:
        """
        pass
