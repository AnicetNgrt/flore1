"""/////////////////////////
///
///   File: VIRTUALSCENE/virtualScene.py
///   Author: Anicet Nougaret
///   License: CC BY-SA (see FLORE1/license.txt)
///
/////////////////////////"""

import os
import time
import sys


def print_crd(content, col, row):
    sys.stdout.write("\33[0m\033["+str(row)+";"+str(col)+"H")
    sys.stdout.write(content)
    sys.stdout.flush()


def extract_color_code(string):
    if not (string.startswith("\u001b[48;5;") or string.startswith("\u001b[38;5;")) or not string.endswith("m"): return
    return int(string[12:len(string)-2])

# ------------------------------------------------------------
# ------------------  VirtualScene Class ---------------------
# ------------------------------------------------------------
class Scene:
    def __init__(self, coord_x=0, coord_y=0, res_x=64, res_y=64, layer_count=10, scale=True):
        self.layers = []

        for l in range(0, layer_count):
            self.layers.append([])

        self.coord_x = int(coord_x)
        self.coord_y = int(coord_y)
        self.res_x = int(res_x * 2)
        self.res_y = int(res_y)

        self.prtcrd = set()
        self.prtcrd_rv = set()
        self.pv_prtcrd = set()
        self.pv_prtcrd_rv = set()
        self.chart = set()
        self.pv_chart = set()

        self.frame_event = False

        if scale == True:
            os.system('mode con: cols=' + str(res_x * 2 + coord_x * 4) + ' lines=' + str(res_y + coord_y * 2) + '')

    # ------------------------------------------------------------

    def put(self, sprite, crd_x, crd_y, layer):

        self.frame_event = True

        if layer >= len(self.layers):
            return

        if sprite.scene == self:
            self.erase(sprite)

        sprite.x = crd_x
        sprite.y = crd_y
        sprite.scene = self
        sprite.layer = int(layer)

        sprite.act_prtcrd = set()

        for px in sprite.prtcrd:
            x, y = px
            if 0 < (x + int(sprite.x)) < self.res_x and 0 < (y + int(sprite.y)) < self.res_y:
                sprite.act_prtcrd.add((x + int(sprite.x), y + int(sprite.y)))

        self.layers[layer].append(sprite)

# ------------------------------------------------------------

    def erase(self, sprite):
        self.layers[sprite.layer].remove(sprite)
        self.frame_event = True
        sprite.x = None
        sprite.y = None
        sprite.layer = None
        sprite.scene = None

# ------------------------------------------------------------

    def gen_stream(self, debug, repeat_color, filter):
        self.stream = "\33[0m"
        self.prtcrd = set()
        self.prtcrd_rv = set()
        self.chart = set()

        start_time = time.time()

        sprite_id = 0

        for layer in reversed(self.layers):
            for sprite in layer:
                px_set = sprite.act_prtcrd.copy()

                if not px_set.issubset(self.prtcrd):
                    is_dis = px_set.isdisjoint(self.prtcrd)

                    if not is_dis: px_set.difference_update(self.prtcrd)

                    for px in px_set:
                        x, y = px

                        xp = (y, x)

                        self.prtcrd.add(px)
                        self.prtcrd_rv.add(xp)

                        crd = str(x - int(sprite.x)) + "|" + str(y - int(sprite.y))

                        self.chart.add((xp, sprite.chart[crd]))

        chart_time = time.time()

        self.datalock = {
            "x": None,
            "y": None,
            "bc": None,
            "fc": None,
            "cc": None
        }

        for el in sorted(self.chart - self.pv_chart):
            xp, data = el
            y, x = xp

            char, bc, fc, cc = data

            if x - 1 != self.datalock["x"] or y != self.datalock["y"]:
                self.stream += "\033[" + str(y + self.coord_y) + ";" + str(
                    x + self.coord_x) + "H"
            if repeat_color == False:
                if bc is not None and bc != self.datalock["bc"]:
                    self.stream += bc
                if fc is not None and fc != self.datalock["fc"]:
                    self.stream += fc
                if cc is not None and cc != self.datalock["cc"]:
                    self.stream += cc
            else:
                if bc is not None:
                    self.stream += bc
                if fc is not None:
                    self.stream += fc
                if cc is not None:
                    self.stream += cc

            self.datalock["x"] = x
            self.datalock["y"] = y
            self.datalock["bc"] = bc
            self.datalock["fc"] = fc
            self.datalock["cc"] = cc

            self.stream += char

        stream_time = time.time()

        self.pv_x = None
        self.pv_y = None

        for xp in sorted(self.pv_prtcrd_rv - self.prtcrd_rv):
            y, x = xp

            if True:
                self.stream += "\33[0m" + "\033[" + str(
                    y + self.coord_y) + ";" + str(x + self.coord_x) + "H" + " "
            else:
                self.stream += "\33[0m" + " "

            self.pv_x = x
            self.pv_y = y

        self.pv_prtcrd_rv = self.prtcrd_rv.copy()
        self.pv_chart = self.chart.copy()

        end_time = time.time()

        if debug:
            print("\33[0m\033[1;40H| >>>> Scene \33[33mdebug")
            print("\33[0m\033[2;40H| \33[40m\33[37m FRAME_COMPUTING: %.3f s" % ((chart_time - start_time)))
            print("\33[0m\033[3;40H| \33[40m\33[37m STREAM_COMPUTING: %.3f s" % ((stream_time - chart_time)))
            print("\33[0m\033[4;40H| \33[40m\33[37m ERASE_COMPUTING: %.3f s" % ((end_time - stream_time)))
            print("\33[0m\033[5;40H| \33[40m\33[33m TOTAL_COMPUTING_LATENCY: %.3f s" % ((end_time - start_time)))

# ------------------------------------------------------------

    def show(self, force=False, debug=False, repeat_color=False, filter={"r":0,"g":0,"b":0}):
        if self.frame_event == True or force == True:
            genesis_time = time.time()

            if force == True:
                self.pv_prtcrd = set()
                self.pv_prtcrd_rv = set()
                self.pv_chart = set()

            self.gen_stream(debug, repeat_color, filter)

            start_time = time.time()

            sys.stdout.write(self.stream)
            sys.stdout.flush()
            end_time = time.time()
            latency = (end_time - genesis_time)
            if latency == 0: latency = 0.00001

            if debug:
                print("\33[0m\033[6;40H| \33[45m\33[37m SYS.STDOUT.WRITE: %9f s" % ((end_time - start_time)))
                print("\33[0m\033[7;40H| \33[45m\33[37m EXPECTED_FPS: %.2f     " % (round(1 / latency)))

            self.frame_event = False

# ------------------------------------------------------------

    def hide(self):
        self.frame_event = True
        x1 = self.coord_x
        y1 = self.coord_y
        x2 = self.coord_x + self.res_x
        y2 = self.coord_y + self.res_y

        for y in range(y1, y1 + (y2 - y1)):
            string = ""
            for x in range(x1, x1 + (x2 - x1)):
                string += " "
            print_crd(string, x1, y)
# ------------------------------------------------------------

"""
Hey dear stranger,
Thanks for reviewing my code. I hope you will find good use of it.
cheers

Anicet
                                ___
 ,~####~,                    __/__/_
(S O-oO)S  ' , -=o>)',   []-(0_ 0  )--|>>>>>  .  , ~ '~ .\(^ o.o^)

"""
