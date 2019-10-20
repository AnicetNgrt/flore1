import flore1

Engine = flore1.Engine(auto_scale=True, win_mode=False)
Refresh = flore1.Refresh(fps=24)

Scene = Engine.new_scene('main', res_x=150, res_y=85, coord_x=10, coord_y=10, layer_count=10)

username_manual = [
    'bc:0',
    '  fc:15 88   88    dP 88b 88  dP"Yb   dP"Yb  8888b.  88     888888 .dP"Y8 888888 888888    db    88  dP',
    '  fc:15 88   88   dP  88Yb88 dP   Yb dP   Yb  8I  Yb 88     88__   `Ybo."   88   88__     dPYb   88odP ',
    '  fc:15 Y8   8P  dP   88 Y88 Yb   dP Yb   dP  8I  dY 88  .o 88""   o.`Y8b   88   88""    dP__Yb  88"Yb ',
    '  fc:15 `YbodP\' dP    88  Y8  YbodP   YbodP  8888Y"  88ood8 888888 8bodP\'   88   888888 dP""""Yb 88  Yb'
]
username_asset = Engine.TextAsset(username_manual)
user_sprt = username_asset.to_sprite()
Scene.put(user_sprt, 1, 65, 4)

credit_asset = Engine.pic_to_textAsset('assets/credit/w pandelis.png', new_size=[128, 32], transparent_rgb=(41, 57, 65))
credit_sprt = credit_asset.to_sprite()
Scene.put(credit_sprt, 1, -260, 5)

fb_sprt = Engine.new_sprite()
flipbook = flore1.Flipbook(Engine, Refresh, fb_sprt, 'assets/wiz/', size=[128, 64], transparent_rgb=(-1, -1, -1), fps=16, sync=False)
Scene.put(fb_sprt, 1, 1, 2)
flipbook.start()

fb_sprt_2 = Engine.new_sprite()
flipbook2 = flore1.Flipbook(Engine, Refresh, fb_sprt_2, 'assets/floppy_disk/', size=[60, 60], transparent_rgb=(103, 103, 103), fps=16, sync=True)
Scene.put(fb_sprt_2, 50, 10, 3)
flipbook2.start()


def loop(Refresh, Scene):
    if loop.i <= 320:
        Scene.put(credit_sprt, 1, -260 + loop.i, 5)
    else:
        Scene.put(fb_sprt_2, 50 + round((loop.i - 320) * 0.5), 10, 3)
    Scene.show(debug=True)


my_loop = (loop, Scene)
Refresh.feed(*my_loop)

while True:
    Refresh.run(debug=True)
