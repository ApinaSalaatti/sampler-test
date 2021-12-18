import time

class Sequencer:
    def __init__(self, config, sampler):
        self.sampler = sampler
        self.tempo = 60
        self.steps_per_beat = 8
        self.next_step_time = time.time() + self.step_length()
        self.current_step = 1
        self.sample = 3

    def step_length(self):
        return 60.0 / (self.tempo * self.steps_per_beat)

    def update(self):
        t = time.time()
        if t >= self.next_step_time:
            self.next_step_time += self.step_length()
            self.step_start()

    '''def step_start(self):
        #print("step starting")
        #print(str(time.time()))
        self.sampler.play_sample(self.sampler.samples.get_sample(1))
        #self.sample = 1 if self.sample == 3 else 3'''

