# this is the start of the n6 game
''' in this level the player will be have to 
1. get 2 brezlin
2. solve one riddle 
3. befriend Jess through helping her drunk ass get home
  3a. as a reward player will get to see tiddies

this level will be mostly text based with ascii art
level 2 will include ascii animation

  move levels to separate files and call them as needed

'''
import time
from os import system
import cmd
import textwrap
import sys
import os
import time
import random
import level_1

# all variables must be fulfilled to pass level
level_1_passed = False 

item_brezlin = 1
riddle_solved = False
befriend_jess = False


def n6_game_level_1():
  print('')
  print('   L E V E L  O N E  B E G I N  I N  - 5 -  S E C O N D S\n')
  time.sleep(5)
  system('clear')
  # SCREEN = pg.display.set_mode((800, 608)) uncomment when pygame installed - change resolution
  name = input('pick your communicator:  PAPI  F.Daddy  UBreezy  GLITCH  YoungKing     answer:  ').lower()
  if name == 'papi':
    print('wise choice....or was it?')
    time.sleep(2)
    print(r"""

    Depression:  8/10
    Humor: 6/10
    Strength: 9/10

    Modifier: Can take more shit than a toilet


                   ,#####,
                   #_   _#
                   |a` `a|
                   |  u  |
                  \\  =  /   -yo can you get me chicken truck?
                  |\\___/|
          ___ ____/:    :\\____ ___
        .'   `.-===-\\   /-===-.`   '.
       /      .-"````-.-"```-.      \
      /'             =:=             '\
    .'  ' .:    o   -=:=-   o    :. '  `.
    (.'   /'. '-.....-'-.....-' .'\\  '.)
    /  ._/   ".     --:--     ."   \\.  \
   |  .'|      ".  ---:---  ."      |'.  |
   |  : |       |  ---:---  |       | :  |
   \\ : |       |_____._____|       | : /
    /   (       |----|------|       )   \
   /... .|      |    |      |      |. ...\
  |::::/''     /     |       \\    ''\\::::|
  `````       /'    .L_      `\\       `````
             /'-.,__/` `\\__..-'\
            ;      /     \\      ;
            :     /       \\     |
            |    /         \\.   |
            |`../           |  ,/
            ( _ )           |  _)
            |   |           |   |
            |___|           \\___|
            :===|            |==|
             \\  /            |__|
             /\\/\\           /"`8.__
             |oo|            __.//___)
             |==|
              __/


      """)
  elif name == 'F.Daddy':
    print('looks like we found the funny guy!')
    time.sleep(2)
    print(r"""

    Depression: 4/10
    Humor: 10/10
    Strength: 6/10

    Modifier: More charisma than Dwane "THE ROCK" Johnson - less hair than a hookers puss

                                  ,;;;;;;,
                                ,;;;'""`;;\
                              ,;;;/  .'`',;\
                            ,;;;;/   |    \|_
                           /;;;;;    \    / .\
                         ,;;;;;;|     '.  \/_/
                        /;;;;;;;|       \
             _,.---._  /;;;;;;;;|        ;   _.---.,_
           .;;/      `.;;;;;;;;;|         ;'      \;;,
         .;;;/         `;;;;;;;;;.._    .'         \;;;.
        /;;;;|          _;-"`       `"-;_          |;;;;\
       |;;;;;|.---.   .'  __.-"```"-.__  '.   .---.|;;;;;|
       |;;;;;|     `\/  .'/__\     /__\'.  \/`     |;;;;;|
       |;;;;;|       |_/ //  \\   //  \\ \_|       |;;;;;|
       |;;;;;|       |/ |/    || ||    \| \|       |;;;;;|
        \;;;;|    __ || _  .-.\| |/.-.  _ || __    |;;;;/
         \jgs|   / _\|/ = /_o_\   /_o_\ = \|/_ \   |;;;/
          \;;/   |`.-     `   `   `   `     -.`|   \;;/
         _|;'    \ |    _     _   _     _    | /    ';|_
        / .\      \\_  ( '--'(     )'--' )  _//      /. \
        \/_/       \_/|  /_   |   |   _\  |\_/       \_\/
                      | /|\\  \   /  //|\ |
                      |  | \'._'-'_.'/ |  |
                      |  ;  '-.```.-'  ;  |
                      |   \    ```    /   |
    __                ;    '.-`````-.'    ;                __
   /\ \_         __..--\     `-----'     /--..__         _/ /\
   \_'/\`''---''`..;;;;.'.__,       ,__.',;;;;..`''---''`/\'_/
        '-.__'';;;;;;;;;;;,,'._   _.',,;;;;;;;;;;;''__.-'
             ``''--; ;;;;;;;;..`"`..;;;;;;;; ;--''``   _
        .-.       /,;;;;;;;';;;;;;;;;';;;;;;;,\    _.-' `\
      .'  /_     /,;;;;;;'/| ;;;;;;; |\';;;;;;,\  `\     '-'|
     /      )   /,;;;;;',' | ;;;;;;; | ',';;;;;,\   \   .'-./
     `'-..-'   /,;;;;','   | ;;;;;;; |   ',';;;;,\   `"`
              | ;;;','     | ;;;;;;; |  ,  ', ;;;'|
             _\__.-'  .-.  ; ;;;;;;; ;  |'-. '-.__/_
            / .\     (   )  \';;;;;'/   |   |    /. \
            \/_/   (`     `) \';;;'/    '-._|    \_\/
                    '-/ \-'   '._.'         `
                      ```      /.`\
                               |__|


      """)
  elif name == 'ubreezy':
    print('good choice - you get a BREZLIN for choosing wisely')
    time.sleep(2)
    print(r'''
               __       __
             .'  `'._.'`  '.
            |  .--;   ;--.  |
            |  (  /   \  )  |
             \  ;` /^\ `;  /
              :` .'._.'. `;
              '-`'.___.'`-'

           Brezlin count: 1
      ''')
    item_brezlin = 1
    time.sleep(2)
    print(r"""

    Depression: 6/10
    Humor: 6/10
    Strength: 6/10

    Modifier: slays more pussy than brezlin
                                              .
                                   .         ;
      .              .              ;%     ;;
        ,           ,                :;%  %;
         :         ;                   :;%;'     .,
,.        %;     %;            ;        %;'    ,;
  ;       ;%;  %%;        ,     %;    ;%;    ,%'
   %;       %;%;      ,  ;       %;  ;%;   ,%;'
    ;%;      %;        ;%;        % ;%;  ,%;'
     `%;.     ;%;     %;'         `;%%;.%;'
      `:;%.    ;%%. %@;        %; ;@%;%'
         `:%;.  :;bd%;          %;@%;'
           `@%:.  :;%.         ;@@%;'
             `@%.  `;@%.      ;@@%;
               `@%%. `@%%    ;@@%;
                 ;@%. :@%%  %@@%;
                   %@bd%%%bd%%:;
                     #@%%%%%:;;
                     %@@%%%::;
                     %@@@%(o);  . '
                     %@@@o%;:(.,'
                 `.. %@@@o%::;
                    `)@@@o%::;
                     %@@(o)::;
                    .%@@@@%::;
                    ;%@@@@%::;.
                   ;%@@@@%%:;;;.
               ...;%@@@@@%%:;;;;,..   
      """)
  elif name == 'glitch':
    print('a gambling man, i see...')
    time.sleep(2)
    print(r'''

    Depression: 3/10
    Humor: 11/10
    Strength: 3/10

    Modifier: Hey, man. Who needs a modifier when you can work the stock market like me?

                                        .,,cccd$$$$$$$$$$$ccc,
                                    ,cc$$$$$$$$$$$$$$$$$$$$$$$$$cc,
                                  ,d$$$$$$$$$$$$$$$$"J$$$$$$$$$$$$$$c,
                                d$$$$$$$$$$$$$$$$$$,$" ,,`?$$$$$$$$$$$$L
                              ,$$$$$$$$$$$$$$$$$$$$$',J$$$$$$$$$$$$$$$$$b
                             ,$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i `$h
                             $$$$$$$$$$$$$$$$$$$$$$$$$P'  "$$$$$$$$$$$h $$
                            ;$$$$$$$$$$$$$$$$$$$$$$$$F,$$$h,?$$$$$$$$$$h$F
                            `$$$$$$$$$$$$$$$$$$$$$$$F:??$$$:)$$$$P",. $$F
                             ?$$$$$$$$$$$$$$$$$$$$$$(   `$$ J$$F"d$$F,$F
                              ?$$$$$$$$$$$$$$$$$$$$$h,  :P'J$$F  ,$F,$"
                               ?$$$$$$$$$$$$$$$$$$$$$$$ccd$$`$h, ",d$
                                "$$$$$$$$$$$$$$$$$$$$$$$$",cdc $$$$"
                       ,uu,      `?$$$$$$$$$$$$$$$$$$$$$$$$$$$c$$$$h
                   .,d$$$$$$$cc,   `$$$$$$$$$$$$$$$$??$$$$$$$$$$$$$$$,
                 ,d$$$$$$$$$$$$$$$bcccc,,??$$$$$$ccf `"??$$$$??$$$$$$$
                d$$$$$$$$$$$$$$$$$$$$$$$$$h`?$$$$$$h`:...  d$$$$$$$$P
               d$$$$$$$$$$$$$$$$$$$$$$$$$$$$`$$$$$$$hc,,cd$$$$$$$$P"
           =$$?$$$$$$$$P' ?$$$$$$$$$$$$$$$$$;$$$$$$$$$???????",,
              =$$$$$$F       `"?????$$$$$$$$$$$$$$$$$$$$$$$$$$$$$bc
              d$$F"?$$k ,ccc$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i
       .     ,ccc$$c`""u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P",$$$$$$$$$$$$h
    ,d$$$L  J$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" `""$$$??$$$$$$$
  ,d$$$$$$c,"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F       `?J$$$$$$$'
 ,$$$$$$$$$$h`$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F           ?$$$$$$$P""=,
,$$$F?$$$$$$$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F              3$$$$II"?$h,
$$$$$`$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P"               ;$$$??$$$,"?"
$$$$F ?$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P",z'                3$$h   ?$F
       `?$$$$$$$$$$$$$$$??$$$$$$$$$PF"',d$P"                  "?$F
          """""""         ,z$$$$$$$$$$$$$P
                         J$$$$$$$$$$$$$$F
                        ,$$$$$$$$$$$$$$F
                        :$$$$$c?$$$$PF'
                        `$$$$$$$P
                         `?$$$$F


      ''')
  elif name == 'youngking':
    print('young king, young king - i like your ambition')
    time.sleep(2)
    print(r'''

    Depression: 9/10
    Humor: 3/10
    Strength: 3/10

    Modifier: *shrugs*

                                    ,-~ |
       ________________          o==]___|
      |                |            \ \
      |________________|            /\ \
 __  /  _,-----._      )           |  \ \.
|_||/_-~         `.   /()          |  /|]_|_____
  |//              \ |              \/ /_-~     ~-_
  //________________||              / //___________\
 //__|______________| \____________/ //___/-\ \~-_
((_________________/_-o___________/_//___/  /\,\  \
 |__/(  ((====)o===--~~                 (  ( (o/)  )
      \  ``==' /                         \  `--'  /
       `-.__,-'                           `-.__,-'


      ''')
#############################  game-play  ############################

while level_1_passed == False:
  if item_brezlin < 2 and riddle_solved == False and befriend_jess == False:
    print(' ')  #add level 1 here

  else:
