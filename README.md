 
# 🌸 Flore 1 
 This is the first **python** 2D game engine **rendering in the terminal**.
 This library features the engine class itself, along with some utilitary classes for a more efficient use of it.

- **[Quick start](#tuto0)**
- **[Support Discord server](https://discord.gg/7GE5Zfy)**

**Note**: Thanks a lot for paying attention to my work. 
My name is Anicet Nougaret, I am a french IT student, and I am doing all of this alone. This project will always remain open source and free.
Therefore, please consider donating, it will greatly support this project ! 
\\(●\^◡\^●)/
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg) ](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=56G94VB5RYGKN&source=url) 

# Table of contents:

 1. [**Features**](#features)
 2. [**Roadmap**](#roadmap) 
 3. [**Compatibility**](#compat)
 4. [**Tutorials**](#tuto)
 5. [**Documentation**](#doc)
 6. [**License**](#license)

# <a name="features"></a>What can it do ?
*The best thing to do would be to take a look at the [tutorials](#tuto), they tend to cover everything the latest build can do.*
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
- `Gradually` Documentation and tutorials
- `Gradually` Quality of life improvements
- `Gradually` Optimization
- `High priority` Input management
- `High priority` UI helper classes
- `Medium priority` Basic server/client fonctionnalities 
- `Low priority` Sound management  
- `Low priority` Remote SSH rendering  


#  <a name="compat"></a>Known compatible terminals
**According to the latest tests**:
1. `good perf.` `good rendering` `Windows 10` `CPU`- **cmd.exe**
2. `good perf.` `good rendering` `Windows 10` `CPU`- **Powershell**
3. `good perf.` `bad rendering` `Windows 10` `GPU`- **new terminal**
4. `bad perf.` `good rendering` `Linux` `CPU`- **repl.it terminal emulator**
 
**Notes**: 
- It has great probability of rendering well on any modern terminal which supports the following escapes codes:
```python
"\033[<row>;<col>H"
"\33[0m"
"\u001b[49;5;<color_code>m"
"\u001b[39;5;<color_code>m"
```
- Terminals that do not support thoses will never be compatibles. 
- flore1 may use python `curses` in future updates which is not compatible with all terminals (it will still be compatible with windows). 
    
# <a name="tuto"></a>Tutorials
Theses aim to be a fun and beginner-friendly way of learning how to use flore1.  
### Table of content:
 0. [Getting started](#tuto0)
 1. [Displaying a static text sprite in a scene](#tuto1)
 2. [Introduction to game loops: Moving a sprite across its scene](#tuto2)
 3. [Converting a picture to a sprite and displaying it](#tuto3)
 4. [Flipbooks: Display a gif on the terminal as an animated text sprite](#tuto4)
 
## <a name="tuto0"></a>0/ Getting started:
### 💿 Installation with pip:
  If you don't have python (3.7 or above) and pip installed, install them first.
  
  **Then, type one of thoses in your favorite terminal**:
  - *universal, may not work:* `pip install flore1`  
  - *unix based OS:* `python -m pip install flore1` 
  - *windows:* `py -m pip install flore1 `

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
    auto_scale = True, # Whether the terminal should be rescaled
    win_mode = False # If you have display issues, you may want to set this to True
    )

```
This will be the very foundation for the following tutorials.
## <a name="tuto1"></a>1/ Displaying a static text sprite:
### 🧭 What we will do:
![enter image description here](https://imgur.com/XVbCCmJ.png)
This tutorial is about displaying a text sprite in a scene with colors and defined (x, y) position.
[-> I just want the code thanks.](#tuto1_code)

### 🎨 Creating a text sprite:
First, you need the basic code I gave [here](#tuto0).

In order to create our text sprite we need to create a "building manual" for the sprite. Don't worry it is just an array of strings.
```python
# following the previously given code:
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
Then you create a sprite from your asset (think of the Text Asset as a building manual).:
```python
super_sprite = super_asset.to_sprite()
# That's that simple
```
Done, now let's display it in a scene !

### 🎥 Displaying a sprite:
In order to display our sprite, we will need a Scene instance to put it in.
So let's create it too:
```python
# following the previously given code:
Scene = Engine.new_scene("super cool name",
    res_x = 64, # don't mind thoses for now
    res_y = 32,
    coord_x = 10,
    coord_y = 5,
    layer_count = 15 #scene's width
    res_y = 32, # scene's height
    coord_x = 10, # scene's distance to left border
    coord_y = 5, # scene's distance to top border
    layer_count = 15 # a layer is where your sprite goes: 1 sprite displayed = 1 layer
    )
```
Now let's put the sprite in the scene and refresh:
```python
# following the previously given code:
# This puts the sprite in the scene
Scene.put(super_sprite, 10, 10, 1) #(sprite, x, y, layer)
# If you don't do this, the scene won't refresh
Scene.show() 
# if you don't want your terminal to close too fast...
time.sleep(15) 
```
Ok, good double click on `main.py`:
![enter image description here](https://imgur.com/vSMx3CP.png)As you can see, because our scene's `coord_x`  and `coord_y` were not 0 and 0, and because we displayed our sprite at (10;10), the text isn't stuck to the left and top border !
### 👩‍🎨Colored Text Sprites:
Wait, color on a terminal ? You are not dreaming... unless your terminal emulator is 20 years old. (you'll see)
In order to have color you must edit your building manual by putting specific codes in it:

 - `"bc:<code>"` This puts background color on any text following it
 - `"fc:<code>"` This changes font color on any text following it
 - `"cc:0"` This stops both background color and font color *(due to limitation you do not seem to be able to stop only one)*

And if you want to know which `<code>` gives you which color, here you go:
![terminal colors](http://www.lihaoyi.com/post/Ansi/Rainbow256.png)*picture credit: http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html*

Ok, now that you know this, let's tweak our asset's by adding codes inside our building manual:
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
## <a name="tuto2"></a>2/ Introduction to game loops: Moving a sprite across its scene:
### 🧭 What we will do:
![fastboi](https://imgur.com/BRbsNUR.gif)
This tutorial is about moving a sprite across the scene.
[-> I just want the code thanks.](#tuto2_code)
### 🚠Introduction:
-So how does moving works in your mind ? 

-We can put sprites at some coordinates and refresh the scene. So why not doing this in a loop ?

-**That's correct !** 

With flore1 there is a very efficient way of doing that thanks to the `flore1.Refresh` class. Let me show you:

#### The code you will start with:
```python
import flore1

Engine = flore1.Engine(auto_scale = True, win_mode = False)

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
```
### ➰ Creating our game loop:
Every game is a loop. That's not a philosophical point here, just a truth. If you want a game you want a loop. And looping in python is easy, you have `for` loops and `while` loops.
Here we just want to move only one sprite, so what we are going to do may seem overkill to you, but believe me, it is necessary that you do it once.

First we will need to create our `game_loop` function:
```python
# following the previously given code:
def game_loop(Scene, super_sprite):
	# every time game_loop.i is incremented, the sprite will
	# be displayed one row below itself
	Scene.put(super_sprite, 10, -10 + game_loop.i, 1)
	# don't forget, if you don't Scene.show() you don't see.a_difference()
	Scene.show()
```
In python, functions are objects. So they do have attributes.
As you can see, we are using `game_loop.i` in our function but we never declared it nor did we initialized it. 
Don't worry, this `<whatever the name of your function is>.i` attribute will be always be there thanks to the Refresh class. This attribute can sync with the engine's rendering speed in order to increment faster (or slow down) if the game runs too slow (or too fast).
Ok, but where is Refresh, and what is meant to be "too slow" ?:
### 📺 Initiating and feeding the Refresh:
```python
# following the previously given code:
Refresh = flore1.Refresh(fps = 24)
```
So what we did here is that we created our Refresh instance, and asked it to run at 24 frames per second. Which means that our `game_loop.i` will try to sync with the Refresh in order to be incremented 24 times per second. If you decide to display so many sprites that the Refresh slows down to 12 frames per second, then `game_loop.i` will be incremented by 2 on every frame, in order to keep up with it's 24 fps objective. 
What I mean by that is that your sprite will always move at the same speed regardless of the lag (in theory).
```python
# following the previously given code:
loop_tuple = (game_loop, Scene, super_sprite)
Refresh.feed(*loop_tuple) # don't forget the *
```
Here we formed a tuple composed with the function `game_loop` itself, and all the variables we want to give as input for its keyword arguments.

**Note**: If your `game_loop` function has default arguments, I advice you see tutorial 4 for a more in depth explanation of the `Refresh.feed` method's syntax.
### 😵 While I loop the loop:
Now you have a super cool refresh, which task is to run `game_loop(Scene, super_sprite)` at 24 fps.
But you still need to run it ! And this can't loop itself sadly...
```python
# following the previously given code:
while True:
    Refresh.run()
```
Every time you call Refresh.run(), well, it does what you asked him to do... at the best of its abilities.
![fastboi](https://imgur.com/BRbsNUR.gif)Wow, do you see this ? A purple ASCII army of squids crossing the screen at a rocking 24 fps ! 
This is purely amazing !

*This gif looks like it is 10 fps but that's only because of my crappy gif recorder ... 
\\( ; - ;  \ )*

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


def game_loop(Scene, super_sprite):
    if game_loop.i <= 50:
        Scene.put(super_sprite, 10, -10 + game_loop.i, 1)
    Scene.show()

loop_tuple = (game_loop, Scene, super_sprite)
Refresh = flore1.Refresh(fps = 24)
Refresh.feed(*loop_tuple)

while True:
    Refresh.run()
```
## <a name="tuto3"></a>3/ Converting a picture with transparency to a sprite and displaying it:
### 🧭 What we will do:
![wow](https://imgur.com/X3xpstQ.png)This tutorial is about displaying pictures on top of one another with transparency, after having them converted to (text) sprites.
[-> I just want the code thanks.](#tuto3_code)
### 📁 Let's get pictures !
For this tutorial we need pictures so make sure you have the following:
```
📁 my_super_game/
|-----🐍 main.py     
|-----📁 assets/
|-----|-----📸 anicet.jpg   -> https://imgur.com/4dFlgUF
|-----|-----🎨 archer.png   -> https://imgur.com/BX2i3j5
|-----|-----🎨 aniss.png    -> https://imgur.com/AYA6Ruc
```
Here also should be your `main.py` right now:
```python
import flore1
import time

Engine = flore1.Engine(
    auto_scale = True, # Wether the terminal should be rescaled
    win_mode = False # If you have display issues, you may want to set this to True
    )

Scene = Engine.new_scene("super cool name",
    res_x = 128, # For this one we need a bigger scene
    res_y = 128,
    coord_x = 1,
    coord_y = 1,
    layer_count = 15
    )
```
**Very important:** Most terminal have large font size by default. It will be necessary to lower this size in your terminal's settings in order to display bigger than 100*100px pictures. Mine is at 6 now for instance.
### 🧾 From pictures to text and... no vice-versa 
The Engine class can convert `.png`, `.jpg` and `.svg` pictures to text Assets with the help of `pillow`, a very known python image manipulation library.
But here comes the issue: **size**. Because even if you ask your terminal to go 14px font style, it won't be easy to display anything bigger than 300*300px. This is more of a pixelart engine than a fancy graphical library. But come on, it's on the terminal :D !
Ok let's try to display `anicet.jpg` (resized of course) in the terminal:
```python
# following the previously given code:
anicet_asset = Engine.pic_to_textAsset(
    path='assets/anicet.jpg', 
	new_size="AUTO", #or: [width,height]
	)
```
This will convert the picture. Note that you can tell it to resize automatically to the maximum reasonnable size, or just tell it which size you want. Also the engine supports transparent pictures, assuming you tell it which color is meant to be transparent.
Ok, now let's create the asset, put it in the scene, and display it. Just as usual:
```python
# following the previously given code:
anicet_sprite = anicet_asset.to_sprite()
Scene.put(anicet_sprite, 10, 10, 1)
Scene.show()
time.sleep(30)
```
![me but pixelated](https://imgur.com/PNXPVtc.png)
Hey, that's me ! *(I feel like I will hate myself for taking this picture in a few years)*
As you can see, the originaly 1024*1024px picture got quite resized ! Note that detailed pictures almost never downscale without ugly artifacts everywhere. This is due to the limited n=255 terminal's color range... so we have no other choices. ¯\\\_(ツ)_/¯
### 📚 Displaying more pictures
Now let's repeat the process in order to display more pictures.
Don't forget to erase the `time.sleep(30)` you put previously, unless you like waiting a lot.
#### a. Let's display a picture with transparency:
```python
# following the previously given code
bow_icon_asset = Engine.pic_to_textAsset(
    path='assets/archer.png', 
	new_size=["32","32"], # we ask it to resize this picture to 32*32px
	transparent_rgb=(238, 195, 154) # The color in the picture that is meant to be transparent
	)
bow_icon_sprite = bow_icon_asset.to_sprite()
Scene.put(bow_icon_sprite, 10, 60, 2) # 2 => layer
```
By puting `(238, 195, 154)` in the `transparent_rgb` optionnal argument, we ask the scene not to print this picture's pixels having this rgb code.
#### b. Let's display a picture without transparency:
```python
# following the previously given code
avatar_asset = Engine.pic_to_textAsset(
    path='assets/aniss.png', 
	new_size=["50","50"] # resize to 50*50px
	# here we do not put anything, this way the scene
	# knows there is no transparency for this picture
	)
avatar_sprite = avatar_asset.to_sprite()
Scene.put(avatar_sprite, 60, 20, 3) # 3 => layer

# Don't forget this:
Scene.show()
time.sleep(30)
```
As you can see we asked our scene to put our 2nd sprite on the 2nd layer and the 3rd one on the 3rd layer. Therefore, the 1st picture on the 1st layer will be on the foreground, and the two others will be more or less on the top according to their layer.

![wow](https://imgur.com/X3xpstQ.png)It works ! The bow icon has transparency, and the pictures do display on top of one another.  
Now you know how to display pictures with flore1 !
### <a name="tuto3_code"></a>📥 Conclusion: This tutorial's code:
```
📁 my_super_game/
|-----🐍 main.py     
|-----📁 assets/
|-----|-----📸 anicet.jpg   -> https://imgur.com/4dFlgUF
|-----|-----🎨 archer.png   -> https://imgur.com/BX2i3j5
|-----|-----🎨 aniss.png    -> https://imgur.com/AYA6Ruc
```
```python
# main.py

import flore1
import time

Engine = flore1.Engine(
    auto_scale = True, # Wether the terminal should be rescaled
    win_mode = False # If you have display issues, you may want to set this to True
    )

Scene = Engine.new_scene("super cool name",
    res_x = 128,
    res_y = 128,
    coord_x = 1,
    coord_y = 1,
    layer_count = 15
    )

anicet_asset = Engine.pic_to_textAsset(path='assets/anicet.jpg', new_size="AUTO")
anicet_sprite = anicet_asset.to_sprite()
Scene.put(anicet_sprite, 10, 10, 1)

bow_icon_asset = Engine.pic_to_textAsset(path='assets/archer.png', new_size=["32","32"], transparent_rgb=(238, 195, 154))
bow_icon_sprite = bow_icon_asset.to_sprite()
Scene.put(bow_icon_sprite, 10, 60, 2)

avatar_asset = Engine.pic_to_textAsset(path='assets/aniss.png', new_size=["50","50"])
avatar_sprite = avatar_asset.to_sprite()
Scene.put(avatar_sprite, 60, 20, 3)

Scene.show()

time.sleep(30)
```
## <a name="tuto4"></a> Flipbooks: Display a gif on the terminal as an animated text sprite
***Disclaimer: featuring free to use assets by [Will Tice](#https://www.patreon.com/bePatron?c=165655&rid=201537)***
### 🧭 What we will do:

![60fps flavour](https://imgur.com/Xo6XNs1.gif)
In this tutorial we will display an animated GIF in the terminal with transparency.
[-> I just want the code thanks.](#tuto4_code)
### 🎬 Finding and making a GIF compatible with flore1:
First we need to find a suitable low-res `.gif` (you can also put large sized GIF since the engine can rescale pictures, but in this tutorial we won't do it).
Personnaly, I'm not a pro pixel art animator so I took my GIF [here](#https://untiedgames.itch.io/five-free-pixel-explosions).


![explosion](https://imgur.com/8kXy0FB.gif)
#### You need to convert your GIF to a folder containing it's frames as PNG files
Note that the original source I gave lets you download a folder containing all individuals frames as png. Which is exactly what the engine needs. But I case you only have a `.gif` file, such as the one above go to [this online tool](https://ezgif.com/split), import your gif, download the `.zip` containing the frames, and extract it in a folder in your project.
#### This tutorial's folder:
```
📁 my_super_game/
|-----🐍 main.py     
|-----📁 assets/
|-----|-----📁 explosion/
|-----|-----|-----📼 frame0000.png
|-----|-----|-----📼 frame0001.png
                   :
|-----|-----|-----📼 frame0063.png
```
**Note**: You need your frames to be ranked in lexicographic order accordingly to their order of appearance in your original GIF.
#### The `main.py` we will start with:
```python
import flore1

Engine = flore1.Engine(
	auto_scale=True, 
	win_mode=False
	)
	
Scene = Engine.new_scene('main', 
	res_x=100, # we need a large scene
	res_y=100, # for our 100*100px gif
	coord_x=1, 
	coord_y=1, 
	layer_count=15
	)
```
### 📘 Creating a Flipbook 

In order to create a flipbook, you first need to create an empty sprite for your flipbook:
```python
# following the previously given code:
explosion_sprt = Engine.new_sprite() 
```
But you also need to create a Refresh which will run our animation:
```python
# following the previously given code:
Refresh = flore1.Refresh(fps=60)
```
Now let's create our flipbook, it requires many parameters, I advice you read my comments on all of them:
```python
# following the previously given code:
explosion_fb = flore1.Flipbook(
	Engine, # our engine instance
	Refresh, # the refresh instance that will run the sprite
	explosion_sprt, # the empty sprite that will be animated by our flipbook
	path='assets/explosion/', # the path to the folder containing our frames 
	size=[100, 100], # the (new)size of our frames
	transparent_rgb=(0, 0, 0), # the transparent color for our frames
	fps=60, # the frame rate of our animation 
	sync=True # whether it has to skip frames if the refresh slows down
	)
```
**Note**: If the frame rate of your refresh is slower than the frame rate of your flipbook, your flipbook may skip frames.  

Now we can start our Flipbook:
```python
# following the previously given code
explosion_fb.start()
```
We will also need to run our refresh in a while loop, as we did previously for sprite movement. But before doing that, we need to ask our refresh to `Scene.show()` at every iteration, otherwise the sprite would update but not the display, and we wouldn't see any difference.
Do you remember when we built a loop function that we fed our refresh with ? Here we don't need to create such function because our `Scene.show()` method already refers to a function. We are just going to feed our refresh with our `Scene.show()` method:
```python
# following the previously given code
Refresh.feed(Scene.show,*(),**{})
```
Here, we are feeding it a bit differently than on tutorial 2, so let me explain how it works:
#### `Refresh.feed`'s syntax:
The first argument must be a function or a method (ex: `my_function`, or `Object.method`), the second argument must be a tuple of keyword arguments for the function (ex: `(x,y,0,18,"ok")`), and the third one must be a dictionnary of default arguments for the function (ex: `{"name"="Anicet","favorite_color"="yellow"}`).
Dont forget to put `*` before your tuple and `**` before your dictionnary.

#### Now let's loop our `Refresh.run()` as we did in tutorial 2:
```python
# following the previously given code
while True:
    Refresh.run()
```
Done, now run it and admire:

![Done, now run it and admire.](https://imgur.com/Xo6XNs1.gif)*true speed on my system, you may get a worse frame rate*
### <a name="tuto4_code"></a>📥 Conclusion: This tutorial's code:
In order to get the frames, I advice you read at least the very beginning of this tutorial.
```
📁 my_super_game/
|-----🐍 main.py     
|-----📁 assets/
|-----|-----📁 explosion/
|-----|-----|-----📼 frame0000.png
|-----|-----|-----📼 frame0001.png
                   :
|-----|-----|-----📼 frame0063.png
```
```python
# main.py

import flore1

Engine = flore1.Engine(auto_scale=True, win_mode=False)
Scene = Engine.new_scene(
	'main', 
	res_x=100, 
	res_y=100, 
	coord_x=1, 
	coord_y=1, 
	layer_count=10
	)

Refresh = flore1.Refresh(fps=60)

explosion_sprt = Engine.new_sprite()
Scene.put(explosion_sprt, -10, -5, 3)
explosion_fb = flore1.Flipbook(
	Engine, 
	Refresh, 
	explosion_sprt, 
	path='assets/explosion/', 
	size=[100, 100], 
	transparent_rgb=(0, 0, 0), 
	fps=60, 
	sync=True
	)
explosion_fb.start()

Refresh.feed(Scene.show,*(),**{})

while True:
    Refresh.run()
```
#  <a name="doc"></a> Documentation
Here you will find detailed explanations for everything you may want to use from this library.

**Notes**: 

- Some methods and properties are not useful for using this library from the outside, that is why everything is not documented. If you want to get info on something not listed here head to our [discord server](https://discord.gg/7GE5Zfy).
- With most fonts, 1 char width = 1/2 char height, always keep this in mind. If the docs don't talk about a `width` parameter or a `x` parameter being "1/2 of its true value" or "multiplied by 2" it means your `width` or your `x` may be the half of what you expect.
- Never give the `self` argument when calling methods.
## <a name="classes"></a>Classes
 
 - [Flipbook](#flipbook) 
 - [Refresh](#refresh)
 - [Engine](#engine)
	 - [Engine.VirtualScene](#engine.virtualscene) *`Scenes`*
	 - [Engine.TextAsset](#engine.textasset) *`Assets`*
		 - [Engine.TextAsset.TextSprite](#engine.textasset.textsprite) *`Sprites`*
## <a name="flipbook"></a>📜 Flipbook [class](#classes)


The Flipbook class lets you easily animate [TextSprites](#textsprites) by computing their texture change rate, function of the Flipbook's [Refresh](#refresh) 's execution rate and the Flipbook frame rate goal. 
### <a name="flipbook-props"></a>Properties

 - [material](#flipbook.material)

### <a name="flipbook-methods"></a>Methods
- [\_\_init\_\_](#flipbook-init) 
- [start](#flipbook-start) 
- [stop](#flipbook-stop) 
---
### <a name="flipbook-init"></a>🧰 \_\_init\_\_ [method](#flipbook-methods)

##### - Description:
Inits the Flipbook: 
- Inits its [material](#flipbook.material) property
	- Creates the `play` function. See [material](#flipbook.material)  for more details.
-  **About picture conversion:**
	- Compatible with `.png`, `.jpg`, `.jpeg`, static `.gif`, and `.svg` pictures.
	- Putting a rgb code that is not part of your picture's color palette is the appropriate way of telling the engine that this picture has no transparency.
	- Putting the `"AUTO"` value in your `size` argument will resize the picture so it fits within 128x128px.

##### - Prototype:
```python
def __init__(self, Engine, Refresh, Sprite, path="", size=[32, 32], transparent_rgb=(-1, -1, -1), fps=24, sync=True)
```
##### - Return value:
No return value
##### - Arguments:
| [ in ] | type  | condition | description |
|--|--|--|--|
| Engine | [Engine](#engine) | None | Engine instance that computes for the creation of the flipbook from its set of pictures
| Refresh | [Refresh](#refresh) | None| Refresh instance that runs the flipbook 
| Sprite | [Sprite](#engine.textasset.textsprite) | None| TextSprite instance that has its texture animated by the flipbook 
| path | string | Path exists| Path to a folder containing all the frames for the animation in lexicographical order. **Relative to the .py file at the root of the call.**
| size | array of integers | [ a>0 , b>0 ] | [width, height] for the animated sprite 
| transparent_rgb | tuple of integers | None | RGB of the transparent color in the flipbook's frames 
| fps | integer | > 0 | Frame rate goal for the flipbook in frame per second
| sync | boolean | None | Whether the flipbook skips frame if the refresh slows down

---
### <a name="flipbook-start"></a>🧰 start [method](#flipbook-methods)
##### - Description:
Feeds the Flipbook's Refresh instance with the Flipbook's [material](#flipbook.material) property.
##### - Prototype:
```python
def start(self)
```
##### - Return value:
No return value
##### - Arguments:
None

---
### <a name="flipbook-stop"></a>🧰 stop [method](#flipbook-methods)
##### - Description:
Terminates the Flipbook's [material](#flipbook.material) property's function execution within the Flipbook's Refresh instance.
##### - Prototype:
```python
def stop(self)
```
##### - Return value:
No return value
##### - Arguments:
None

---
### <a name="flipbook.material"></a>📌 material [property](#flipbook-props) 
##### Description:
A tuple composed with `play`: a function which changes the Flipbook's sprite's texture function of the Flipbook's Refresh and the Flipbook's frame rate goal, and also composed with all of this function's arguments. Feeding a Refresh with `*(Flibook.material)` starts the Flipbook.


## <a name="refresh"></a>📜 Refresh [class](#classes)
You can "[feed](#refresh-feed)" the Refresh class with a `(function, *args, **kwars)` tuple. It will add it to it's [execution stack](#refresh.stack). Everytime you ask the Refresh to "[do](#refesh-do)" it will call all the `function(*args, **kwargs)` from its stack, compute execution time and wait if the execution time was too fast, or ask all the function that have their attribute `sync` set to `True` in its stack to "skip" frames if it was too slow. Therefore the Refresh class is there for frame stabilisation purposes and speed stabilisation purposes. For more details see the docs on its [methods](#refresh-methods).

**Note**: I only talk about functions in this class's doc. **Everything also works with `(method, *args, **kwargs)` tuples**.

### <a name="refresh-props"></a>Properties
- [fps](#refresh.fps)
- [stack](#refresh.stack)
- [frame](#refresh.frame)
- [i](#refresh.i)
### <a name="refresh-methods"></a>Methods
- [\_\_init\_\_](#refresh-init) 
- [terminate](#refresh-terminate) 
- [feed](#refresh-feed) 
- [do](#refresh-do) 
- [run](#refresh-run) 
- ---
### <a name="refresh-init"></a>🧰 \_\_init\_\_ [method](#refresh-methods)
##### - Description:
Inits all the [properties](#refresh-props) of the Refresh instance.
##### - Prototype:
```python
def __init__(self, fps=35)
```
##### - Return value:
No return value
##### - Arguments:
| [ in ] | type | condition | description
|--|--|--|--|
| fps | integer | > 0 | Execution rate goal of the Refresh 
---
### <a name="refresh-terminate"></a>🧰 terminate [method](#refresh-methods)
##### - Description:
Removes a specific `(function, *args, **kwargs)` tuple from the Refresh instance's execution [stack](#refresh.stack).
In other words, the Refresh instance stops calling `function(*args, **kwargs)` when it's [do](#refresh-do) method is called.
##### - Prototype:
```python
def terminate(self, func, *args, **kwargs)
```
##### - Return value:
No return value
##### - Arguments:
| [ in ] | type | description
|--|--|--|
| func | function | Function type element of the tuple to remove from the [stack](#refresh.stack)
| *args | *args | Arguments type element of the tuple to remove from the [stack](#refresh.stack) 
| **kwargs | **kwargs | Keyworded arguments type element of the tuple to remove from the [stack](#refresh.stack)

---
### <a name="refresh-feed"></a>🧰 feed [method](#refresh-methods)
##### - Description:
Adds a `(function, *args, **kwargs)` tuple to the Refresh instance's execution [stack](#refresh.stack). 
In other words, it asks the Refresh instance to call `function(*args, **kwargs)` via the [do](#refresh-do) method every time its [run](#refresh-run) method is called, to add its execution time to the total execution latency, and, only if `function.sync = True`, to sync its execution rate with the Refresh instance's execution latency goal.
##### - Prototype:
```python
def feed(self, function, *args, **kwargs)
```
##### - Return value:
No return value
##### - Arguments:
| [ in ] | type | description
|--|--|--|
| func | function | Function type element of the tuple to append the [stack](#refresh.stack) with
| *args | *args | Arguments type element of the tuple to append the [stack](#refresh.stack) with 
| **kwargs | **kwargs | Keyworded arguments type element of the tuple to append the [stack](#refresh.stack) with
---
### <a name="refresh-do"></a>🧰 do [method](#refresh-methods)
##### - Description:
For each `(function, *args, **kwargs)` tuple in the Refresh instance's [stack](#refresh.stack) it may call `function(*args, **kwargs)` (if `function.sync` is True, it only calls it on frame change). But before, if `function.i` does not exist it sets it to `0`, if `function.sync` does not exist, it sets it to `True`, and if `function.refresh` does not exist, it sets it to `self`.
##### - Prototype:
```python
def do(self)
```
##### - Return value:
No return value
##### - Arguments:
No arguments

---
### <a name="refresh-run"></a>🧰 run [method](#refresh-methods)
##### - Description:
Calls the [do](#refresh-do) method and computes its execution time (the latency caused by it). Then it computes the [Refresh.i](#refresh.i) property, function of the latency and the [Refresh.fps](#refresh.fps) property. The point is that this property always augments at the same speed regardless of the low or high latency. Then [Refresh.frame](#refresh.frame) is assigned the round value of [Refresh.i](#refresh.i).
##### - Prototype:
```python
def run(self, debug=False)
```
##### - Return value:
No return value
##### - Arguments:
| [ in ] | type | description
|--|--|--|
| self | [Refresh](#refresh) | The Refresh instance that you run
| debug | boolean | Whether you want the debug overlay for this method to show on the top left corner
---
### <a name="refresh.fps"></a>📌 fps [property](#refresh-props) 
##### Description: 
The frame rate goal of the Refresh instance. It is meant to be an integer.

---
### <a name="refresh.stack"></a>📌 stack [property](#refresh-props) 
##### Description: 
A list of `(function, *args, **kwargs)` tuple. It lists all the functions that can be called by the Refresh instance and all their arguments. This depends on whether the function's `.sync` attribute is set to `True` or `False`, and on whether [Refresh.frame](#refresh.frame) has changed.

---
### <a name="refresh.frame"></a>📌 frame [property](#refresh-props) 
##### Description: 
The current "frame" (or turn count) of the Refresh. It is equal to the rounded value of [Refresh.i](#refresh.i). When its value changes the synced functions in the [stack](#refresh.stack) get called and their `.i` attribute changes as much as the [Refresh.frame](#refresh.frame) did. 

**Note**: The unsynced functions in the [stack](#refresh.stack) are always called and their `.i` attribute is just incremented by 1 at each call.

---
### <a name="refresh.i"></a>📌 i [property](#refresh-props) 
##### Description: 
A float variable that accumulates the frame latency and the frame advance in order to count the [frame](#refresh.frame) count more accuratly.

---
## <a name="engine"></a>📜 Engine [class](#classes)
The Engine takes care of everything from rendering to input and sound, but its usage is a bit barebone from time to time. That's why it is not the only flore1 top level class. 
### Subclasses
-  [VirtualScene](#engine.virtualscene)
-  [TextAsset](#engine.textasset)
### <a name="engine-props"></a>Properties
-  [vscenes](#engine.vscenes)
-  [auto_scale](#engine.auto_scale)

### <a name="engine-methods"></a>Methods

- [\_\_init\_\_](#engine-init) 
- [new_scene](#engine-new_scene) 
- [del_scene](#engine-del_scene) 
- [new_sprite](#engine-new_sprite) 
- [pic_to_textAsset](#engine-pic_to_textasset) 
### <a name="engine-init"></a>🧰 \_\_init\_\_ [method](#engine-methods)
##### - Description:
- Inits the Engine instance:
	- Inits its [auto_scale](#engine.auto_scale) property
	- Inits its [vvscenes](#engine.vscenes) property
- Displays the flore1's logo if `logo == True`
##### - Prototype:
```python
def __init__(self, auto_scale=False, win_mode=False, logo=False)
```
##### - Return value:
No return value
##### - Arguments:
| [ in ] | type | description
|--|--|--|
| auto_scale | boolean | Whether the Engine should try to resize the terminal when a [Engine.VirtualScene](#engine.virtualscene) instance is created.
| win_mode | boolean | Whether to realize a compatibility manipulation which may fix rendering issue on some terminals.
| logo | boolean | Whether to display flore1's logo on start.
---
### <a name="engine-new_scene"></a>🧰 new_scene [method](#engine-methods)
##### - Description:
Creates an [Engine.VirtualScene](#engine.virtualscene) instance, puts it inside the Engine's [vscenes](#engine.vscenes) dictionnary at the `name` entry, and returns it.
##### - Prototype:
```python
def new_scene(self, name, coord_x, coord_y, res_x, res_y, layer_count)
```
##### - Return value:
[Engine.VirtualScene](#engine.virtualscene): The scene just created.
##### - Arguments:
| [ in ] | type | condition | description
|--|--|--|--|
| name | string | != "" | The key of the scene in the [Engine.vscenes](#engine.vscenes) dictionnary
| coord_x | integer | > 0 | The distance of the scene from the terminal's left border in chars
| coord_y | integer | > 0 | The distance of the scene frome the terminal's top border in chars  
| res_x | float | > 0 | 1/2 of the width of the scene in chars. (multiplied by 2 and then  rounded)
| res_y | integer | > 0 | The height of the scene in chars
| layer_count | integer | > 0 | The number of layers in the scene, in other words, how many level of superposition the scene tries to manage.
 
---
### <a name="engine-del_scene"></a>🧰 del_scene [method](#engine-methods)
##### - Description:
Deletes an entry in [Engine.vscenes](#engine.vscenes). **This will delete the [Engine.VirtualScene](#engine.virtualscene) instance itself.**
##### - Prototype:
```python
def del_scene(self, name)
```
##### - Return value:
No return value
##### - Arguments:
| [ in ] | type | condition | description
|--|--|--|--|
| name | string | != "" | The key of the entry to delete.
---
### <a name="engine-new_sprite"></a>🧰 new_sprite [method](#engine-methods)
##### - Description:
Creates and return an empty [Engine.TextAsset.TextSprite](#engine.textasset.textsprite) (sprite) instance. You can put it in a scene, but if you do not set its asset property before showing the scene, it may crash.
##### - Prototype:
```python
def new_sprite(self)
```
##### - Return value:
[Engine.TextAsset.TextSprite](#engine.textasset.textsprite) An empty sprite
##### - Arguments:
None

---

### <a name="engine-pic_to_textasset"></a>🧰 pic_to_textAsset [method](#engine-methods)
##### - Description:
Opens, rescale if needed, and gathers the color palette for a picture with the `Pillow` library, and then converts it to an array of strings called a "building manual". Then it calls [`Engine.TextAsset(building_manual)`](#Engine.TextAsset) and returns the Asset resulting from this.
- Compatible with `.png`, `.jpg`, `.jpeg`, static `.gif`, and `.svg` pictures.
- Putting a rgb code that is not part of your picture's color palette is the appropriate way of telling the engine that this picture has no transparency.
- Letting the `new_size` argument as `"AUTO"` will resize the picture so it fits within 128x128px.
##### - Prototype:
```python
def pic_to_textAsset(self, path="", new_size="AUTO", transparent_rgb=(-1, -1, -1))
```
##### - Return value:
None
##### - Arguments:
| [ in ] | type | condition | description
|--|--|--|--|
| path | string | path exists | the path to the picture to convert.
| new_size | [integer, integer] | [> 0, > 0] | Resize width and height in pixels. 
| transparent_rgb | (integer, integer, integer) | none | RGB code of the color that is meant to be transparent in the picture.
---
### <a name="engine.auto_scale"></a>📌 auto_scale [property](#engine-props) 
##### Description: 
Boolean: Whether the [Engine.VirtualScene(s)](#engine.virtualscene) created with this [Engine](#engine) instance's [`new_scene()`](#engine.new_scene) method will try to rescale the terminal window.
### <a name="engine.vscenes"></a>📌 vscenes [property](#engine-props) 
##### Description: 
Dictionnary of all the [Engine.VirtualScene(s)](#engine.virtualscene) instances created with this [Engine](#engine) instance's [`new_scene()`](#engine.new_scene) method mapped by their names.

---
## <a name="engine.virtualscene"></a>📜 Engine.VirtualScene [(sub)class](#classes)
The VirtualScene (or you could say "Scene") instance's job is to display [TextSprite](#engine.textasset.textsprite) instances correctly, and as fast as possible, in the terminal.
### <a name="virtualscene-methods"></a>Methods
- [\_\_init\_\_](#virtualscene-init)
- [put](#virtualscene-put)
- [erase](#virtualscene-erase)
- [show](#virtaulscene-show)

---
### <a name="virtualscene-init"></a>🧰 \_\_init\_\_ [method](#virtualscene-methods)
##### - Description:
- Inits the Scene instance:
	- Inits all its properties to their default values.
	- Rescales the terminal window if [Engine.auto_scale](#engine.auto_scale) is set to `True`.

##### - Prototype:
```python
def __init__(self, coord_x=0, coord_y=0, res_x=64, res_y=64, layer_count=10, scale=True)
```
##### - Return value:
No return value
##### - Arguments:
| [ in ] | type | condition | description |
|--|--|--|--|
| coord_x | int | none | Distance of the Scene instance in character width to the terminal window's left border.
| coord_y | int | none | Distance of the Scene instance in character height to the terminal window's top border.
| res_x | int | > 0 | The Scene instance's width in pixels.
| res_y | int | > 0 | The Scene instance's height in pixels.
| layer_count | int | > 0 | The number of layers that the Scene instance has. In other words, how many different level of supperposition it has to manage. (An empty layer causes no significant lag).

---
### <a name="virtualscene-put"></a>🧰 put [method](#virtualscene-methods)
##### - Description:
- Removes a Sprite instance from the Scene instance if it was already in.
- Puts a Sprite instance in one of the Scene instance's layers. 

In order to see it in action, you must [show](#scene-show) the Scene instance again.
##### - Prototype:
```python
def put(sefl, sprite, crd_x, crd_y, layer)
```
##### - Return value:
No return value
##### - Arguments:
| [ in ] | type | condition | description
|--|--|--|--|
| sprite | [Engine.TextAsset.TextSprite](#engine.textasset.textsprite) | none | The Sprite instance to put in the Scene
| crd_x | integer | none | Distance of the Sprite to the Scene instance's left border in character width.
| crd_y | integer | none | Distance of the Sprite to the Scene instance's top border in character height.
| layer | integer | > 0 and < `len(scene.layers)` | The index of the layer in which you put the Sprite instance.

---
### <a name="virtualscene-erase"></a>🧰 erase [method](#virtualscene-methods)
##### - Description:
##### - Prototype:
```python
def erase(self, sprite)
```
##### - Return value:
##### - Arguments:
| [ in ] | type | description |
|--|--|--|
| sprite | [Engine.TextAsset.TextSprite](#engine.textasset.textsprite) | The Sprite instance to erase from the Scene

---
### <a name="virtualscene-show"></a>🧰 show [method](#virtualscene-methods)
##### - Description:
Refreshes the display if the Scene instance got updated.
##### - Prototype:
```python
def show(self, debug=False)
```
##### - Return value:
No return value
##### - Arguments:
| [ in ] | type | description |
|--|--|--|
| debug | boolean | Whether the debug overlay for this method should be displayed (show fps and frame latency)

---
## <a name="engine.textasset"></a>📜 Engine.TextAsset [(sub)class](#classes)
 A TextAsset instance (Asset) is a building manual for creating [TextAsset.TextSprites](#engine.textasset.textsprite). It can convert an easy syntax for creating text based sprites into a format more suitable for the [Engine.VirtualScene](#engine.virtualscene) instance.
 ### Subclass
-  [TextSprite](#engine.textasset.textsprite)
### <a name="textasset-props"></a>Properties
-  [building_manual](#textasset.building_manual)
-  [chart](#textasset.building_manual)

### <a name="textasset-methods"></a>Methods
- [\_\_init\_\_](#textasset-init)
- [generate_chart](#textasset-generate_chart)
- [to_sprite](#textasset-to_sprite)
---
### <a name="textasset-init"></a>🧰 \_\_init\_\_ [method](#textasset-methods)
##### - Description:
Inits the TextAsset instance and call its [generate_chart](#textasset-generate_chart)  method.
##### - Prototype:
```python
def __init__(self, building_manual)
```
##### - Return value:
No return value
##### - Arguments:
| [ in ] | type | description
|--|--|--|
| building_manual | Array of strings | The building manual for the Asset. See [building_manual](#textasset.building_manual) for more details. 
---
### <a name="textasset-generate_chart"></a>🧰 generate_chart [method](#textasset-methods)
##### - Description:
Generates the Asset instance's [chart](#textasset.chart) property by interpreting its [building_manual](#textasset.building_manual) property. 
##### - Prototype:
```python
def generate_chart(self)
```
##### - Return value:
No return value
##### - Arguments:
None

---
### <a name="textasset-to_sprite"></a>🧰 to_sprite [method](#textasset-methods)
##### - Description:
Creates an empty [TextSprite](#engine.textasset.textsprite) instance, sets its Asset property to `self` and returns it.
##### - Prototype:
```python
def to_sprite(self)
```
##### - Return value:
[TextSprite](#engine.textasset.textsprite) A sprite which chart will be the copy of this Asset's [chart](#textasset.chart).
##### - Arguments:
None
### <a name="textasset.building_manual"></a>📌 building_manual [property](#textasset-props)
##### Description: 
A building_manual is an array of strings which represents each line needed in order to draw your text sprite. Here come some examples:

A square made of `a` chars:
```python
[
"aaaaaaaa",
"aaaaaaaa",
"aaaaaaaa",
"aaaaaaaa" 
]
```
A menu (just a sprite, not functional):
```python
[
"=== MENU ===",
"|-choice 1 |",
"|-choice 2 |",
"|-choice 3 |",
"|-exit     |",
"============"
]
```
You can add `style codes` to your building manual. Thoses codes are the following:
- `bc:<color>` Puts a colored background to everything following it. 
- `fc:<color>` Puts a font color to everything following it.
- `cc:0` Stops both background and font color.

With `<color>` being a number between 0 and 255 

---
### <a name="textasset.chart"></a>📌 chart [property](#textasset-props)
##### Description:
Cells data generated from the textAsset's building manual which makes printing sprites more manageable and therefore more optimised.

---
### <a name="textasset.prtcrd"></a>📌 prtcrd [property](#textasset-props)
##### Description:
A python set of (x, y) tuples representing all the coordinates in the chart. In other words, it is the set of all the cells covered by a [Sprite](#engine.textasset.textsprite) instance resulting of this Asset instance.

---
## <a name="engine.textasset.textsprite"></a>📜 Engine.TextAsset.TextSprite [(sub)class](#classes)
TextSprites (or Sprites) are what the [Engine.VirtualScene](#engine.virtualscene) instances can display. They have many properties that one can tweak in order to change how the sprite instance is displayed. Whether it is its texture, its scene, its layer on the scene, or its (x, y) position on the scene.
### <a name="textsprite-props"></a>Properties:
- [chart](#textsprite.chart)
- [prtcrd](#textsprite.prtcrd)
- [act_prtcrd](#textsprite.act_prtcrd)
- [scene](#textsprite.scene)
- [layer](#textsprite.layer)
- [x](#textsprite.x)
- [y](#textsprite.y)
### <a name="textsprite-methods"></a>Methods:
- [\_\_init\_\_](#textsprite-init)
- [set_asset](#textsprite-set_asset)
---
### <a name="textsprite-init"></a> 🧰 \_\_init\_\_ [method](#textsprite-methods)
##### - Description:
Inits the TextSprite:
- Sets its [chart](#textsprite.chart) property to `None`
- Sets its [prtcrd](#textsprite.prtcrd) property to `set()`
- Sets its [act_prtcrd](#textsprite.act_prtcrd) property to `set()`
- Sets its [scene](#textsprite.scene) property to `None`
- Sets its [layer](#textsprite.layer) property to `None`
- Sets its [x](#textsprite.x) property to `0`
- Sets its [y](#textsprite.y) property to `0`
##### - Prototype:
```python
def __init__(self)
```
##### - Return value:
No return value
##### - Arguments:
None

---
### <a name="textsprite-set_asset"></a> 🧰 set_asset [method](#textsprite-methods)
##### - Description:
Copies an Asset's [chart](#textasset.chart) property and [prtcrd](#textasset.prtcrd) property into the Sprite's [chart](#textsprite.chart) property and [prtcrd](#textsprite.prtcrd) property, and regenerates its [act_prtcrd](#textsprite.act_prtcrd) if its coordinates have changed, or if the Asset's "set of printed coordinates" is different from the sprite's previous one.
##### - Prototype:
```python
def set_asset(self, asset)
```
##### Return value:
No return value
##### - Arguments:
| [ in ] | type | description
|--|--|--|
| asset | [Engine.TextAsset](#engine.textasset) | The Asset instance which [chart](#textasset.chart) property and [prtcrd](#textasset.prtcrd) property will be copied into the Sprite's [chart](#textsprite.chart) property and [prtcrd](#textsprite.prtcrd) property.|

---
### <a name="textsprite.chart"></a>📌 chart [property](#textsprite-props)
##### Description:
Exactly the same as [TextAsset.chart](#textasset.chart)

---
### <a name="textsprite.prtcrd"></a>📌 prtcrd [property](#textsprite-props)
##### Description:
Exactly the same as [TextAsset.prtcrd](#textasset.prtcrd)

---
### <a name="textsprite.act_prtcrd"></a>📌 act_prtcrd [property](#textsprite-props)
##### Description:
Similar to [TextAsset.prtcrd](#textasset.prtcrd), but here it is a set of all the cells covered by the Sprite **relative to its current position's (x, y) coordinates in its [Scene](#textsprite.scene)**.

---
### <a name="textsprite.scene"></a>📌 scene [property](#textsprite-props)
##### Description:
The [Engine.VirtualScene](#engine.virtualscene) (Scene) instance in which this Sprite instance is displayed.

---
### <a name="textsprite.layer"></a>📌 layer [property](#textsprite-props)
##### Description:
The layer in which resides this Sprite instance within its [Scene](#textsprite.scene).

---
### <a name="textsprite.x"></a>📌 x [property](#textsprite-props)
##### Description:
The distance in character width of the Sprite to its [Scene](#textsprite.scene)'s left border.

---
### <a name="textsprite.y"></a>📌 y [property](#textsprite-props)
##### Description:
The distance in character height of the Sprite to its [Scene](#textsprite.scene)'s top border.

---
# <a name="license"></a>License
This library is distributed under a CC-BY-SA license:
- You can:
	- **Share** — copy and redistribute the material in any medium or format
	- **Adapt** — remix, transform, and build upon the material for any purpose, **even commercially.**
- Under the following terms:
	- **Attribution** — You must give [appropriate credit](https://creativecommons.org/licenses/by-sa/2.0/fr/deed.en#), provide a link to the license, and [indicate if changes were made](https://creativecommons.org/licenses/by-sa/2.0/fr/deed.en#). You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
	- **ShareAlike** — If you remix, transform, or build upon the material, **you must distribute your contributions under the [same license](https://creativecommons.org/licenses/by-sa/2.0/fr/deed.en#) as the original.**

### More info at: https://creativecommons.org/licenses/by-sa/2.0/fr/deed.en

### Any kind of collaboration on this project is welcomed !  **(●^◡ ^● )**

### <a name="thanks"></a>Thanks for reading !

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTkwNzc1Nzg0NCwtMTUxNjM3NDk2NSw3ND
A5MTYxMjEsODc5MTI5OTYsMTA5ODkxNzA4OSwtMjA0MzUxMTU5
MywtMTIwODkxMDQxMiwtNzI4NzE3MjQyLDE5MDA5MTU3MjEsLT
EyNjk0MTMzMDYsLTEyNTA4MjE3MTEsLTIwNzAyNTQ4NjMsLTY0
MjYxNzU1NywtNzI2NTY3Njg2LC04NDgzOTg2ODMsOTEzNDYxMz
c3LC0xNzgxODg3MzU5LC0xNzg5MDM3ODI2LDE0MTUyMDE3MDEs
LTE1MzIwMDI5NTldfQ==
-->