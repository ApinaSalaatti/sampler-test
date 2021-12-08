import os

from sampler.sample import Sample

class SampleBanks:
    def __init__(self, config):
        self.current_bank = 0
        self.banks = []

        self.sample_dir = config["paths"]["samples"]

        for d in os.listdir(self.sample_dir):
            path = os.path.join(self.sample_dir, d)
            if not os.path.isdir(path):
                print("not a bank: " + path)
                continue
            bank = []
            index = 0
            for s in os.listdir(path):
                f = os.path.join(path, s)
                bank.append(Sample(f))
            self.banks.append(bank)

    def set_bank(self, b):
        self.current_bank = b

    def get_sample(self, index):
        return self.banks[self.current_bank][index]