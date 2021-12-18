import sampler

import sys
import toml

config = None
try:
    with open("config.toml") as c:
        config = toml.loads(c.read())
except:
    print("Failed to open/parse configuration file")
    sys.exit(1)

running = True
def quit():
    global running
    running = False

s = sampler.Sampler(config)
sequencer = sampler.Sequencer(config, s)

if "keyboard" in config["devices"]["controllers"]:
    print("Enabling keyboard")
    k = sampler.controllers.KeyboardController()
    k.enable(s, quit)

print("Sampler started")

while running:
    sequencer.update()
