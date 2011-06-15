from instrument import Instrument
import pyaudio
import wave
import sys

class Microphone(Instrument):
    """Class for recording sounds from a microphone
    """
    
    def __init__(self,
                 output,
                 chunk = 1024,
                 channels = 1,
                 rate = 44100):
        """Create a new microphone, specifying details about waveform and file
        
        Arguments:
        - `chunk`:
        - `channels`:
        - `rate`:
        - `output`:
        """
        self._chunk = chunk
        self._channels = channels
        self._rate = rate
        self._output = output
        self.format = pyaudio.paInt32
        self.data = []
        self.mic = None
        
        sound = pyaudio.PyAudio()

    def start(self):
        """Start recording
        
        Arguments:
        - `self`:
        """
        self.mic = self.sound.open(format = self.format,
                                   channels = self.channels,
                                   rate = self.rate,
                                   input = True,
                                   frames_per_buffer = self.chunk)
        self.start_time = time()
        self.start_clock = clock()

    def update(self):
        """Grab new samples from the microphone
        
        Arguments:
        - `self`:
        """
        if self.mic.get_read_available() > self.chunk:
            try:
                samples = self.mic.read(self.chunk)
                self.data.append(samples)
            except IOError, e:
                if e.args[1] == pyaudio.paInputOverflowed:
                    print "ignoring overflow" # TODO use logger/warn
                    ## 32 comes from the format of the integer being
                    ## used to store the samples
                    data = '\x00' * 32 * self.chunk * self.channels
                else:
                    raise

    def stop(self):
        """Stop recording
        
        Arguments:
        - `self`:
        """
        self.stop_time = time()
        self.stop_clock = clock()
        self.mic.close()
        self.sound.terminate()
    
    def store(self):
        """Write a wave file from the sample data
        
        Arguments:
        - `self`:
        """
        wf = wave.open(self.output, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.sound.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(''.join(self.data))
        wf.close()
    
