"""/////////////////////////
///
///   File: TEXTASSET/textAsset.py
///   Author: Anicet Nougaret
///   QuickDesc: The Engine's subclass managing text assets
///   License: CC BY-SA (see FLORE1/license.txt)
///
/////////////////////////"""

#import time

# ------------------------------------------------------------
# ------------------    UTIL FUNCTIONS   ---------------------
# ------------------------------------------------------------
def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# ------------------------------------------------------------

def extract_ansi(word, datalock):
    if word.startswith("bc:"):
        if word[3:] != 256:
            datalock["bc"] = "\u001b[48;5;" + word[3:] + "m \b"
        else:
            datalock["bc"] = None
        if datalock["cc"] == "\33[0m \b":
            datalock["cc"] = None
        return datalock

    if word.startswith("fc:"):
        if word[3:] != 256:
            datalock["fc"] = "\u001b[38;5;" + word[3:] + "m \b"
        else:
            datalock["fc"] = None
        if datalock["cc"] == "\33[0m \b":
            datalock["cc"] = None
        return datalock

    if word.startswith("cc:"):
        if word[3:] == "0":
            datalock["bc"] = None
            datalock["fc"] = None
            datalock["cc"] = "\33[0m \b"
            return datalock

        else:
            datalock["cc"] = "\33[" + word[3:] + "m \b"
            return datalock

# ------------------------------------------------------------

def is_escape_code(word):
    if len(word) > 6: return False

    is_bc = word.startswith("bc:")
    is_fc = word.startswith("fc:")
    is_cc = word.startswith("cc:")
    a = True if is_bc or is_fc or is_cc else False
    if a == False: return False

    b = True

    for char in word[3:]:
        if represents_int(char) == False: b = False

    if b == False: return False

    if (is_bc or is_fc) and not 0 <= int(word[3:]) <= 256: return False
    if (is_cc) and not 0 <= int(word[3:]) <= 1: return False

    return True
# ------------------------------------------------------------


# ------------------------------------------------------------
# ------------------   TextAsset Class   ---------------------
# ------------------------------------------------------------
class TextAsset:
    from .TEXTSPRITE.textSprite import TextSprite

    def __init__(self, building_manual):
        self.building_manual = building_manual
        self.generate_chart()

# ------------------------------------------------------------

    def generate_chart(self, si="α", ei="β"):
        if si == ei: return
        self.chart = {}
        self.prtcrd = set()
        x = 0
        y = 0
        self.datalock = {"bc": None, "fc": None, "cc": None}

        for line in self.building_manual:
            i = -1

            while i < len(line) - 1:
                found_escape = False
                i += 1
                if line[i] != "ª":

                    if i + 6 <= len(line):
                        if is_escape_code(line[i:i + 6]):
                            self.datalock = extract_ansi(line[i:i + 6], self.datalock)
                            i += 5
                            found_escape = True

                    if i + 5 <= len(line) and found_escape == False:
                        if is_escape_code(line[i:i + 5]):
                            self.datalock = extract_ansi(line[i:i + 5], self.datalock)
                            i += 4
                            found_escape = True

                    if i + 4 <= len(line) and found_escape == False:
                        if is_escape_code(line[i:i + 4]):
                            self.datalock = extract_ansi(line[i:i + 4], self.datalock)
                            i += 3
                            found_escape = True

                    if found_escape == False:
                        char = line[i]
                        self.prtcrd.add((x, y))
                        crd = str(x) + "|" + str(y)
                        self.chart[crd] = (char, self.datalock["bc"], self.datalock["fc"], self.datalock["cc"])

                        if self.datalock["bc"] != None:
                            pass
                            #print("\033["+str(y)+";"+str(x)+"H"+self.datalock["bc"]+char)

                        x += 1

                else:
                    x += 1

            x = 0
            y += 1

# ------------------------------------------------------------

    def to_sprite(self):
        tp = self.TextSprite()
        tp.set_asset(self)
        return tp
# ------------------------------------------------------------
