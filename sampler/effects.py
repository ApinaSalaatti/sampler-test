import numpy
import random
distortion = False


class Effect:
    def __init__(self):
        self.gain = 1000

    def apply(self, data):
        pass


class Distortion(Effect):
    def apply(self, data):
        self.gain * numpy.tanh(data)

def toggle_effect(e):
    global distortion
    if e == "d":
        distortion = not distortion
        print("d: " + str(distortion))

def apply_effects_to_frame(ch1, ch2):
    if distortion:
        ch1, ch2 = 5000 * numpy.tanh([ch1, ch2])

    return ch1, ch2