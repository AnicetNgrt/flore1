 
# Flore 1 - pre alpha
 The first **python** 2D game engine **rendering in the terminal**.

## Table of content:

 1. [**Features**](#features)
 2. [**Roadmap**](#roadmap) 
 3. [**Compatibility**](#compat)
 4. [**Tutorials**](#tuto)
 5. [**Documentation**](#doc)
 6. [**License**](#license)

## <a name="features"></a>What can it do ?
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

##  <a name="roadmap"></a>What is planned ?
 - Input management
 - Sound management
 - Remote SSH rendering
 - Basic server/client fonctionnalities


##  <a name="compat"></a>Known compatible terminals
 - Windows 10 - Powershell
 - Windows 10 - cmd
 - Windows 10 - new GPU terminal
 - Windows 10 - python terminal
 - Linux - repl.it terminal emulator
 
 Note that it has great probability of rendering well on any modern shell which supports the following escapes codes:
 

    "\033[<row>;<col>H"
    "\33[0m"
    "\u001b[49;5;<color_code>m"
    "\u001b[39;5;<color_code>m"
    
  ##  <a name="doc"></a>Tutorial  (aimed towards beginners)
  
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

### 🎨 Creating a text sprite:

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
  Now, in order to create our text sprite we need to create a "building manual" for the sprite. Don't worry it is just an array of strings.
```python
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
  
 ##  <a name="doc"></a>Documentation
 The flore1 module has 3 top level classes located in `flore1/flore1.py`:
 

 - [Engine](#engine_doc)
 - [Refresh](#refresh_doc)
 - [Flipbook](#anim_doc)

 ### <a name="engine_doc"></a>Engine class:
##### >>>> 🚧  work in progress
 
 
## <a name="license"></a>License
This library is distributed under a CC-BY-SA license.
Any kind of collaboration on this project is welcomed !  **(●^◡ ^● )**

