import flore1

# You could totally have a JSON settings file for this
profile = {
    "start": ['p','enter'],
    "pause": ['m','space'],
    "up": ['up arrow','z'],
    "down": ['down arrow','s'],
    "left": ['left arrow','q'],
    "right": ['right arrow','d']
}

# Engine Initialisation
Input = flore1.InputHandler(keys = profile)
Graphics = flore1.Graphics(auto_scale=True, win_mode=False)
Scene = Graphics.new_scene('main', res_x=100, res_y=100, coord_x=1, coord_y=1, layer_count=10)
Refresh = flore1.Refresh(fps=60)

# Assets Initialisation
fb = {}
sprt = {}

sprt["explosion"] = Graphics.new_sprite()
Scene.put(sprt["explosion"], -10, -5, 0)
fb["explosion"] = flore1.Flipbook(Graphics, Refresh, sprt["explosion"], path='keyboard_demo_1_assets/explosion/', size=[100, 100], transparent_rgb=(0, 0, 0), fps=60, sync=True)
fb["explosion"].start()

sprt["flame"] = Graphics.new_sprite()
Scene.put(sprt["flame"], -10, -5, 1)
fb["flame"] = flore1.Flipbook(Graphics, Refresh, sprt["flame"], path='keyboard_demo_1_assets/blue flame/', size=[100, 100], transparent_rgb=(0, 0, 0), fps=60, sync=True)
fb["flame"].start()

# Game loop
def loop(Scene, Input, fb, sprt):
    speed = 3*(loop.i-loop.last_i)

    if Input.is_pressed("pause"):
        fb["explosion"].stop()
        fb["flame"].stop()
    if Input.is_pressed("start"):
        fb["explosion"].start()
        fb["flame"].start()

    x = sprt["flame"].x
    y = sprt["flame"].y

    if Input.is_pressed("up"):
        Scene.put(sprt["flame"], x, y-speed/2, 1)
    if Input.is_pressed("down"):
        Scene.put(sprt["flame"], x, y+speed/2, 1)
    if Input.is_pressed("left"):
        Scene.put(sprt["flame"], x-speed, y, 1)
    if Input.is_pressed("right"):
        Scene.put(sprt["flame"], x+speed, y, 1)

    Scene.show()

# Running the game
Refresh.feed(loop, *(Scene, Input, fb, sprt), **{})

while True:
    Refresh.run()
