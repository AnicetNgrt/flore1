 
# Flore 1 - pre alpha
 The first **python** 2D game engine **rendering in the terminal**.

### Note:
Thanks a lot for paying attention to my work. 
My name is Anicet Nougaret, and I'm doing all of this alone. 
This project will always remain open source and free.
Therefore, please consider donating, it will greatly support this project ! 
\\(●'◡'●)/
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg) ](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=56G94VB5RYGKN&source=url) 

# Table of contents:

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
- `Gradually` Documentation and tutorials
- `Gradually` Optimization
- `High priority` Input management
- `Medium priority` Basic server/client fonctionnalities 
- `Low priority` Sound management  
- `Low priority` Remote SSH rendering  


#  <a name="compat"></a>Known compatible terminals
 1. Windows 10 - Powershell
 2. Windows 10 - cmd
 3. Windows 10 - new GPU terminal
 4. Windows 10 - python terminal
 5. Linux - repl.it terminal emulator
 
**Notes**: 
- It has great probability of rendering well on any modern terminal which supports the following escapes codes:
```python
"\033[<row>;<col>H"
"\33[0m"
"\u001b[49;5;<color_code>m"
"\u001b[39;5;<color_code>m"
```
- Terminals that do not support thoses will never be compatibles.
- 
    
  #  <a name="tuto"></a>Tutorials
  ### Table of content:
  

 0. [Getting started](#tuto0)
 1. [Displaying a static text sprite in a scene](#tuto1)
 2. [Introduction to game loops: Moving a sprite across it's scene](#tuto2)
 3. [Converting a picture to a sprite and displaying it](#tuto3)
 4. [Flipbooks: Display a gif on the terminal as an animated text sprite](#tuto4)
 
## <a name="tuto0"></a>0/ Getting started:
### 💿 Installation with pip:
  If you don't have python (3.67 or above) and pip installed, install them first.
  
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
    auto_scale = True, # Whether the terminal should be rescaled
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
Now let's put the sprite in and refresh:
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
 - `"cc:0"` This stops both background color and font color *(due to limitation you can't seem to stop only one)*

And if you want to know which `<code>` gives you which color, here you go:
![terminal colors](http://www.lihaoyi.com/post/Ansi/Rainbow256.png)*picture credit: http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html*

Ok, now that you know this, let's tweak our asset'sinsert codes inside our building manual with codes:
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
## <a name="tuto2"></a>2/ Introduction to game loops: Moving a sprite across it's scene:
### 🧭 What we will do:
![fastboi](https://imgur.com/BRbsNUR.gif)
This tutorial is about moving a sprite across the scene.
[-> I just want the code thanks.](#tuto2_code)
### 🚠Introduction:
-So how does moving works in your mind ? 
-We can put sprites at some coordinates and refresh the scene. So why not doing this in a loop ?
-**Correct !** 

With flore1 there is a very elegafficient way of doing that thanks to the `flore1.Refresh` class. Let me show you:

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
So what we did here is that we created our Refresh instance, and asked it to run at 24 frames per second. Which means that our `game_loop.i` will try to sync with the Refresh in order to be incremented 24 times per second. If you decide to display so many sprites that the Refresh slows down to 12 frames per second, then `game_loop.i` will increment by 2 on every frame, in order to keep up with it's 24 fps objective. 
What I mean by that is that your sprite will always move at the same speed regardless of the lag (in theory).
```python
# following the previously given code:
loop_tuple = (game_loop, Scene, super_sprite)
Refresh.feed(*loop_tuple) # don't forget the *
```
Here we formed a tuple composed with the function `game_loop` itself, and all the variables we want to give as inputs for its keyword arguments.

**Note**: If your `game_loop` function has default arguments, I advice you see tutorial 4 for a more in depth explanation of the `Refresh.feed` method's syntax.
### 😵 While I loop the loop:
Now you have a super cool refresh, which task is to run `game_loop(Refresh, Scene, super_sprite)` at 24 fps.
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
But here comes the issue: **size**. Because even if you ask your terminal to go 14px font style, it won't be easy to display anything bigger than 300*300px. So, yeah, tThis is more of a pixel-art engine than a fancy graphical library. But come on, it's on the terminal :D !
Ok let's try to display `anicet.jpg` (resized of course) in the terminal:
```python
# following the previously given code:
anicet_asset = Engine.pic_to_textAsset('assets/anicet.jpg', 
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
As you can see, the originaly 1024*1024px picture got quite resized ! FilVery detailed pictures almost never downscale without ugly artifacts everywhere. This is due to the limited n=255 terminal's color range... so I have no other choice. ¯\\\_(ツ)_/¯
### 📚 Displaying more pictures
Now let's repeat the process in order to display more pictures.
Don't forget to erase the `time.sleep(30)` you put previously, unless you like waiting a lot.
#### a. Let's display a picture with transparency:
```python
# following the previously given code
bow_icon_asset = Engine.pic_to_textAsset('assets/archer.png', 
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
avatar_asset = Engine.pic_to_textAsset('assets/aniss.png', 
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

anicet_asset = Engine.pic_to_textAsset('assets/anicet.jpg', new_size="AUTO")
anicet_sprite = anicet_asset.to_sprite()
Scene.put(anicet_sprite, 10, 10, 1)

bow_icon_asset = Engine.pic_to_textAsset('assets/archer.png', new_size=["32","32"], transparent_rgb=(238, 195, 154))
bow_icon_sprite = bow_icon_asset.to_sprite()
Scene.put(bow_icon_sprite, 10, 60, 2)

avatar_asset = Engine.pic_to_textAsset('assets/aniss.png', new_size=["50","50"])
avatar_sprite = avatar_asset.to_sprite()
Scene.put(avatar_sprite, 60, 20, 3)

Scene.show()

time.sleep(30)
```
## <a name="tuto4"></a> Flipbooks: Display a gif on the terminal as an animated text sprite
### 🧭 What we will do:

![60fps flavour](https://imgur.com/Xo6XNs1.gif)
In this tutorial we will display an animated GIF in the terminal with transparency.
[-> I just want the code thanks.](#tuto4_code)
### 🎬 Finding and making a GIF compatible with flore1:
First we need to find a suitable low-res `.gif` (you can also put large sized GIF since the engine can rescale pictures, but in this tutorial we won't do it).
Personnaly, I'm not a pro pixel art animator so I took my GIF [here](#https://untiedgames.itch.io/five-free-pixel-explosions).


![explosion](https://imgur.com/8kXy0FB.gif)
#### You need to convert your GIF to a folder containing it's frames as PNG files
Note that the original source I gave lets you download a folder containing all individuals frames as png. Which is exactly what the engine needs. But I case you only have a `.gif` file, such as the one above go to [https://ezgif.com/split](https://ezgif.com/split), import your gif, download the `.zip` containing the frames, and extract it in a folder in your project.
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
**Note**: You need your frame's to be ranked in lexicographic order accordingly to their order of appearance in your original GIF.
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
	'assets/explosion/', # the path to all our frames 
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
Here, we are feeding it a bit differently than on tutorial 2, so let me explain hwo it works:
#### `Refresh.feed`'s syntax:
The first argument must be a function or a method (ex: `my_function`, or `Object.method`), the second argument must be a tuple of keyword arguments for the function (ex: `(x,y,0,18,"ok")`), and the third one must be a dictionnary of default arguments for the function (ex: `{"name"="Anicet","favorite_color"="yellow"}`).

#### Now let's loop our `Refresh.run()` as we did in tutorial 2:
```python
# following the previously given code
while True:
    Refresh.run()
```
Done, now run it and admire:

![Done, now run it and admire.](https://imgur.com/Xo6XNs1.gif)
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
	'assets/explosion/', 
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
## <a name="classes"></a>Classes
 
 - [Flipbook](#flipbook)
 - [Refresh](#refresh)
 - [Engine](#engine)
	 - [Engine.VirtualScene](#engine.virtualscene)
	 - [Engine.TextAsset](#engine.textasset)
		 - [Engine.TextAsset.TextSprite](#engine.textasset.textsprite)
## <a name="flipbook"></a>Flipbook [class](#classes)


The Flipbook class lets you easily animate [TextSprites](#textsprites) by computing their texture change rate, function of the Flipbook's [Refresh](#refresh) 's execution rate and the Flipbook frame rate goal. 
### <a name="flipbook-props"></a>Public properties

 - [material](#flipbook.material)

### <a name="flipbook-methods"></a>Methods
- [\_\_init\_\_](#flipbook-init) 
- [start](#flipbook-start) 
- [stop](#flipbook-stop) 
---
### <a name="flipbook-init"></a> \_\_init\_\_ [method](#methods)

##### - Description:
Inits the Flipbook: 
- Inits its [material](#flipbook.material) property with a tuple of a function called `play` and its arguments. 
	- The `play` function calls the Flipbook's sprite's [set_asset](#textsprite-set_asset) method in rythm, in order to change the Flipbook's sprite's texture at the rythm of the frame rate goal. 

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
A tuple composed with a function which changes the Flipbook's sprite's texture at some rate function of the Flipbook's Refresh and the Flipbook's frame rate goal, and also composed of all this function's arguments. Feeding a Refresh with *(this tuple) will start the Flipbook.


## <a name="refresh"></a>Refresh [class](#classes)
The Refresh class executes a stack of functions that you "fed" it with every time you tell it to "do" it. It constantly calculates execution time and calls the functions you fed it with accordingly, while also incrementing faster/slower all of its stack's function's `.i` attribute depending on whether the execution latency keeps up or not with the execution rate goal. This way, functions you fed it with can keep up with the current execution latency. For instance, if your function goal is to animate sprite it can then decide to skip frames.
### <a name="refresh-methods"></a>Methods
- [\_\_init\_\_](#refresh-init) 
- [terminate](#refresh-terminate) 
- [feed](#refresh-feed) 
- [do](#refresh-do) 
- [run](#refresh-run) 
### <a name="refresh-init"></a> \_\_init\_\_ [method](#methods)
---
### <a name="refresh-terminate"></a> terminate [method](#methods)
---
### <a name="refresh-feed"></a> feed [method](#methods)
---
### <a name="refresh-do"></a> do [method](#methods)
---
### <a name="refresh-run"></a> run [method](#methods)
---
## <a name="engine"></a>Engine [class](#classes)

- [\_\_init\_\_](#engine-init) 
- [new_scene](#engine-new_scene) 
- [del_scene](#engine-del_scene) 
- [new_sprite](#engine-new_sprite) 
- [find_trsprt_index](#engine-find_trsprt_index) 
- [pic_to_textAsset](#engine-pic_to_textasset) 
### <a name="engine-init"></a> \_\_init\_\_
[->method](#methods)

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



 
# <a name="license"></a>License
This library is distributed under a CC-BY-SA license.
Any kind of collaboration on this project is welcomed !  **(●^◡ ^● )**

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyMDg5NDAxMzcsLTEzMzUwODcwMDIsMT
kxNDc4ODY5MSwtNzc2MDM5MDIxLC0xNDgzMjY2NzkzLC0xMzAy
NDA1Nzg2LDkxMzM3NDI4OSwtMTAxNTkxNjkxNSwtMTc1OTE2MT
M3NSw4NDkzNDAxNzIsLTMwMTA2Mjk4MSwtMTg5NDg1NTU0OCwt
MTM0MTQyNDEzMSwtMjEyMjI4MzA3OCwtOTcxOTQzNTY4LC03MD
I3MzkxMDQsLTcwMjczOTEwNCwxMDUxOTIzNjAsMTM3NTU5NzU5
NCwxNDc0NjI5MTI2XX0=
-->