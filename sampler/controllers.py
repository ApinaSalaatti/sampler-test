from pynput import keyboard
import sys

class KeyboardController:
    def enable(self, sampler, quit_func):
        self.sampler = sampler

        listener = keyboard.Listener(on_press=self.key_pressed, on_release=self.key_released, suppress=True)
        listener.start()
        self.ctrl_down = False
        self.quit = quit_func

    def key_pressed(self, key):
        if key == keyboard.Key.ctrl or key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            self.ctrl_down = True
            return

        if hasattr(key, "char"):
            if key.char == "h" or (key.char == "c" and self.ctrl_down):
                self.quit()

            elif key.char == "1":
                self.sampler.samples.set_bank(0)
            elif key.char == "2":
                self.sampler.samples.set_bank(1)
            elif key.char == "3":
                self.sampler.samples.set_bank(2)
            elif key.char == "4":
                self.sampler.samples.set_bank(3)
            elif key.char == "5":
                self.sampler.samples.set_bank(4)
            elif key.char == "6":
                self.sampler.samples.set_bank(5)
            elif key.char == "7":
                self.sampler.samples.set_bank(6)
            elif key.char == "8":
                self.sampler.samples.set_bank(7)
            elif key.char == "9":
                self.sampler.samples.set_bank(8)

            elif key.char == "q":
                self.sampler.play_sample(self.sampler.samples.get_sample(0))
            elif key.char == "w":
                self.sampler.play_sample(self.sampler.samples.get_sample(1))
            elif key.char == "e":
                self.sampler.play_sample(self.sampler.samples.get_sample(2))
            elif key.char == "a":
                self.sampler.play_sample(self.sampler.samples.get_sample(3))
            elif key.char == "s":
                self.sampler.play_sample(self.sampler.samples.get_sample(4))
            elif key.char == "d":
                self.sampler.play_sample(self.sampler.samples.get_sample(5))
            elif key.char == "z":
                self.sampler.play_sample(self.sampler.samples.get_sample(6))
            elif key.char == "x":
                self.sampler.play_sample(self.sampler.samples.get_sample(7))
            elif key.char == "c":
                self.sampler.play_sample(self.sampler.samples.get_sample(8))
            elif key.char == "r":
                self.sampler.mark_loop_pos()
            elif key.char == "t":
                self.sampler.set_volume(s.volume + 0.1)
            elif key.char == "f":
                self.sampler.toggle_effect("d")
            elif key.char == "n":
                self.sampler.set_speed(self.sampler.get_speed() * 0.9)
            elif key.char == "m":
                self.sampler.set_speed(self.sampler.get_speed() * 1.1)
            elif key.char == "y":
                self.sampler.stop_all()
    

    def key_released(self, key):
        if key == keyboard.Key.ctrl or key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            self.ctrl_down = False
            return