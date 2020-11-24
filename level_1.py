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
import level_2
#### asciimatics
from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText


# all variables must be fulfilled to pass level
level_1_passed = False 

item_brezlin = 0
riddle_solved = False
befriend_jess = False

name = 'unassigned'

def n6_game_level_1():
  print('')
  print('   L E V E L  O N E  B E G I N  I N  - 5 -  S E C O N D S\n')
  time.sleep(5)
  system('clear')
  name = input('pick your communicator:  PAPI  F.Daddy  UBreezy  GLITCH  YoungKing     answer:  ').lower()
  if name == 'papi':
    item_brezlin = 0
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
        .    `.-===-\\   /-===-.`   .
       /      .-`````-.-````-.      \
      /              =:=              \
    .`  ` .:    o   -=:=-   o    :. `  `.
    (.`   /'. `-.....-`-.....-` .'\\  `.)
    /  ._/   `.     --:--     .`   \\.  \
   |  .`|      `.  ---:---  .`      |`.  |
   |  : |       |  ---:---  |       | :  |
   \\ : |       |_____._____|       | : /
    /   (       |----|------|       )   \
   /... .|      |    |      |      |. ...\
  |::::/``     /     |       \\    ``\\::::|
  `````       /`    .L_      `\\       `````
             /`-.,__/` `\\__..-`\
            ;      /     \\      ;

      """)
  elif name == 'f.daddy':
    item_brezlin = 0
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
    item_brezlin = 0
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
    item_brezlin = 0
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
                         `?$$$$F      ''')
  elif name == 'youngking':
    item_brezlin = 0
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
  selected_names = ['papi','f.daddy','ubreezy','glitch','youngking']
  if name in selected_names:
    print('your character is ' + name.upper())
    time.sleep(3)
    input('''Press ENTER to continue...
            or any key, i dont know how this program works.
      ''')
    n6_game_level_1a()

#############################  game-play  ############################


def n6_game_level_1a():
  while level_1_passed == False:
    if item_brezlin < 2 and riddle_solved == False and befriend_jess == False:
      print('')  #add level 1 here
      system('clear')
      print(r'''
  ______
 /|_||_\\.__
(   _    _ _\
=`-(_)--(_)-'  
      ''')
      time.sleep(.5)
      system('clear')
      print(r'''
      ______
     /|_||_\\.__
    (   _    _ _\
    =`-(_)--(_)-' 
        ''')
      time.sleep(.5)
      system('clear')
      print(r'''
          ______
         /|_||_\\.__
        (   _    _ _\
        =`-(_)--(_)-' 
        ''')
      time.sleep(.5)
      system('clear')
      print(r'''
              ______
             /|_||_\\.__
            (   _    _ _\
            =`-(_)--(_)-' 
          ''')
      time.sleep(.5)
      system('clear')
      print(r'''
                  ______
                 /|_||_\\.__
                (   _    _ _\
                =`-(_)--(_)-' 
              ''')
      time.sleep(.5)
      system('clear')
      print(r'''
                      ______
                     /|_||_\\.__
                    (   _    _ _\
                    =`-(_)--(_)-' 
                  ''')
      time.sleep(.5)
      system('clear')
      print(r'''
                          ______
                         /|_||_\\.__
                        (   _    _ _\
                        =`-(_)--(_)-' 
        ''')
      time.sleep(.5)
      system('clear')
      print(r'''
                              ______
                             /|_||_\\.__
                            (   _    _ _\
                            =`-(_)--(_)-' 
        ''')
      time.sleep(.5)
      system('clear')
      print(r'''
                                  ______
                                 /|_||_\\.__
                                (   _    _ _\
                                =`-(_)--(_)-' 
          ''')
    level_1_prompt()

def befriend_jess_play():
  system('clear')
  time.sleep(2)
  ## drinking animation here
  ## introduce Jess
  print(r'''Everybody is getting litty spaghetti
            ~  ~
      ( o )o)
     ( o )o )o)
   (o( ~~~~~~~~o
   ( )' ~~~~~~~'
   ( )|)       |-.
     o|     _  |-. \
     o| |_||_) |  \ \
      | | ||_) |   | |
     o|        |  / /
      |        |." "
      |        |- '
      .========.      ..............especially your JOC LPO... ''')
  time.sleep(3)
  give_jess_drinks = input(r'''
 /////////////\\\\
(((((((((((((( \\\\ -HEY N6! GIVE ME A DRINK!
))) ~~      ~~  (((
((( (*)     (*) )))
)))     <       (((
((( ' ______/`  )))
))) ___________/(((
       _) (_
      /  _/ \
     /(     )\
    // )___( \\
    \\(     )//          
     (       )
      |  |  |             Jess is stumbling. She is not handling her liquor well.
       | | |                And that dip she has in is making her dizzy.
       | | |                    Do you give her a drink, or walk her home?
      _|_|_|_                          (type 'home' -or- 'drink')
                                    answer:    ''').lower()
  if give_jess_drinks == 'home':
    time.sleep(2)
    print('')
    print('you are a responsible communicator. congratulations.')
    time.sleep(2)
    print('you have made a new friend.')
    befriend_jess == True
    time.sleep(3)
    system('clear')
    print('''


              CONGRATULATIONS, FELLOW COMMUNICATOR!
                YOU HAVE COMPLETED LEVEL 1!


      ''')
    input('press enter to continue to level 2')
    level_2.n6_game_level_2(screen)
  elif give_jess_drinks == 'drink':
    time.sleep(2)
    print(r'''
            __          MORE DRINKS IT IS!
           )==(           LITTY TITTY!
           )==(
           |H |
           |H |
           |H |
          /====\
         / Dr S \
        /========\
       :HHHHHHHH H:
       |HHHHHHHH H|
       |HHHHHHHH H|
       |HHHHHHHH H|
\______|=/========\________/
 \     :/oO/      |\      /
  \    / oOOO  Le | \    /
   \__/| OOO Grape|  \__/
    )( |  O       |   )(
    )( |==========|   )(
    )( |HHHHHHHH H|   )(
    )( |HHHHHHHH H|   )(
   .)(.|HHHHHHHH H|  .)(.
  ~~~~~~~~~~~~~~~~  ~~~~~~
  ''')
    time.sleep(2)
    print('Jess is now so drunk you have no idea what shes saying.')
    time.sleep(1)
    print('You decide to carry her home')
    time.sleep(5)
    print('You\'re getting her some water when you turn around and see...')
    time.sleep(3)
    system('clear')
    print(r'''
|mMMMMMMMMMMMm  mM                                                                                   |
|MMMMMMMMMMMMMMMmMM                        _,--'`-._         __                                      |
|MMMMMMMMMMMMMMMMMMm-.-._               ,-'   `""'  `-.---,'"  "`-.                                  |
|MP\_,  ",",""""YMMMMMm._\  ,._,   __ ,'           .:_,`'          `.                                |
|M\__,-'| /|      `YMMMMMMMMMMMMP,""."`-._  ...._,-='               ;                                |
|m\__.. ' `' _..  . `YMMMMMMMP'_.,-'      `. _,'.::.              ,'                                 |
|\_`--'        ' //|  \  `"-/"'         .:_,'           _____.,--<                                   |
|m `   / , `::, ;( )  :)::,'           .,'          ,-"' __.,--'--._.                                |
|MMm  | |/      \|/:.:/;;'           _,' ,          ;_,-'          -`-._                             |
|MMMm.` '        ._,-'"  .:        ,' _,/          //               `-. `-.                          |
|MMMMMMMm    .::,'        `:.      `"','          //      .::        `-. `-`-,                       |
|MMMMM""""""---/         .           /  ,  ,     //      .;"""`-----=.._`-._,'.                      |
|              |          :.        / ,'/ /; /  /"      .':      ..     `-.,'  `-._                  |
|              |            `.     / / / // // /       ;'          ::..            `-.               |
|              :              `:  '-' / // // /       /               ::.             `.             |
|               \               \::. (_/(_; y'       /                             _.   `._          |
|                \               \;;:._    /        /                  . .:      "YMMm     `---..__  |
|                 \              `.    "",'        /;                              YMMMm           ``|
|                  `.              :.  ,'         /"\                          `::. "MMMI;:.         |
|                    `.            ::;'          /   \                           `:  YMM;|::         |
|                      `.           '           /     \       .                    `. |:;f:          |
|                        `.                    /       \                             `|:j;           |
|                          `.                 /         \     .                        `;::.         |
|                            `-.             /           \    .                          `::.        |
|                               `-.        ,'             \ .                              \::       |
|                                  `-._  ,'                `.  .                            `::.     |
|                                      ""                    \                                \::.   |
|                                                             `.                               `::   |
|                                                               `._                              \`"-|
|                                                                  `-.____________________________\  |

      ''')
    input('Take a moment to see some LPO tiddy. Press \'enter\' when you want to continue.')
    system('clear')
    print('''


              CONGRATULATIONS, FELLOW COMMUNICATOR!
                YOU HAVE COMPLETED LEVEL 1!


      ''')
    input('press enter to continue to level 2')
    level2.n6_game_level_2(screen)




def next_part_of_game():
  print('You\'ve made it far, young brezlin.')
  time.sleep(1)
  print('Now it\'s time to flex your muscles.')
  time.sleep(1)
  print('The ones...BETWEEN YOUR EARS.')
  time.sleep(5)
  system('clear')
  print('''
    To pass the next test, you must answer 3 riddles correctly. They will not be simple...
    Let us see if you have spent enough time in the dreaded EUCOM AOR yet...
    ''')
  time.sleep(4)
  answer_riddle_1 = input('''  Riddle number ONE:

    what is Young yet old,
      of pickled liver,
        stinks of wet tobacco,
          it\'s name gives all a shiver?
                                  answer (one word):                   ''').lower()
  if answer_riddle_1 in ['youngers','matt youngers','chief youngers']:
    time.sleep(2)
    print('')
    print('Much too easy - let us try something a little harder...')
    time.sleep(2)
    answer_riddle_2 = input('''   Riddle number TWO;

    so cold and so sad,
      you may have a reason.
        to this place you\'ll travel,
          for the holiday season.
                                  answer (one word):                  ''').lower()
    if answer_riddle_2 in ['nowhere','here','stuttgart','barracks']:
      time.sleep(2)
      print('')
      print('Impressive, mein brezlin. One more riddle and you pass this stage.')
      time.sleep(2)
      answer_riddle_3 = input('''     Riddle number THREE:

      right hand raised high,
        an oath of 6 years.
          a mistake there\'s no doubt,
            only remedy is 9 or 10 ______.
                                    answer (one word):                 ''').lower()
      if answer_riddle_3 in ['beers','beer']:
        time.sleep(2)
        print('')
        print('Most excellent! You have passed this test!')
        time.sleep(2)
        print('It\'s now 1900 and you are leaving the base now...')
        print('')
        time.sleep(2)
        print('You will soon be home...')
        time.sleep(5)
        befriend_jess_play()
      else:
        time.sleep(2)
        print('NO! Perhaps you need more time in the JOC! Try again in -5- seconds')
        time.sleep(5)
        next_part_of_game()
    else:
      time.sleep(2)
      print('NO! Perhaps you need more time in the JOC! Try again in -5- seconds')
      time.sleep(5)
      next_part_of_game()

  else:
    time.sleep(2)
    print('NO! Perhaps you need more time in the JOC! Try again in -5- seconds')
    time.sleep(5)
    next_part_of_game()




possible_answers_to_1 = ['brezlin','get brezlin','pretzel','pretzels','brez','brekkie','breakfast']

def level_1_prompt():
  item_brezlin = 1
  print('  it\'s 5 am - still dark outside...')
  time.sleep(1)
  print('   you\'re almost at work.')     
  time.sleep(1)
  print('     before you get to work, theres still one more thing you need.')
  time.sleep(1)
  print('      ...what is it?')
  answer_to_1 = input('  answer: ').lower()

  if answer_to_1 in possible_answers_to_1:
    print('')
    print(' excellent, mein brezlin. you are learning quickly')
    time.sleep(1)
    print(' take this brezlin with you, youll need it.')
    time.sleep(1)
    print(r'''
               __       __
             .'  `'._.'`  '.
            |  .--;   ;--.  |
            |  (  /   \  )  |
             \  ;` /^\ `;  /
              :` .'._.'. `;
              '-`'.___.'`-' 
      ''')
    time.sleep(.5)
    item_brezlin += 1
    print('     Brezlin count: ', item_brezlin )
    time.sleep(5)
    print('')
    print('....lets continue your shitty day.')
    print('its almost 1300...time for the dreaded DAILY UPDATE BRIEF')
    attend_dub = input('           do you go? (yes/no)       answer:  ').lower()
    if attend_dub == 'yes':
      print('')
      print('   you have chosen......')
      time.sleep(2)
      print('CORRECTLY')
      time.sleep(1)
      next_part_of_game()
    elif attend_dub == 'no':
      print('')
      print('   you are a brave muhfucka...')
      time.sleep(1)
      print('   but your choices have forced you to skip lunch.')
      time.sleep(3)
      next_part_of_game()    
  elif answer_to_1 not in possible_answers_to_1:
    print('')
    print('     incorrect, try again tomorrow (in 5 seconds).')
    time.sleep(5)
    system('clear')
    level_1_prompt()




