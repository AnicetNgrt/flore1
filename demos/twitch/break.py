from flore1 import *
import time

bm = [
    "fc:160",
    "@@@@@@@   @@@@@@@   @@@@@@@@   @@@@@@   @@@  @@@",
    "@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@",
    "@@!  @@@  @@!  @@@  @@!       @@!  @@@  @@!  !@@",
    "!@   @!@  !@!  @!@  !@!       !@!  @!@  !@!  @!!",
    "@!@!@!@   @!@!!@!   @!!!:!    @!@!@!@!  @!@@!@! ",
    "!!:  !!!  !!: :!!   !!:       !!:  !!!  !!: :!! ",
    ":!:  !:!  :!:  !:!  :!:       :!:  !:!  :!:  !:!",
    " :: ::::  ::   :::   :: ::::  ::   :::   ::  :::",
    ":: : ::    :   : :  : :: ::    :   : :   :   :::"
]

ta = TextAsset(bm)
sp = TextSprite(asset=ta)
scene = Scene(1, 1, 50, 22, 10)
scene.put(sp, 24, 2, 1)

bm2 = [
"fc:214",
"        _       _    _                        ",
"   ___ |_| ___ | |_ | |_    ___  ___  _ _ _   ",
"  |  _|| || . ||   ||  _|  |   || . || | | |  ",
"  |_|  |_||_  ||_|_||_|    |_|_||___||_____|  ",
"          |___|                               cc:0"
]
ta2 = TextAsset(bm2)
sp2 = TextSprite(asset=ta2)
scene.put(sp2, 24, 12, 1)

print_crd("Coming back soon...", 30, 20)

scene.show()

time.sleep(25)
