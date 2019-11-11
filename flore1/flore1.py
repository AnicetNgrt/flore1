"""/////////////////////////
///
///   File: flore1.py
///   Author: Anicet Nougaret
///   License: CC BY-SA (see FLORE1/license.txt)
///
/////////////////////////"""

# Python native
import ctypes
import sys
import math
import time
import os
from functools import lru_cache

# pypI
import keyboard
import clipboard

# local
from .engine_classes import *

# -----------------------------------------------------------

def resize_console(col, row):
    os.system('mode con: cols=' + str(col) + ' lines=' + str(row) + '')

def create_dir_and_file(dir, name):
    path = os.path.join(dir, name)
    if not os.path.exists(dir):
        os.makedirs(dir, exist_ok=True)
    open(path, 'a').close()
    return path

def save_var_as(var, dir, filename, ext):
    if not filename.endswith(ext):
        path = create_dir_and_file(dir, filename+ext)
    else:
        path = create_dir_and_file(dir, filename)
    with open(path, "r+") as f:
        if os.path.getsize(path) == 0:
            f.write(str(var))
    return path

def load_var_from(path):
    if not os.path.exists(path):
        print("PATH DOES NOT EXIST")
        time.sleep(2)
        return None
    with open(path, "r") as f:
        if os.path.getsize(path) <= 999999999:
            return eval(f.read())
        else:
            print("FILE TOO BIG")
            time.sleep(2)
            return None

def save_asset_as(asset, folder, name):
    path = os.path.join(folder, name)
    if not hasattr(asset, "chart") or not hasattr(asset, "prtcrd"): return
    save_var_as((asset.chart, asset.prtcrd), folder, name, ".jus")

def load_asset_from(path):
    chart, prtcrd = load_var_from(path)
    if chart != None:
        ta = TextAsset()
        ta.chart = chart
        ta.prtcrd = prtcrd
        return ta
    else: return TextAsset("")

def load_assets_from(folder):
    assets = []
    if not os.path.exists(folder): return []
    for file in sorted(os.listdir(folder)):
        if not file.endswith(".jus"): continue
        path = os.path.join(folder, file)
        chart, prtcrd = load_var_from(path)
        if chart != None:
            ta = TextAsset()
            ta.chart = chart
            ta.prtcrd = prtcrd
            assets.append(ta)
        else: continue
    return assets

def fix_color():
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

def show_logo(duration=5):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'engine_assets_lib\logo.png')
    PicConv = PictureConverter()
    scene = Scene(1 , 1, 64, 40, 1)
    logo_asset = PicConv.pic2asset(path=filename, size=[32,32], alpha=(0,0,0))
    logo_sprt = TextSprite(asset=logo_asset)
    scene.put(logo_sprt,32,4,0)
    scene.show()
    print_crd("\033[38;5;8mmade with \033[38;5;198m  F L O R E 1    E N G I N E  ", 43, 3)
    time.sleep(duration)
    print("\33[0m")

def clear_screen():
    print(chr(27) + "[H" + chr(27) + "[J")

def cursor_to_crd(col, row):
    sys.stdout.write("\33[0m\033["+str(row)+";"+str(col)+"H")

def print_crd(content, col, row):
    sys.stdout.write("\33[0m\033["+str(row)+";"+str(col)+"H")
    sys.stdout.write(content)
    sys.stdout.flush()

def save_cursor():
    sys.stdout.write("\033[s")
    sys.stdout.flush()

def restore_cursor():
    sys.stdout.write("\033[u")
    sys.stdout.flush()

def extract_ints(string):
    list = []
    el = ""
    for char in string:
        if char.isdigit():
            el += char
        if not char.isdigit():
            if el != "":
                list.append(int(el))
                el = ""
    return list

def draw_rectangle(char, topleft_x, topleft_y, bottright_x, bottright_y):
    x1 = int(topleft_x)
    y1 = int(topleft_y)
    x2 = int(bottright_x)
    y2 = int(bottright_y)

    for y in range(y1, y1 + (y2 - y1)):
        string = ""
        for x in range(x1, x1 + (x2 - x1)):
            string += char
        print_crd(string, x1, y)

def draw_line(char, xa, ya, xb, yb):
    xa = int(xa); ya = int(ya); xb = int(xb); yb = int(yb)
    if xa == xb and ya == yb: return print_crd(char, xa, ya)

    xa, xb, ya, yb = (xa, xb, ya, yb) if xa < xb else (xb, xa, yb, ya)

    a = (yb - ya) / (xb - xa) if xb != xa else -2

    if -1 <= a <= 1:
        for x in range(0, xb - xa):
            print_crd(char, x+xa, math.floor(x*a + ya))

    if a < -1 or a > 1:
        xa, xb, ya, yb = (xa, xb, ya, yb) if ya > yb else (xb, xa, yb, ya)

        a = (xa - xb) / (ya - yb)

        for y in range(0, ya - yb):
            print_crd(char, math.floor(y*a + xb), y+yb)

def sys_print(string):
    sys.stdout.write(string)
    sys.stdout.flush()

def get_hotkey():
    if not hasattr(get_hotkey, "last"):
        get_hotkey.last = {
            "hotkey": None,
            "delay": 0,
            "time": time.time()
        }
    hotkey = str(keyboard.read_hotkey(suppress=False))

    if hotkey == get_hotkey.last["hotkey"]:
        if get_hotkey.last["time"] + get_hotkey.last["delay"] > time.time():
            return None
        else:
            get_hotkey.last["time"] = time.time()
            get_hotkey.last["delay"] /= 1.5
    else:
        get_hotkey.last["hotkey"] = hotkey
        get_hotkey.last["delay"] = 0.3
        get_hotkey.last["time"] = time.time()

    return hotkey

def get_last_hotkey():
    if not hasattr(get_hotkey, "last"):
        get_hotkey.last = {
            "hotkey": None,
            "delay": 0,
            "time": time.time()
        }
    return get_hotkey.last["hotkey"]


def get_key():
    if not hasattr(get_key, "last"):
        get_key.last = {
            "key": None,
            "delay": 0,
            "time": time.time()
        }
    key = str(keyboard.read_key(suppress=False))

    if key == get_key.last["key"]:
        if get_key.last["time"] + get_key.last["delay"] > time.time():
            return None
        else:
            get_key.last["time"] = time.time()
            get_key.last["delay"] /= 1.5
    else:
        get_key.last["key"] = key
        get_key.last["delay"] = 0.3
        get_key.last["time"] = time.time()

    return key

def get_last_key():
    if not hasattr(get_key, "last"):
        get_key.last = {
            "key": None,
            "delay": 0,
            "time": time.time()
        }
    return get_key.last["key"]

def alt_input(x, y, prompt="", maxline=999, maxchar=99999, digit_only=False, max_width=9999):
    string = ""
    key = ""
    crt_y = y
    crt_x = x
    clip = ""
    last = {
        "key": None,
        "delay": 0,
        "time": time.time()
    }
    cursor_to_crd(x, y)

    @lru_cache(maxsize=32)
    def line_count(string):
        count = 1
        for char in string:
            if char == "\n": count += 1
        return count

    def longest_line(string):
        max = 0
        count = 0
        for char in string:
            count += 1
            if char == "\n":
                if count > max: max += count - max
                count = 0
        return max

    sys.stdout.write(prompt)
    sys.stdout.flush()

    while key != "enter":
        time.sleep(0.05)

        if keyboard.is_pressed("ctrl+c"):
            clipboard.copy(clip)
            continue
        if keyboard.is_pressed("ctrl+v"):
            pasted = clipboard.paste()
            if len(pasted) + len(string) > maxchar: continue
            string += pasted
            crt_x += len(pasted)
            sys.stdout.write(pasted)
            sys.stdout.flush()
            time.sleep(0.2)
            continue

        key = str(keyboard.read_key(suppress=False))

        if key == last["key"]:
            if last["time"] + last["delay"] > time.time():
                continue
            else:
                last["time"] = time.time()
                last["delay"] /= 1.5
        else:
            last["key"] = key
            if last["key"] == "backspace":
                last["delay"] = 0.15
            else:
                last["delay"] = 0.3
            last["time"] = time.time()

        if key == "backspace":
            if crt_x == x: continue
            crt_x -= 1
            if len(string) >= 1: string = string[:len(string)-1]
            sys.stdout.write("\b \b")
            sys.stdout.flush()
        elif key == "suppr":
            while string[len(string)-1] != " " and crt_x > x+1:
                crt_x -= 1
                string = string[:len(string)-1]
                sys.stdout.write("\b \b")
                sys.stdout.flush()
        elif key == "right shift" and line_count(string) < maxline:
            string += "\n"
            crt_y += 1
            crt_x = x
            cursor_to_crd(x, crt_y)
            sys.stdout.flush()
        elif key == "space" and len(string) < maxchar:
            crt_x += 1
            string += " "
            sys.stdout.write(" ")
            sys.stdout.flush()
        elif len(key) == 1 and len(string) < maxchar:
            if digit_only == True and key.isdigit() == False: continue
            crt_x += 1
            string += key
            sys.stdout.write(key)
            sys.stdout.flush()

    draw_rectangle(" ", x, y, x+longest_line(string), y+line_count(string))
    return string
