#this is for val - in case you forgets
#
#  created by UnderBreezy

import time
from os import system
import cmd
import textwrap
import sys
import os
import time
import random
# import pygame uncomment when installed

system('clear')




# handle item lists - list every item available and switch 0 to 1 when obtained
item_laptop = 0
item_SIPR_token = 0
item_SRB_bonus = 0
item_brezlin = 0
item_coffee = 0
item_SKL = 0
item_SIPR_admin = 0


# these are lists for start_screen()
food_list = ['brezlin','brez','pretzel','beer']
women_list = ['bitches','bitchez','pussy','whores','hookers','women','tiddies','titties']
look_in_the_mirror = ['mirror','look in the mirror', 'scrud']


# this is the start screen - select what to do
def start_screen():
	print('   ')
	print('   PLAY   --   EXIT  --  UPGRADE  --  GO FUCK YOURSELF  --  LOOK IN THE MIRROR, SCRUD')
	print('   ')
	first_selection = input('what you wanna do, player?   input: ').lower()
	if first_selection == 'play':
		brezlin()
	elif first_selection == 'exit':
		print('')
		print('aint even gonna try and play...quitter')
		print(' ')
		time.sleep(2)
		exit()
	elif first_selection == 'upgrade':
		print('   ')
		print('upgrade coming soon - current version: 0.1')
		print('   ')
		back_out = input('type "backout" to exit to main screen   ')
		if back_out.lower() == 'backout':
			start_screen()
		else:
			print('''im gonna exit anyways...stupid bitch
				''')
			time.sleep(2)
			start_screen()
	elif first_selection == 'go fuck youself':  #  this ends the game -- FIX
		print('')
		print('HAH GAE!')
		start_screen()
	elif first_selection in look_in_the_mirror:
		time.sleep(1)
		print('''

			                     ___       
			                     | /]       
			        _           _(_)       
			     ___))         [  | |___      
			      ) //o          | |     |  
			  _ (_    >         | |      ]    
			 (O)  |__<          | | ____/      
			 [/] /   )        [__|/_                          
			 [|]|  (  )        __/___|_____                    
			 [|]|   ( )__  ___|            |                   
			 [|]|    (___E/%%/|____________|_____              
			 [/]|=====__   (_____________________)             
			 [|] |_____ |    |                  |              
			 [/========| |   |                  |              
			 [|]     []| |   |                  |              
			 [/]     []| |_  |                  |              
			 [|]     []|___) |                  |             
			======================================
			''')
		time.sleep(1)
		start_screen()



# this is the start of the n6 game
''' in this level the player will be have to 
1. get 2 brezlin
2. solve one riddle 
3. befriend Jess through helping her drunk ass get home
	3a. as a reward player will get to see tiddies

	move levels to separate files and call them as needed
'''
def n6_game_level_1():
	print('')
	print('   L E V E L  O N E  B E G I N  I N  - 5 -  S E C O N D S\n')  #give a more clever title for level 1
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
  /' ._/   ".     --:--     ."   \\. '\
 |  .'|      ".  ---:---  ."      |'.  |
 |  : |       |  ---:---  |       | :  |
 \\ : |       |_____._____|       | : /
  /   (       |----|------|       )   \
 /... .|      |    |      |      |. ...\
|::::/'' jgs /     |       \\    ''\\::::|
'""""       /'    .L_      `\\       """"'
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
		Humor: 3/10
		Strength: 3/10

		Modifier: 

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
	elif name == 'youngking'
		print('young king, young king - i like your ambition')
		time.sleep(2)
		print(r'''


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
       `-.__,-'       Vespa P-200 E       `-.__,-'


			''')



	# include animations from https://github.com/peterbrittain/asciimatics/wiki



'''
def n6_game_level_2():
# this level should spawn a game play area 

#handle having enough brezlin to continue to next level
if item_brezlin >= X:
	n6_game_level_3:
else:
	print('you dont have enough brezlin')


'''

# this is the brezlin/bitches section
def brezlin():

	while 1 == 1:
		print('')
		print('')
		print('')
		is_brezlin = input("     what is the best?   answer: ").lower()

		if is_brezlin in food_list:
			time.sleep(1)
			print('')
			print('      you aint nevuh lied ')
			print('                           ')
			time.sleep(1)
			print('       good game, player')
			print('')
			time.sleep(1)
			print(r"""
               __       __
             .'  `'._.'`  '.
            |  .--;   ;--.  |
            |  (  /   \  )  |
             \  ;` /^\ `;  /
              :` .'._.'. `;
              '-`'.___.'`-'  is this all there is to life tho....or is there more........
		""")
		elif is_brezlin in women_list:
			print('well then heres a bitch for you...')
			time.sleep(2)
			print(r"""
                                              _..  
                                          .qd$$$$bp.
                                        .q$$$$$$$$$$m.
                                       .$$$$$$$$$$$$$$
                                     .q$$$$$$$$$$$$$$$$
                                    .$$$$$$$$$$$$P\$$$$;
                                  .q$$$$$$$$$P^"_.`;$$$$
                                 q$$$$$$$P;\   ,  /$$$$P
                               .$$$P^::Y$/`  _  .:.$$$/
                              .P.:..    \ `._.-:.. \$P
                              $':.  __.. :   :..    :'
                             /:_..::.   `. .:.    .'|
                           _::..          T:..   /  :
                        .::..             J:..  :  :
                     .::..          7:..   F:.. :  ;
                 _.::..             |:..   J:.. `./
            _..:::..               /J:..    F:.  : 
          .::::..                .T  \:..   J:.  /
         /:::...               .' `.  \:..   F_o'
        .:::...              .'     \  \:..  J ;
        ::::...           .-'`.    _.`._\:..  \'
        ':::...         .'  `._7.-'_.-  `\:.   \
         \:::...   _..-'__.._/_.--' ,:.   b:.   \._ 
          `::::..-"_.'-"_..--"      :..   /):.   `.\   
            `-:/"-7.--""            _::.-'P::..    \} 
 _....------""""""            _..--".-'    ::..     `. 
(::..              _...----""  _.-'       `---:..    `-.
 : :..      _.-' '   `""---""                 `::...___)
  `: ._.-"
""")
			break   
		elif is_brezlin == 'n6':
			is_n6 = input('   are you part of the N6 department? (yes/no)   answer: ').lower()
			if is_n6 == 'no':
				print('move along, outsider\n')
				time.sleep(2)
				start_screen()
			elif is_n6 == 'yes':
				print("\033[1;32;40m       \033 \n")
				print('    you have chosen the righteous path, fellow brezlin')
				print('      prepare yourself by taking this with you:\n')
				time.sleep(1.5)
				print('''


				   ._________________.
				   |.---------------.|
				   ||               ||
				   ||   -._ .-.     ||
				   ||   -._| | |    ||
				   ||   -._|"|"|    ||
				   ||   -._|.-.|    ||
				   ||_______________||  # this looks weird when executed
				   /.-.-.-.-.-.-.-.-.\
				  /.-.-.-.-.-.-.-.-.-.\
				 /.-.-.-.-.-.-.-.-.-.-.\
				/_____||__________||____|
				|_______________________|


						''')
				item_laptop = 1   
				n6_game_level_1()   # begin the n6 game here
		else:
			time.sleep(1.5)
			print('     ...wrong. try again, you gabagool mothafucka  ')
			print('')
			time.sleep(1.5)

start_screen()















































'''   ANSI Color codes for new colored text
print("\033[0;37;40m Normal text\n")
print("\033[2;37;40m Underlined text\033[0;37;40m \n")
print("\033[1;37;40m Bright Colour\033[0;37;40m \n")
print("\033[3;37;40m Negative Colour\033[0;37;40m \n")
print("\033[5;37;40m Negative Colour\033[0;37;40m\n")
 
print("\033[1;37;40m \033[2;37:40m TextColour BlackBackground          TextColour GreyBackground                WhiteText ColouredBackground\033[0;37;40m\n")
print("\033[1;30;40m Dark Gray      \033[0m 1;30;40m            \033[0;30;47m Black      \033[0m 0;30;47m               \033[0;37;41m Black      \033[0m 0;37;41m")
print("\033[1;31;40m Bright Red     \033[0m 1;31;40m            \033[0;31;47m Red        \033[0m 0;31;47m               \033[0;37;42m Black      \033[0m 0;37;42m")
print("\033[1;32;40m Bright Green   \033[0m 1;32;40m            \033[0;32;47m Green      \033[0m 0;32;47m               \033[0;37;43m Black      \033[0m 0;37;43m")
print("\033[1;33;40m Yellow         \033[0m 1;33;40m            \033[0;33;47m Brown      \033[0m 0;33;47m               \033[0;37;44m Black      \033[0m 0;37;44m")
print("\033[1;34;40m Bright Blue    \033[0m 1;34;40m            \033[0;34;47m Blue       \033[0m 0;34;47m               \033[0;37;45m Black      \033[0m 0;37;45m")
print("\033[1;35;40m Bright Magenta \033[0m 1;35;40m            \033[0;35;47m Magenta    \033[0m 0;35;47m               \033[0;37;46m Black      \033[0m 0;37;46m")
print("\033[1;36;40m Bright Cyan    \033[0m 1;36;40m            \033[0;36;47m Cyan       \033[0m 0;36;47m               \033[0;37;47m Black      \033[0m 0;37;47m")
print("\033[1;37;40m White          \033[0m 1;37;40m            \033[0;37;40m Light Grey \033[0m 0;37;40m               \033[0;37;48m Black      \033[0m 0;37;48m")
 
\n")
'''
