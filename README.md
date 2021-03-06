# 🌸 Flore 1 [Not updated anymore]
 This is the first **python** 2D-ANSI game engine **rendering in the terminal**.
 This library features the engine class itself, along with some utilitary classes for a more efficient use of it.
 ```
 pip install flore1
 ```

# Table of contents:

 1. [**Features**](#features)
 2. [**Roadmap**](#roadmap) 
 3. [**Compatibility**](#compat)
 4. [**Examples**](#examples)
 5. [**Documentation**](#doc)
 6. [**Tools**](#tools)
 7. [**License**](#license)

# <a name="features"></a>What can it do ?

#### Graphics:
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

#### Input handling:
- Input profiles for easy key customization
- Tell if one of the actions in the input profile has one of its corresponding key pressed.
- `alt_input()` Alternative to `input()` which is very customizable
- Simultaneous keys / shortcut detection support
#  <a name="roadmap"></a>What is planned ?
- `Gradually` Documentation and tutorials
- `Gradually` Quality of life improvements
- `Gradually` Optimization
- `High priority` Mouse handler
- `High priority` UI helper classes
- `Medium priority` Basic server/client fonctionnalities 
- `Low priority` Sound management  
- `Low priority` Remote SSH rendering  


#  <a name="compat"></a>Known compatible terminals
**According to the latest tests**:
1. `fast` `good rendering` `Windows 10` `CPU`- **cmd.exe**
2. `fast` `good rendering` `Windows 10` `CPU`- **Powershell**
3. `fast` `bad rendering` `Windows 10` `GPU`- **new terminal**
4. `slow` `good rendering` `Linux` `CPU`- **repl.it terminal emulator**
 
**Notes**: 
- It has great probability of rendering well on any modern terminal which supports the following escapes codes:
```python
"\033[<row>;<col>H"
"\33[0m"
"\u001b[49;5;<color_code>m"
"\u001b[39;5;<color_code>m"
```
- Terminals that do not support thoses will never be compatibles. 
- Flore1 is not using ncurses

# <a name="exemples"></a>Examples
### ⏳ Refresh example 1 :
#### Description:
Prints `1`, `test` and `3.14` 2 times per second.
#### Code:
```python
from flore1 import *

# Creating the Refresh instance
# and initializing its call frequency (fps)
refr = Refresh(fps=2) 

# Function we want to be called
def example(arg1, arg2, arg3='something'):
	print(arg1)
	print(arg2)
	print(arg3)

# asking to add the function to the calling queue
refr.feed(example, (1, 'test'), {'arg3':3.14})
#	(function, *args, **kwargs)
# How example will be called then:
#     example(1, 'test', 3.14)

# Repeatedly asking the Refresh Instance to
# check if it is time to call all the function
# in its calling queue.
while True:
	refr.run()
```
#  <a name="doc"></a> Documentation 
Flore1 only features documentation with Google-style docstrings in the code. Markdown documentation is coming soon.
# <a name="tools"></a>Tools
- [flore1-paint](https://github.com/AnicetNgrt/flore1-paint) An open source paint software for drawing and animating flore1 TextAssets

# <a name="license"></a>License
This library is distributed under a CC-BY-SA license:
- You can:
	- **Share** — copy and redistribute the material in any medium or format
	- **Adapt** — remix, transform, and build upon the material for any purpose, **even commercially.**
- Under the following terms:
	- **Attribution** — You must give [appropriate credit](https://creativecommons.org/licenses/by-sa/2.0/fr/deed.en#), provide a link to the license, and [indicate if changes were made](https://creativecommons.org/licenses/by-sa/2.0/fr/deed.en#). You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
	- **ShareAlike** — If you remix, transform, or build upon the material, **you must distribute your contributions under the [same license](https://creativecommons.org/licenses/by-sa/2.0/fr/deed.en#) as the original.**

#### More info at: https://creativecommons.org/licenses/by-sa/2.0/fr/deed.en
___
### Any kind of collaboration on this project is welcomed !

##### <a name="thanks"></a>Thanks for reading !

<!--stackedit_data:
eyJoaXN0b3J5IjpbOTc0NzUzOTI0LDExNDg2MzkxOTAsLTY2OT
YxMDM1Nyw4MTQxOTQ5MTMsMTU1OTEzMjE2OSwxMzIxMTE5NTIy
LDEzNzg5MTY2NDMsLTI5NzQ5NjUzNywtMTg1MDc4MzIyMiw5Mj
EzMTQ0MjEsMTU4ODY4MDE3NSwtODgwNjg3ODUsLTE2OTA5NjE0
MDgsLTkwNzc1Nzg0NCwtMTUxNjM3NDk2NSw3NDA5MTYxMjEsOD
c5MTI5OTYsMTA5ODkxNzA4OSwtMjA0MzUxMTU5MywtMTIwODkx
MDQxMl19
-->
