"""
File: engine_locals/flipbook.py
Author: Anicet Nougaret
Version: 19.11.2019.A
"""

import keyboard
"""Module for handling keyboard inputs"""

import time
import sys

class InputHandler:
    """The class for game input handling and keyboard profiles handling

    The InputHandler object can compare user inputs and the game's keyboard controls
    profile in order to modify the keyboard profile, detect actions intended by the
    player and handling actions delays.

    Attributes:
        keys (:obj:'dict |str: list[str]|'):
            A dictionnary of all the different actions for the user with all
            their corresponding keys.
        delays (:obj:'dict |str: int|):
            A dictionnary of all the different actions for the users with their
            repeat delay.

            The '__default__' entry of this dictionnary lets you set a default delay
            for all the actions you didn't added to the delays dict.
    """

    def __init__(self, keys={}, delays={}):
        """Inits the InputHandler object.

        Args:
            keys (:obj:'dict |str: list[str]|', optional):
                A dictionnary of all the different actions for the user with all
                their corresponding keys. Defaults to empty dict.
            delays (:obj:'dict |str: int|, optional):
                A dictionnary of all the different actions for the users with their
                repeat delay. Defaults to empty dict.

                The '__default__' entry of this dictionnary lets you set a default delay
                for all the actions you didn't added to the delays dict.
        """

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

    def user_set_key(self, name):
        """Records a hotkey from the keyboard and adds it for a specified action.

        Args:
            name (str): Name of the action to add a key to.
        """
        try:
            self.keys[name].append(keyboard.read_hotkey(suppress=True))
        except:
            pass

# ------------------------------------------------------------

    def del_key(self, name, key):
        """Removes one key for an action.

        Args:
            name (str): Name of the action.
            key (str): Name of the key.
        """
        try:
            self.keys[name].remove(key)
        except:
            pass

# ------------------------------------------------------------

    def is_pressed(self, name):
        """Tells if an action has one of its corresponding keys pressed.

        Note:
            Takes input delays into account.

        Args:
            name (str): Name of the action to check.

        Returns:
            True if one of the correspinding keys is pressed, False otherwise.
        """

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
