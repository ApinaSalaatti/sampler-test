import sys
import sounddevice
import toml

def set_conf():
    if len(sys.argv) < 4:
        print("Please provide setting and value")
        sys.exit(1)
    else:
        c = sys.argv[2]
        v = sys.argv[3]

    if c == "devices.output":
        config["devices"]["output"] = int(v)
    elif c == "paths.samples":
        config["paths"]["samples"] = v

    with open("config.toml", "w") as c:
        c.write(toml.dumps(config))

def get_conf(conf):
    if len(sys.argv) < 3:
        print("Please provide setting")
        sys.exit(1)
    else:
        c = sys.argv[2]
        if c == "devices.output":
            print(config["devices"]["output"])
        elif c == "paths.samples":
            print(config["paths"]["samples"])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide command (get, set, query_audio)")
        sys.exit(1)

    try:
        with open("config.toml") as c:
            config = toml.loads(c.read())
    except:
        print("Failed to open/parse configuration file")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "query_audio":
        print(sounddevice.query_devices())
    elif cmd == "get":
        get_conf()
    elif cmd == "set":
        set_conf()
    else:
        print("Unknown command: " + cmd)