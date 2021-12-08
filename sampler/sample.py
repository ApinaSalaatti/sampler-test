from scipy.io.wavfile import read
import numpy

class Sample:

    def __init__(self, filename):
        a = read(filename)
        self.audio_data = numpy.array(a[1],dtype=numpy.int16)
        self.audio_length = len(self.audio_data)