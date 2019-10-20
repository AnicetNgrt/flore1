![logo](https://imgur.com/YkSRs3R.png)
# Flore 1 - pre alpha
The first **python** 2D game engine **rendering in the terminal**.

## What can it do ?
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

## What is planned ?:
#### Everything else you would expect from a barebone game engine:
 - Input management
 - Sound management
 - Remote SSH rendering
 - Basic server/client fonctionnalities


## Known compatible terminal emulators:
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
  
## License:
This library is distributed under a CC-BY-SA license.
Any kind of collaboration on this project is welcomed  (●^◡ ^● )

