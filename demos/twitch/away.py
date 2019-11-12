from flore1 import *
import time

bm = [
    "fc:75"
    "          :::     :::       :::     :::   :::   :::",
    "       :+: :+:   :+:       :+:   :+: :+: :+:   :+:",
    "     +:+   +:+  +:+       +:+  +:+   +:+ +:+ +:+",
    "   +#++:++#++: +#+  +:+  +#+ +#++:++#++: +#++:",
    "  +#+     +#+ +#+ +#+#+ +#+ +#+     +#+  +#+",
    " #+#     #+#  #+#+# #+#+#  #+#     #+#  #+#",
    "###     ###   ###   ###   ###     ###  ###"
]

ta = TextAsset(bm)
sp = TextSprite(asset=ta)
scene = Scene(1, 1, 50, 22, 10)

scene.put(sp, 20, 6, 1)

print_crd("See you soon...", 30, 15)

scene.show()

time.sleep(25)
