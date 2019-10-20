"""/////////////////////////
///
///   File: util.py
///   Author: Anicet Nougaret
///   QuickDesc: Some utilitary functions needed by the Engine
///   License: CC BY-SA (see FLORE1/license.txt)
///
/////////////////////////"""


def nearest_rgb_to_ansi(c, ref):
    dist_list = []
    c[0] -= 0
    c[1] += 30  # Just me tweaking rgb to get a little filter effect.
    c[2] += 15  # I'll put some conditions behind thoses tweaks later.
    for c2 in ref:
        distR = abs(c2[0] - c[0])
        distG = abs(c2[1] - c[1])
        distB = abs(c2[2] - c[2])
        dist_list.append(distR + distG + distB)
    return dist_list.index(min(dist_list))


# note: def chunk and def get_palette_in_rgb found on stackoverflow, not my code
def chunk(seq, size, group_by_list=True):
    func = tuple
    if group_by_list:
        func = list
    return [func(seq[i:i + size]) for i in range(0, len(seq), size)]


def get_palette_in_rgb(img):
    assert img.mode == 'P'
    pal = img.getpalette()
    colors = chunk(pal, 3, False)
    return colors
