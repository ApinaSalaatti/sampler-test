#
#  SamplerBox 
#
#  author:    Joseph Ernest (twitter: @JosephErnest, mail: contact@samplerbox.org)
#  url:       http://www.samplerbox.org/
#  license:   Creative Commons ShareAlike 3.0 (http://creativecommons.org/licenses/by-sa/3.0/)
#
#  samplerbox_audio.pyx: Audio engine (Cython) 
#

import numpy

import sampler.effects as effects

MAX = numpy.iinfo('int16').max
MIN = numpy.iinfo('int16').min



def mixaudiobuffers(playingsounds, frame_count):
    rmlist = []
    output = numpy.zeros((frame_count, 2), numpy.float64)

    for snd in playingsounds:
        pos = snd.pos
        end_pos = snd.loop_end if snd.loop_end > -1 else snd.sample.audio_length
        speed = snd.speed
        data = snd.sample.audio_data
  
        frames = frame_count

        ii = 0
        pos_from_sound = 0
        for i in range(frames):
            ii += 1
            pos_from_sound = int(pos + ii * speed)
            if pos_from_sound >= end_pos:
                if snd.loop_pos == -1:
                    rmlist.append(snd)
                    break
                else:
                    pos_from_sound = snd.loop_pos

            ch1 = data[pos_from_sound][0]
            ch2 = data[pos_from_sound][1]

            ch1, ch2 = effects.apply_effects_to_frame(ch1, ch2)

            '''if ch1 > MAX * 0.2:
                ch1 = MAX * 0.2
            elif ch1 < MIN * 0.2:
                ch1 = MIN * 0.2

            if ch2 > MAX * 0.2:
                ch2 = MAX * 0.2
            elif ch2 < MIN * 0.2:
                ch2 = MIN * 0.2'''

            

            output[i][0] += ch1
            output[i][1] += ch2
        snd.pos = pos_from_sound+1

    return output, rmlist

def binary24_to_int16(data, length):
    i = 0
    res = numpy.zeros(length, numpy.int16)
    b = (res.data)
    for i in range(length):
        b[2*i] = data[3*i+1]
        b[2*i+1] = data[3*i+2]
    return res