import numpy
import random
distortion = False

def toggle_effect(e):
    global distortion
    if e == "d":
        distortion = not distortion
        print("d: " + str(distortion))

def apply_effects_to_frame(ch1, ch2):
    if distortion:
        ch1, ch2 = 5000 * numpy.tanh([ch1, ch2])

    return ch1, ch2