from flore1 import *
import time

bm = [
    "fc:160_________________________________________",
    "_________________________________________",
    "__fc:15ª8888888b.fc:160___fc:15ª8888888888fc:160__fc:15ª.d8888b.fc:160____",
    "__fc:15ª888fc:160___fc:15ªY88bfc:160_fc:15ª888fc:160________fc:15ªd88Pfc:160__fc:15ªY88bfc:160__",
    "__fc:15ª888fc:160____fc:15ª888fc:160_fc:15ª888fc:160________fc:15ª888fc:160____fc:15ª888fc:160__",
    "__fc:15ª888fc:160___fc:15ªd88Pfc:160_fc:15ª8888888fc:160____fc:15ª888fc:160__________",
    "__fc:15ª8888888P\"fc:160___fc:15ª888fc:160________fc:15ª888fc:160__________",
    "__fc:15ª888fc:160_fc:15ªT88bfc:160___fc:15ª888fc:160________fc:15ª888fc:160____fc:15ª888fc:160__",
    "__fc:15ª888fc:160__fc:15ªT88bfc:160__fc:15ª888fc:160________fc:15ªY88bfc:160__fc:15ªd88Pfc:160__",
    "__fc:15ª888fc:160___fc:15ªT88bfc:160_fc:15ª8888888888fc:160__fc:15ª\"Y8888P\"fc:160____",
    "_________________________________________",
    "_________________________________________"
]

ta = TextAsset(bm)
sp = TextSprite(asset=ta)
scene = Scene(1, 1, 50, 22, 10)

circle_bm = [
    "fc:160",
    "ªªªªªªªªªª_.:nnnnnn:._",
    "ªªªªªªª.o%%%%%%%%%%%%%%o.",
    "ªªªªª/n%%%%%%%%%%%%%%%%%%n\\",
    "ªªªª/%%%%%%%%%%%%%%%%%%%%%%\\",
    "ªªª,%%%%%%%%%%%%%%%%%%%%%%%%,",
    "ªªª|%%%%%%%%%%%%%%%%%%%%%%%%|",
    "ªªª'%%%%%%%%%%%%%%%%%%%%%%%%'",
    "ªªªª\\%%%%%%%%%%%%%%%%%%%%%%/",
    "ªªªªª\\u%%%%%%%%%%%%%%%%%%u/",
    "ªªªªªªª'o%%%%%%%%%%%%%%o'",
    "ªªªªªªªªªª\"°~uuuuuu~°\""
]

circle_ta = TextAsset(circle_bm)
circle_sp = TextSprite(asset=circle_ta)

scene.put(sp, 15, 3, 1)
scene.put(circle_sp, 60, 3, 2)

print_crd("Live starting soon...", 30, 20)

scene.show()

time.sleep(25)
