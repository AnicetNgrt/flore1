"""/////////////////////////
///
///   File: flore1engine.py
///   Author: Anicet Nougaret
///   QuickDesc: The Engine class and the Flow class
///   License: CC BY-SA (see FLORE1/license.txt)
///
/////////////////////////"""

import ctypes
import time
import math
import os

from PIL import Image
from .util import get_palette_in_rgb, nearest_rgb_to_ansi
from .ansiRGB import ANSI_RGB
# ------------------------------------------------------------


# ------------------------------------------------------------
# ------------------    FLIPBOOK CLASS   ---------------------
# ------------------------------------------------------------
class Flipbook:
    def __init__(self, Engine, Refresh, Sprite, path="", size=[32, 32], transparent_rgb=(-1, -1, -1), fps=24, sync="True"):
        self.Refresh = Refresh
        self.asset_list = []
        if not os.path.exists(path): return

        for file in sorted(os.listdir(path)):
            filename = os.fsdecode(file)
            if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".gif"):
                asset_path = os.path.join(path, filename)
                self.asset_list.append(Engine.pic_to_textAsset(asset_path, size, transparent_rgb))

        def play(Sprite, asset_list, fps):
            if not hasattr(play, "last_frame"):
                play.last_frame = -1
            if not hasattr(play, "frame"):
                play.frame = 0
            if not hasattr(play, "speed"):
                fps_ratio = play.refresh.fps / fps
                if fps_ratio > 1:
                    play.speed = 1 / fps_ratio
                else:
                    play.speed = fps_ratio

            #print("\033["+str(len(asset_list)-1)+";1H "+("%2s" % str(play.speed)))
            #print("\033["+str(len(asset_list))+";1H "+("%2s" % str(play.last_frame)))

            play.frame = play.speed * play.i
            crt_frame = math.floor(play.frame) % len(asset_list)

            if crt_frame != play.last_frame:
                Sprite.set_asset(asset_list[crt_frame])

            play.last_frame = crt_frame

        play.sync = sync
        self.material = (play, Sprite, self.asset_list, fps)

# ------------------------------------------------------------

    def start(self):
        self.Refresh.feed(*self.material)

# ------------------------------------------------------------

    def stop(self):
        self.Refresh.terminate(*self.material)
# ------------------------------------------------------------


# ------------------------------------------------------------
# ------------------    REFRESH CLASS    ---------------------
# ------------------------------------------------------------
class Refresh:
    def __init__(self, fps=35):
        self.fps = fps
        self.pv_i = 0
        self.i = 0
        self.pv_frame = 0
        self.frame = 0
        self.stack = []

# ------------------------------------------------------------

    def terminate(self, func, *args, **kwargs):
        self.stack.remove((func, args, kwargs))

# ------------------------------------------------------------

    def feed(self, func, *args, **kwargs):
        self.stack.append((func, args, kwargs))

# ------------------------------------------------------------

    def do(self):
        for func, args, kwargs in self.stack:
            if hasattr(func, "refresh") == False:
                func.__dict__["refresh"] = self
            if hasattr(func, "sync") == False:
                func.__dict__["sync"] = True
            if not hasattr(func, "i"):
                func.__dict__["i"] = 0
            else:
                if func.sync == True and (self.frame-self.pv_frame) > 0:
                    func.__dict__["i"] += self.frame-self.pv_frame  
                    func(*args, **kwargs)
                elif func.sync == False:
                    func.__dict__["i"] += 1
                    func(*args, **kwargs)



# ------------------------------------------------------------

    def run(self, debug=False):
        required_fps = self.fps

        start_time = time.time()
        
        self.do()

        exec_time = time.time()
        latency = exec_time - start_time

        if latency < 0.0001: latency = 0.0001

        fps = 1 / latency

        self.pv_frame = self.frame
        self.pv_i = self.i

        if fps > required_fps:
            time.sleep(((1 / required_fps) - latency)/1.1)
            self.i += 1
        
        if required_fps >= fps:
            self.i += required_fps / fps
        
        self.frame = round(self.i)
        #print(self.i)

        if debug:
            otp = "\33[0m\033[1;0H| >>>> Refresh.\33[34mrun \33[33mdebug"
            print(otp)

            otp = "\033[2;0H\33[0m|\u001b[38;5;15m\u001b[48;5;16m  INVERTED_LATENCY_CAP: "
            print(otp + str(self.fps))

            otp = "\33[0m\033[3;0H|\u001b[48;5;16m\u001b[38;5;15m  LATENCY: "
            print("%s%1.2f   " % (otp, latency))

            otp = "\033[4;0H\33[0m|\u001b[38;5;16m"
            if fps >= self.fps:
                otp += "\u001b[48;5;85m"
            elif self.fps * 0.8 <= fps < self.fps:
                otp += "\u001b[48;5;87m"
            elif self.fps * 0.5 <= fps < self.fps * 0.8:
                otp += "\u001b[48;5;221m"
            elif self.fps * 0.2 <= fps < self.fps * 0.5:
                otp += "\u001b[48;5;202m"
            else:
                otp += "\u001b[48;5;9m"
            otp += "  EXECUTION_FREQUENCY: "
            print("%s%1.2f   " % (otp, fps))

            otp = "\33[0m\033[5;0H|\u001b[48;5;16m\u001b[38;5;15m  FRAME_DIFF: "
            print("%s%1.2f   " % (otp, self.frame-self.pv_frame))

            otp = "\33[0m\033[6;0H|\u001b[48;5;16m\u001b[38;5;15m  ACCUMULATOR_DIFF: "
            print("%s%1.2f   " % (otp, self.i-self.pv_i))

            final_time = time.time()
            total_latency = final_time - start_time
            otp = "\33[0m\033[7;0H|\u001b[38;5;15m\u001b[48;5;16m  STABILISED_FREQUENCY: "
            print("%s%1.2f   " % (otp, (self.i - self.pv_i)/total_latency))
        
# ------------------------------------------------------------


# ------------------------------------------------------------
# ------------------     ENGINE CLASS    ---------------------
# ------------------------------------------------------------
class Engine:
    def __init__(self, auto_scale=False, win_mode=False, logo=False):
        print(chr(27) + "[H" + chr(27) + "[J")
        self.vscenes = {}
        self.auto_scale = auto_scale

        if win_mode == True:
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

        if logo == True:
            tmp_scene = self.new_scene("tmp", 1, 1, 64, 64, 1)
            logo_asset = self.pic_to_textAsset(path="flore1/logo.png", new_size=[32,32], transparent_rgb=(0,0,0))
            logo_sprite = logo_asset.to_sprite()
            tmp_scene.put(logo_sprite,32,16,0)
            tmp_scene.show()
            time.sleep(5)
            self.del_scene("tmp")
            print("\33[0m")


    from .VIRTUALSCENE.virtualScene import VirtualScene
    from .TEXTASSET.textAsset import TextAsset

    def new_scene(self, name, coord_x, coord_y, res_x, res_y, layer_count):
        self.vscenes[name] = self.VirtualScene(coord_x, coord_y, res_x, res_y, layer_count, self.auto_scale)
        return self.vscenes[name]

# ------------------------------------------------------------

    def del_scene(self, name):
        del self.vscenes[name]

# ------------------------------------------------------------

    def new_sprite(self):
        return self.TextAsset.TextSprite()

# ------------------------------------------------------------

    def find_trsprt_index(self, rgb_palette, transparent_RGB):
        if transparent_RGB in rgb_palette:
            return rgb_palette.index(transparent_RGB)
        else:
            return None

# ------------------------------------------------------------

    def pic_to_textAsset(self, path="", new_size="AUTO", transparent_rgb=(-1, -1, -1)):
        img_file = Image.open(path)
        [xs, ys] = img_file.size
        building_manual = []

        scale_filt = Image.NEAREST
        if not path.endswith(".png"):
            scale_filt = Image.LANCZOS

        if new_size == "AUTO":
            while (xs > 128 * (xs / ys) and ys > 128):
                xs = int(xs / 1.3)
                ys = int(ys / 1.3)
        else:
            xs = int(new_size[0])
            ys = int(new_size[1])

        img_file = img_file.resize((int(xs), int(ys)), scale_filt)
        img = img_file.convert("P")
        rgb_palette = get_palette_in_rgb(img)

        trsprt_index = self.find_trsprt_index(rgb_palette, transparent_rgb)

        if len(rgb_palette) < 255:
            found_black = False
            i = 0
            while i < len(rgb_palette):
                if rgb_palette[i] == (0, 0, 0) and found_black == False:
                    found_black = True
                elif rgb_palette[i] == (0, 0, 0) and found_black == True:
                    del rgb_palette[i]
                    i -= 1
                i += 1

        img = img.load()
        ansi_palette = []
        for color in rgb_palette:
            r, g, b = color
            c_array = [r, g, b]
            nearest = nearest_rgb_to_ansi(c_array, ANSI_RGB)
            ansi_palette.append(nearest)

        pv_code = -1
        code = 0
        for y in range(0, ys):
            building_manual.append("")
            for x in range(0, xs):
                ci = img[x, y]
                code = ansi_palette[ci]
                #print("%s%2s" % (("\33["+str(y)+";"+str((x*2)+1)+"H"),"\33[38;5;"+str(ci)+"m@@"))

                if code != pv_code:
                    pixel = "bc:" + str(code) + "  "
                else:
                    pixel = "  "

                if trsprt_index is not None:
                    if rgb_palette[ci] == transparent_rgb:
                        pixel = "ªª"

                pv_code = code
                building_manual[y] += pixel

            pv_code = -1

        picAsset = self.TextAsset(building_manual)
        return picAsset