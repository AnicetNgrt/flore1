 
# 🌸 Flore 1 
 This is the first **python** 2D game engine/graphical library **rendering in the terminal**.
 This library features the engine class itself, along with some utilitary classes for a more efficient use of it.


**[Quick start](#tuto0)**

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
- `Gradually` Optimization
- `High priority` Input management
- `Medium priority` Basic server/client fonctionnalities 
- `Low priority` Sound management  
- `Low priority` Remote SSH rendering  


#  <a name="compat"></a>Known compatible terminals
**According to the latest tests**:
 1. `good perf.` `medium rendering` `Windows 10` `CPU`- **Powershell**
 2. `good perf.` `good rendering` `Windows 10` `CPU`- **cmd.exe**
 3. `good perf.` `bad rendering` `Windows 10` `GPU`- **new terminal**
 4. `good perf.` `good rendering` `Windows 10` `CPU`- **python terminal**
 5. `bad perf.` `good rendering` `Linux` `CPU`- **repl.it terminal emulator**
 
**Notes**: 
- It has great probability of rendering well on any modern terminal which supports the following escapes codes:
```python
"\033[<row>;<col>H"
"\33[0m"
"\u001b[49;5;<color_code>m"
"\u001b[39;5;<color_code>m"
```
- Terminals that do not support thoses will never be compatibles. 
    
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
This will be the very foundation for all the following tutorials !
## <a name="tuto1"></a>1/ Displaying a static text sprite:
### 🧭 What we will do:
![enter image description here](https://imgur.com/XVbCCmJ.png)
This tutorial is about displaying a text sprite in a scene with colors and defined (x, y) position.
[-> I just want the code thanks.](#tuto1_code)

### 🎨 Creating a text sprite:
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
## <a name="classes"></a>Classes
 
 - [Flipbook](#flipbook) 
 - [Refresh](#refresh)
 - [Engine](#engine)
	 - [Engine.VirtualScene](#engine.virtualscene) *`Scenes`*
	 - [Engine.TextAsset](#engine.textasset) *`Assets`*
		 - [Engine.TextAsset.TextSprite](#engine.textasset.textsprite) *`Sprites`*
## <a name="flipbook"></a>Flipbook [class](#classes)


The Flipbook class lets you easily animate [TextSprites](#textsprites) by computing their texture change rate, function of the Flipbook's [Refresh](#refresh) 's execution rate and the Flipbook frame rate goal. 
### <a name="flipbook-props"></a>Properties

 - [material](#flipbook.material)

### <a name="flipbook-methods"></a>Methods
- [\_\_init\_\_](#flipbook-init) 
- [start](#flipbook-start) 
- [stop](#flipbook-stop) 
---
### <a name="flipbook-init"></a> \_\_init\_\_ [method](#methods)

##### - Description:
Inits the Flipbook: 
- Inits its [material](#flipbook.material) property
	- Creates the `play` function. See [material](#flipbook.material)  for more details.

##### - Prototype:
```python
def __init__(self, Engine, Refresh, Sprite, path="", size=[32, 32], transparent_rgb=(-1, -1, -1), fps=24, sync="True")
```
##### - Return value:
No return value
##### - Arguments:
| [ in ] | type  | description |
|--|--|--|
| self | [Flipbook](#flipbook) | Flipbook instance just created 
| Engine | [Engine](#engine) | Engine instance that computes for the creation of the flipbook from its set of pictures
| Refresh | [Refresh](#refresh) | Refresh instance that runs the flipbook 
| Sprite | [Sprite](#engine.textasset.textsprite) | TextSprite instance that has its texture animated by the flipbook 
| path | string | Path to a folder containing all the frames for the animation in lexicographical order 
| size | array of integers | [width, height] for the animated sprite 
| transparent_rgb | tuple of integers | RGB of the transparent color in the flipbook's frames 
| fps | integer | Frame rate goal for the flipbook in frame per second
| sync | boolean | Whether the flipbook skips frame if the refresh slows down
---
### <a name="flipbook-start"></a> start [method](#methods)
##### - Description:
Feeds the Flipbook's Refresh instance with the Flipbook's [material](#flipbook.material) property.
##### - Prototype:
```python
def start(self)
```
##### - Return value:
No return value
##### - Arguments:
| [ in ] | type | description
|--|--|--|
| self | [Flipbook](#flipbook) | Flipbook instance that starts playing
---
### <a name="flipbook-stop"></a> stop [method](#methods)
##### - Description:
Terminates the Flipbook's [material](#flipbook.material) property's function execution within the Flipbook's Refresh instance.
##### - Prototype:
```python
def stop(self)
```
##### - Return value:
No return value
##### - Arguments:
| [ in ] | type | description
|--|--|--|
| self | [Flipbook](#flipbook) | Flipbook instance that stops playing
---
### <a name="flipbook.material"></a> material [property](#flipbook-props) 
##### Description:
A tuple composed with `play`: a function which changes the Flipbook's sprite's texture function of the Flipbook's Refresh and the Flipbook's frame rate goal, and also composed with all of this function's arguments. Feeding a Refresh with `*(Flibook.material)` starts the Flipbook.


## <a name="refresh"></a>Refresh [class](#classes)
You can "[feed](#refresh-feed)" the Refresh class with a `(function, *args, **kwars)` tuple. It will add it to it's [execution stack](#refresh.stack). Everytime you ask the Refresh to "[do](#refesh-do)" it will call all the `function(*args, **kwargs)` from its stack, compute execution time and wait if the execution time was too fast, or ask all the function that have their attribute `sync` set to `True` in its stack to "skip" frames if it was too slow. Therefore the Refresh class is there for frame stabilisation purposes and speed stabilisation purposes. For more details see the docs on its [methods](#refresh-methods).*

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
### <a name="refresh-init"></a> \_\_init\_\_ [method](#methods)
##### - Description:
Inits all the [properties](#refresh-props) of Refresh.
##### - Prototype:
```python
def __init__(self, fps=35)
```
##### - Return value:
No return value
##### - Arguments:
| [ in ] | type | description
|--|--|--|
| self | [Refresh](#refresh) | Refresh instant to initialize
| fps | integer | Execution rate goal of the Refresh 
---
### <a name="refresh-terminate"></a> terminate [method](#methods)
##### - Description:
Removes a specific `(function, *args, **kwargs)` tuple from the Refresh's execution [stack](#refresh.stack).
In other words, the Refresh stops calling `function(*args, **kwargs)` when it's [do](#refresh-do) method is called.
##### - Prototype:
```python
def terminate(self, func, *args, **kwargs)
```
##### - Return value:
No return value
##### - Arguments:
| [ in ] | type | description
|--|--|--|
| self | [Refresh](#refresh) | The Refresh instance which [stack](#refresh.stack) gets the tuple removed from
| func | function | Function type element of the tuple to remove from the [stack](#refresh.stack)
| *args | *args | Arguments type element of the tuple to remove from the [stack](#refresh.stack) 
| **kwargs | **kwargs | Keyworded arguments type element of the tuple to remove from the [stack](#refresh.stack)

---
### <a name="refresh-feed"></a> feed [method](#methods)
##### - Description:
Adds a `(function, *args, **kwargs)` tuple to the Refresh's execution [stack](#refresh.stack). 
In other words, it asks the Refresh to call `function(*args, **kwargs)` via the [do](#refresh-do) method every time its [run](#refresh-run) method is called, to add its execution time to the total execution latency, and, only if `function.sync = True`, to sync its execution rate with the Refresh's execution latency goal.
##### - Prototype:
```python
def feed(self, function, *args, **kwargs)
```
##### - Return value:
No return value
##### - Arguments:
| [ in ] | type | description
|--|--|--|
| self | [Refresh](#refresh) | The Refresh instance which [stack](#refresh.stack) gets appended with the tuple
| func | function | Function type element of the tuple to append the [stack](#refresh.stack) with
| *args | *args | Arguments type element of the tuple to append the [stack](#refresh.stack) with 
| **kwargs | **kwargs | Keyworded arguments type element of the tuple to append the [stack](#refresh.stack) with
---
### <a name="refresh-do"></a> do [method](#methods)
##### - Description:
For each `(function, *args, **kwargs)` tuple in the Refresh's [stack](#refresh.stack) it may call `function(*args, **kwargs)` (if `function.sync` is True, it only calls it on frame change). But before, if `function.i` does not exist it sets it to `0`, if `function.sync` does not exist, it sets it to `True`, and if `function.refresh` does not exist, it sets it to `self`.
##### - Prototype:
```python
def do(self)
```
##### - Return value:
No return value
##### - Arguments:
| [ in ] | type | description
|--|--|--|
| self | [Refresh](#refresh) | The Refresh instance which [stack](#refresh.stack) is being reviewed
---
### <a name="refresh-run"></a> run [method](#methods)
##### - Description:
Calls the [do](#refresh-do) method and computes its execution time (the latency caused by it). Then it computes the [Refresh.i](#refresh.i) property function of the latency and the [Refresh.fps](#refresh.fps) property. The point is that this property  always augments at the same speed regardless of the low or high latency. Then [Refresh.frame](#refresh.frame) is 
##### - Prototype:
```python
def run(self, debug=False)
```
##### - Return value:
No return value
##### - Arguments:
| [ in ] | type | description
|--|--|--|
| self | [Refresh](#refresh) | The Refresh instance that is ran
| debug | boolean | Whether you want the debug header for this method to show on the top left corner
---
### <a name="refresh.fps"></a> fps [property](#flipbook-props) 
##### Description: 
The frame rate goal of the Refresh instance. It is meant to be an integer.

---
### <a name="refresh.stack"></a> stack [property](#flipbook-props) 
##### Description: 
A list of `(function, *args, **kwargs)` tuple. It lists all the functions that can be called by the Refresh and all their arguments. This depends on whether the function's `.sync` attribute is set to `True` and 

---
### <a name="refresh.frame"></a> frame [property](#flipbook-props) 
##### Description: 
The current "frame" (or turn count) of the Refresh. It is equal to the rounded value of [Refresh.i](#refresh.i). When its value changes the synced functions in the [stack](#refresh.stack) get called and their `.i` attribute changes as much as the [Refresh.frame](#refresh.frame) did. 

**Note**: The unsynced functions in the [stack](#refresh.stack) are always called and their `.i` attribute is just incremented by 1 at each call.

---
## <a name="engine"></a>Engine [class](#classes)

- [\_\_init\_\_](#engine-init) 
- [new_scene](#engine-new_scene) 
- [del_scene](#engine-del_scene) 
- [new_sprite](#engine-new_sprite) 
- [find_trsprt_index](#engine-find_trsprt_index) 
- [pic_to_textAsset](#engine-pic_to_textasset) 
### <a name="engine-init"></a> \_\_init\_\_ [method](#methods)
##### - Description:
##### - Prototype:
```python
```
##### - Return value:

##### - Arguments:
| [ in ] | type | description
|--|--|--|
|  |  |
---
### <a name="engine-new_scene"></a> new_scene
[->method](#methods)

### <a name="engine-del_scene"></a> del_scene
[->method](#methods)

### <a name="engine-new_sprite"></a> new_sprite
[->method](#methods)

### <a name="engine-find_trsprt_index"></a> find_trsprt_index
[->method](#methods)

### <a name="engine-pic_to_textasset"></a> pic_to_textAsset
[->method](#methods)

# <a name="thanks"></a>Thanks for reading !
Your interest and enthusiasm for this project over on reddit.com and on github.com is really what motivates me !
 
# <a name="license"></a>License
This library is distributed under a CC-BY-SA license.
Any kind of collaboration on this project is welcomed !  **(●^◡ ^● )**

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2ODY1NTM3NjYsLTE2OTYxMTc0NzAsMT
M4MTc3MzY5MiwxNjkwMDQxNDYwLC05NTI5MjgzNzgsLTEyMTYx
OTU0NTYsLTY1NzgwNzQxNCw1MzkyMzg5OTAsLTE1NDQ1NDU0ND
MsLTE2Mzc3ODc5OTksMjA3NzczNzI2NywtMTMzNTA4NzAwMiwx
OTE0Nzg4NjkxLC03NzYwMzkwMjEsLTE0ODMyNjY3OTMsLTEzMD
I0MDU3ODYsOTEzMzc0Mjg5LC0xMDE1OTE2OTE1LC0xNzU5MTYx
Mzc1LDg0OTM0MDE3Ml19
-->