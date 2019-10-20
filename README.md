 
# Flore 1 - pre alpha
 The first **python** 2D game engine **rendering in the terminal**.

# Table of content:

 1. [**Features**](#features)
 2. [**Roadmap**](#roadmap) 
 3. [**Compatibility**](#compat)
 4. [**Tutorials**](#tuto)
 5. [**Documentation**](#doc)
 6. [**License**](#license)

# <a name="features"></a>What can it do ?
#### For now, what it does the best is rendering:
 -   Interpret an easy syntax for creating text based sprites with color.
 -   Convert pictures to text based sprites.
 -   Manage picture's transparency.
 -   Create scenes with defined resolution, position and frame rate.
 -   Render sprites in a scene.
 -   Move sprites in a scene.
 -   Convert all the pictures in a directory to a flipbook.
 -   Display sprites with layers, transparency and depth management.
 -   Add custom functions to the game loop.
 -   Sync/unsync the looped functions with render speed (fps stabilisation).
 -  Play flibook in a scene at a desired frame rate. 

#  <a name="roadmap"></a>What is planned ?
 - Input management
 - Sound management
 - Remote SSH rendering
 - Basic server/client fonctionnalities


#  <a name="compat"></a>Known compatible terminals
 1. Windows 10 - Powershell
 2. Windows 10 - cmd
 3. Windows 10 - new GPU terminal
 4. Windows 10 - python terminal
 5. Linux - repl.it terminal emulator
 
 Note that it has great probability of rendering well on any modern shell which supports the following escapes codes:
 

    "\033[<row>;<col>H"
    "\33[0m"
    "\u001b[49;5;<color_code>m"
    "\u001b[39;5;<color_code>m"
    
  #  <a name="tuto"></a>Tutorials
  ### Table of content:
  

 0. [**Getting started**](#tuto0)
 1. [Displaying a static text sprite in a scene](#tuto1)
 2. [Introduction to game loops: Moving a sprite across it's scene](#tuto2)

## <a name="tuto0"></a>0/ Getting started:
### 💿 Installation with pip:
  If you don't have python (3.6 or above) and pip installed, install them first.
  
  Then, type this in your favorite terminal:
  `pip install flore1` or `python -m pip install flore1` 
  or `py -m pip install flore1 ` depending on your OS

### 📁 Project folder:
You want something like this:
```
📁 my_super_game/
|------🐍 main.py   just empty now  \(°o° /)  
|------📁 assets/   this folder will contain your assets eg: pictures
```
### 📖 minimal `main.py`
Now let's grab your favorite python IDE !
Edit `main.py` to look like this:
```python
import flore1 # we will need this to access the engine's classes
import time # will be useful at the end

# let's create our Engine instance !
Engine = flore1.Engine(
    auto_scale = True, # Wether the terminal should be rescaled
    win_mode = False # If you have display issues, you may want to set this to True
    )

```
This will be the very foundation for all the following tutorials !
## <a name="tuto1"></a>1/ Displaying a static text sprite:
### 🧭 What we will do:
![enter image description here](https://imgur.com/XVbCCmJ.png)
This tutorial is about displaying a text sprite in a scene with color and defined (x, y) position.
[-> I just want the code thanks.](#tuto1_code)

### 🎨 Creating a text sprite:
In order to create our text sprite we need to create a "building manual" for the sprite. Don't worry it is just an array of strings.
```python
# just following the previously given code:
building_manual = [
	"MY SUPER TEXT SPRITE LOOKS DAMN COOL",
	"Don't you agree ?",
	"Now I will do an ASCII army of squids just for the sake of it:",
	"(S 0-o0)S  (S 0-o0)S  (S 0-o0)S  (S 0-o0)S  (S 0-o0)S  (S 0-o0)S"
]
super_asset = Engine.TextAsset(building_manual)
 # This is our "Text Asset". Every time we will want to create a sprite
 # with this same building manual, we will create it from this Text Asset
```
Then you create a sprite from your asset (think of the Text Asset as a building manual).
```python
super_sprite = super_asset.to_sprite()
# That's that simple
```
Done, now let's display it in our previously created scene !

### 🎥 Displaying a sprite:
In order to display our sprite, we will need a Scene instance to put it in.
So let's create it too:
```python
# just following the previously given code:
Scene = Engine.new_scene("super cool name",
    res_x = 64, # don't mind thoses for now
    res_y = 32,
    coord_x = 10,
    coord_y = 5,
    layer_count = 15
    )
```
Now let's put the sprite in and refresh:
```python
# just following the previously given code:
# This puts the sprite in the scene
Scene.put(super_sprite, 10, 10, 1) #(sprite, x, y, layer)
# If you don't do this, the scene won't refresh
Scene.show() 
# if you don't want your terminal to close too fast...
time.sleep(15) 
```
Ok, good double click on `main.py`:
![enter image description here](https://imgur.com/vSMx3CP.png)As you can see, because our scene's `coord_x`  and `coord_y` were not 0 and 0, and because we displayed our sprite at (10;10), the text isn't stuck to the left border !
### 👩‍🎨Colored Text Sprites:
Wait, color on a terminal ? You are not dreaming... unless your terminal emulator is 20 years old. (you'll see)
In order to have color you must edit your building manual by putting specific codes in it:

 - `"bc:<code>"` This puts background color on any text following it
 - `"fc:<code>"` This changes font color on any text following it
 - `"cc:0"` This stops both background color and font color *(due to limitation you can't seem to stop only one)*

And if you want to know which `<code>` gives which color, here you go:
![terminal colors](http://www.lihaoyi.com/post/Ansi/Rainbow256.png)*picture credit: http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html*

Ok, now that you know this, let's tweak our asset's building manual with codes:
```python
building_manual = [
	"bc:195fc:127MY SUPER TEXT SPRITE LOOKS DAMN COOLcc:0",
	"Don't you agree ?",
	"Now I will do an ASCII army of squids just for the sake of it:",
	"fc:200(S 0-o0)S  (S 0-o0)S  (S 0-o0)S  (S 0-o0)S  (S 0-o0)S  (S 0-o0)Scc:0"
]
```
Let's look at it:
![enter image description here](https://imgur.com/XVbCCmJ.png)That's awesome isn't it ? And it is definitely easier than escape codes.

### <a name="tuto1_code"></a>📥 Conclusion: This tutorial's code:
```python
import flore1
import time

Engine = flore1.Engine(
    auto_scale = True, # Wether the terminal should be rescaled
    win_mode = False # If you have display issues, you may want to set this to True
    )

building_manual = [
	"bc:195fc:127MY SUPER TEXT SPRITE LOOKS DAMN COOLcc:0",
	"Don't you agree ?",
	"Now I will do an ASCII army of squids just for the sake of it:",
	"fc:200(S 0-o0)S  (S 0-o0)S  (S 0-o0)S  (S 0-o0)S  (S 0-o0)S  (S 0-o0)Scc:0"
]
super_asset = Engine.TextAsset(building_manual)
super_sprite = super_asset.to_sprite()

Scene = Engine.new_scene("super cool name",
    res_x = 64,
    res_y = 32,
    coord_x = 10,
    coord_y = 5,
    layer_count = 15
    )

Scene.put(super_sprite, 10, 10, 1)
Scene.show()

time.sleep(15)
```
## <a name="tuto2"></a>2/ Refresh class and sprite movement:
### 🧭 What we will do:
![fastboi](https://imgur.com/BRbsNUR.gif)
This tutorial is about moving a sprite across the scene.
[-> I just want the code thanks.](#tuto2_code)
### 🚠Introduction:
-So how does moving work in your mind ? 
-We can put sprites at some coordinates and refresh the scene. So why not doing this in a loop ?
-**Correct !** 

With flore1 there is a very elegant way of doing that thanks to the `flore1.Refresh` class. Let me show you:

#### The code you will start with:
```python
import flore1

Engine = flore1.Engine(auto_scale = True, win_mode = False)

building_manual = [
	"fc:200(S 0-o0)S  (S 0-o0)S  (S 0-o0)S  (S 0-o0)S  (S 0-o0)S  (S 0-o0)Scc:0"
]
super_asset = Engine.TextAsset(building_manual)
super_sprite = super_asset.to_sprite()

Scene = Engine.new_scene("super cool name",
    res_x = 64,
    res_y = 32,
    coord_x = 10,
    coord_y = 5,
    layer_count = 15
    )
```
### ➰ Creating our game loop:
Every game is a loop. That's not a philosophical point here, just a truth. If you want a game you want a loop. And looping in python is easy, you have `for` loops and `while` loops.
Here we just want to move only one sprite, so what we are going to do may seem overkill to you, but believe me, it is necessary that you do it once.

First we will need to create our `game_loop` function:
```python
# just following the previously given code:
# THE FIRST ARGUMENT MUST ALWAYS BE "Refresh"
# but whatever you put afterwards is up to you
# be careful, that's an easy mistake
def game_loop(Refresh, Scene, super_sprite):
	# every time game_loop.i is incremented, the sprite will
	# be displayed one row below itself
	Scene.put(super_sprite, 10, -10 + game_loop.i, 1)
	# don't forget, if you don't Scene.show() you don't see.a_difference()
	Scene.show()
```
In python, functions are objects. So they do have attributes.
As you can see, we are using `game_loop.i` in our function but we never declared it. 
Don't worry, this `<whatever the name of your function is>.i` will be always there thanks to the Refresh class. This attribute can sync with the engine's rendering speed in order to increment faster (or slow down) if the game runs too slow (or too fast).
Ok, but where is Refresh, and what is meant to be "too slow" ?:
### 📺 Initiating and feeding the Refresh:
```python
# just following the previously given code:
Refresh = flore1.Refresh(fps = 24)
```
So what we did here is that we created our Refresh instance, and asked it to run at 24 frames per second. Which means that our `game_loop.i` will try to sync with the Refresh in order to be incremented 24 times per second. If you decide to display so many sprites that the Refresh slows down to 12 frames per second, then `game_loop.i` will increment by 2 on every frame, in order to keep up with it's 24 fps objective. 
What I mean by that is that your sprite will always move at the same speed regardless of the lag (in theory).
```python
# just following the previously given code:
loop_tuple = (game_loop, Scene, super_sprite)
Refresh.feed(*loop_tuple) # don't forget the *
```
Here we formed a tuple composed with the function `game_loop` itself, and all the variables we want to give as inputs for its arguments. 
You will notice that we didn't put the Refresh in the tuple. In fact, Refresh is always a mendatory argument for the functions you feed your Refresh with, so you don't have to give it. In the tuple you only give the inputs to the arguments that come after the Refresh.
### 😵 While I loop the loop:
Now you have a super cool refresh, which task is to run `game_loop(Refresh, Scene, super_sprite)` at 24 fps.
But you still need to run it ! And this can't loop itself sadly...
```python
# just following the previously given code:
while True:
    Refresh.run()
```
Every time you call Refresh.run(), well, it does what you asked him to do... at the best of its abilities.
![fastboi](https://imgur.com/BRbsNUR.gif)Wow, do you see this ? A purple ASCII army of squids crossing the screen at a rocking 24 fps ! 
This is purely amazing !

*This gif looks like it is 10 fps but that's only because of my crappy gif recorder ... \( ; - ;  \ )*

### <a name="tuto2_code"></a>📥 Conclusion: This tutorial's code:
```python
import flore1

Engine = flore1.Engine(
    auto_scale = True, # Wether the terminal should be rescaled
    win_mode = False # If you have display issues, you may want to set this to True
    )

building_manual = [
	"bc:195fc:127MY SUPER TEXT SPRITE LOOKS DAMN COOLcc:0",
	"Don't you agree ?",
	"Now I will do an ASCII army of squids just for the sake of it:",
	"fc:200(S 0-o0)S  (S 0-o0)S  (S 0-o0)S  (S 0-o0)S  (S 0-o0)S  (S 0-o0)Scc:0"
]
super_asset = Engine.TextAsset(building_manual)
super_sprite = super_asset.to_sprite()

Scene = Engine.new_scene("super cool name",
    res_x = 64,
    res_y = 32,
    coord_x = 10,
    coord_y = 5,
    layer_count = 15
    )


def game_loop(Refresh, Scene, super_sprite):
    if game_loop.i <= 50:
        Scene.put(super_sprite, 10, -10 + game_loop.i, 1)
    Scene.show()

loop_tuple = (game_loop, Scene, super_sprite)
Refresh = flore1.Refresh(fps = 24)
Refresh.feed(*loop_tuple)

while True:
    Refresh.run()
```
  
 #  <a name="doc"></a>Documentation
 The flore1 module has 3 top level classes located in `flore1/flore1.py`:
 

 - [Engine](#engine_doc)
 - [Refresh](#refresh_doc)
 - [Flipbook](#anim_doc)

 ## <a name="engine_doc"></a>Engine class:
##### >>>> 🚧  work in progress
 
 
# <a name="license"></a>License
This library is distributed under a CC-BY-SA license.
Any kind of collaboration on this project is welcomed !  **(●^◡ ^● )**

