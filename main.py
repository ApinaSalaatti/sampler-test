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

s = sampler.Sampler(config)

if "keyboard" in config["devices"]["controllers"]:
    print("Enabling keyboard")
    k = sampler.controllers.KeyboardController()
    k.enable(s)

print("Sampler started")
running = True
while running:
    pass
