import keyboard
import time
import sys



# ------------------------------------------------------------
# ------------------  INPUTHANDLER CLASS  --------------------
# ------------------------------------------------------------
class InputHandler:
    def __init__(self, keys={}, delays={}):
        self.delays = delays
        if not ("__default__" in self.delays):
            self.delays["__default__"] = 0.1
        self.keys = keys
        self.last = {
            "name": None,
            "delay": 0,
            "time": time.time()
        }

# ------------------------------------------------------------

    def set_key(self, name, keys = []):
        self.keys[name] = keys

# ------------------------------------------------------------

    def user_set_key(self, name, keys = []):
        try:
            self.keys[name].append(keyboard.read_hotkey(suppress=True))
        except:
            pass

# ------------------------------------------------------------

    def add_key(self, name, key):
        try:
            self.keys[name].append(key)
        except:
            pass

# ------------------------------------------------------------

    def del_key(self, name, key):
        try:
            self.keys[name].remove(key)
        except:
            pass

# ------------------------------------------------------------

    def is_pressed(self, name):
        try:
            for key in self.keys[name]:
                if keyboard.is_pressed(key):
                    if self.last["name"] == name and time.time() - self.last["time"] < self.last["delay"]:
                        return False
                    self.last["name"] = name
                    if name in self.delays:
                        self.last["delay"] = self.delays[name]
                    else:
                        self.last["delay"] = self.delays["__default__"]
                    self.last["time"] = time.time()
                    return True
        except:
            pass

        return False
# ------------------------------------------------------------
