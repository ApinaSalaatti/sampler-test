import sounddevice
import time

import wave
import numpy
import os
import math
import sys

from scipy.io.wavfile import read

from sampler.samplebanks import SampleBanks

#import pyximport
#pyximport.install()
import sampler.mixer
from sampler.sample import Sample
import sampler.effects as effects

MAX_POLYPHONY = 80

class PlayingSample:
    def __init__(self, sample):
        self.sample = sample
        self.loop_pos = -1
        self.loop_end = -1
        self.pos = 0
        self.speed = 1

        self.use_fadeout = False
        self.fadeout_left = 30000 # fadeout takes 30000 frames

        self.marking_loop = 0

    def mark_loop(self):
        if self.marking_loop == 0:
            self.loop_pos = self.pos
            self.marking_loop = 1
        elif self.marking_loop == 1:
            self.loop_end = self.pos
            self.marking_loop = 2
        elif self.marking_loop == 2:
            self.clear_loop()
            self.marking_loop = 0

    def clear_loop(self):
        self.loop_end = -1
        self.loop_pos = -1



class Sampler:
    def __init__(self, config):
        self.samples = SampleBanks(config)
        #print(sounddevice.query_devices())
        try:
            #print("Opening sound device")
            out_dev = config["devices"]["output"]
            self.sd = sounddevice.OutputStream(device=out_dev, blocksize=512, samplerate=44100, channels=2, dtype='int16', callback=self.audioCallback)
            self.sd.start()
        except:
            print("Failed to open sound device")
            sys.exit(1)

        self.audio_data = None
        self.audio_length = 0

        self.playing_sounds = []

        #self.volume = 10 ** (-12.0/20)
        self.volume = 0.8

        self.setting_loop = False
        self.current_sample = None

    def mark_loop_pos(self):
        if self.current_sample:
            self.current_sample.mark_loop()

    def clear_loops(self):
        for s in self.playing_sounds:
            s.clear_loop()

    def set_speed(self, s):
        if self.current_sample:
            self.current_sample.speed = s
    def get_speed(self):
        if self.current_sample:
            return self.current_sample.speed
        
        return 0

    def toggle_effect(self, e):
        effects.toggle_effect(e)

    def set_volume(self, v):
        self.volume = v

    def stop_all(self):
        self.playing_sounds = []

    def audioCallback(self, outdata, frame_count, time_info, status):
        if len(self.playing_sounds) > 0:
            self.playing_sounds = self.playing_sounds[-MAX_POLYPHONY:]
            b, rmlist = sampler.mixer.mixaudiobuffers(self.playing_sounds, frame_count)
            for e in rmlist:
                try:
                    self.playing_sounds.remove(e)
                    if e == self.current_sample:
                        self.current_sample = None
                except:
                    pass
            b *= self.volume
            outdata[:] = b.reshape(outdata.shape)
        else:
            outdata[:] = numpy.zeros((frame_count, 2), numpy.int16)


    def play_sample(self, s):
        if s is not None:
            self.current_sample = PlayingSample(s)
            self.playing_sounds.append(self.current_sample)