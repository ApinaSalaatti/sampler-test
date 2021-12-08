from pynput import keyboard

class KeyboardController:
    def enable(self, sampler):
        self.sampler = sampler

        listener = keyboard.Listener(on_press=self.key_pressed, on_release=self.key_released, suppress=True)
        listener.start()

    def key_pressed(self, key):
        if key.char == "w":
            self.sampler.play_sample(self.sampler.samples.get_sample(0))
        elif key.char == "e":
            self.sampler.play_sample(self.sampler.samples.get_sample(1))
        elif key.char == "r":
            self.sampler.mark_loop_pos()
        elif key.char == "t":
            self.sampler.set_volume(s.volume + 0.1)
        elif key.char == "d":
            sampler.toggle_effect("d")
        elif key.char == "z":
            self.sampler.set_speed(self.sampler.get_speed() * 0.9)
        elif key.char == "x":
            self.sampler.set_speed(self.sampler.get_speed() * 1.1)
    

    def key_released(self, key):
        pass