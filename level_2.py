
'''
to advance, player must...
1. battle track successfully
    -fade/mist with animation?
2. obtain 3 brezlin
3. obtain 1 doner kebab
4. be yelled at by 1 person
5. finish one maze

# include animations from https://github.com/peterbrittain/asciimatics/wiki
#handle having enough brezlin to continue to next level
'''

import time
from os import system
import cmd
import textwrap
import sys
import os
from time import sleep
import random
###### asciimatics imports
from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText



def n6_game_level_2(screen):
    effects = [
        Cycle(
            screen,
            FigletText("LEVEL  2", font='big'),
            screen.height // 2 - 8),
        Cycle(
            screen,
            FigletText("GET  IT", font='big'),
            screen.height // 2 + 3),
        Stars(screen, (screen.width + screen.height) // 2)
    ]
    screen.play([Scene(effects, 500)])
    
Screen.wrapper(n6_game_level_2) # whole game jumps here. fix this





