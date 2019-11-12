import os

# PypI
from PIL import Image

# local
from .engine_consts import ANSI_RGB
from .textAsset import TextAsset


class PictureConverter:
    def __init__(self):
        self._cache_path = os.path.join("__flore1cache__","_pic_cache.jus")

        if not os.path.exists("__flore1cache__"):
            os.makedirs("__flore1cache__", exist_ok=True)

        open(self._cache_path, 'a').close()

        with open(self._cache_path, "r+") as f:
            if os.path.getsize(self._cache_path) == 0:
                f.write(str(dict()))
                self._cache = dict()
            else:
                self._cache = eval(f.read())

    def pics2assets(self, dir="", size="AUTO", alpha=(-1, -1, -1)):
        assets = []
        if not os.path.exists(dir): return assets

        for file in sorted(os.listdir(dir)):
            filename = os.fsdecode(file)
            if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".gif"):
                asset_path = os.path.join(dir, filename)
                assets.append(self.pic2asset(asset_path, size, alpha))

        return assets

# ------------------------------------------------------------

    def pic2asset(self, path="", size="AUTO", alpha=(-1, -1, -1)):
        key = str((path, size, alpha))
        if key in self._cache.keys():
            return TextAsset(self._cache[key])

        img_file = Image.open(path)
        [xs, ys] = img_file.size
        building_manual = []

        scale_filt = Image.NEAREST
        if not path.endswith(".png"):
            scale_filt = Image.LANCZOS

        if size == "AUTO":
            while (xs > 128 * (xs / ys) and ys > 128):
                xs = int(xs / 1.3)
                ys = int(ys / 1.3)
        else:
            xs = int(size[0])
            ys = int(size[1])

        img_file = img_file.resize((int(xs), int(ys)), scale_filt)
        img = img_file.convert("P")
        rgb_palette = self.get_palette_in_rgb(img)

        trsprt_index = self.find_trsprt_index(rgb_palette, alpha)

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
            nearest = self.nearest_rgb_to_ansi(c_array, ANSI_RGB)
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
                    if rgb_palette[ci] == alpha:
                        pixel = "ªª"

                pv_code = code
                building_manual[y] += pixel

            pv_code = -1

        self._cache[key] = building_manual

        with open(self._cache_path, "w") as f:
            f.truncate(0)
            f.write(str(self._cache))

        return TextAsset(building_manual)

# ------------------------------------------------------------

    def find_trsprt_index(self, rgb_palette, transparent_RGB):
        if transparent_RGB in rgb_palette:
            return rgb_palette.index(transparent_RGB)
        else:
            return None

# ------------------------------------------------------------

    def nearest_rgb_to_ansi(self, c, ref):
        dist_list = []
        c[0] -= 0 # in case you want to filter things up
        c[1] += 0
        c[2] += 0
        for c2 in ref:
            distR = abs(c2[0] - c[0])
            distG = abs(c2[1] - c[1])
            distB = abs(c2[2] - c[2])
            dist_list.append(distR + distG + distB)
        return dist_list.index(min(dist_list))

# ------------------------------------------------------------

    # note: def chunk and def get_palette_in_rgb found on stackoverflow, not my code
    def chunk(self, seq, size, group_by_list=True):
        func = tuple
        if group_by_list:
            func = list
        return [func(seq[i:i + size]) for i in range(0, len(seq), size)]

# ------------------------------------------------------------

    def get_palette_in_rgb(self, img):
        assert img.mode == 'P'
        pal = img.getpalette()
        colors = self.chunk(pal, 3, False)
        return colors

# ------------------------------------------------------------
