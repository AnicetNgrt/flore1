import flore1

Engine = flore1.Engine(auto_scale=True, win_mode=False)
Refresh = flore1.Refresh(fps=60)

Scene = Engine.new_scene('main', res_x=100, res_y=100, coord_x=1, coord_y=1, layer_count=10)

explosion_sprt = Engine.new_sprite()
explosion_fb = flore1.Flipbook(Engine, Refresh, explosion_sprt, path='assets/explosion/', size=[100, 100], transparent_rgb=(0, 0, 0), fps=60, sync=True)
Scene.put(explosion_sprt, 1, 1, 3)
explosion_fb.start()

Refresh.feed(Scene.show,*(),**{})

while True:
    Refresh.run()