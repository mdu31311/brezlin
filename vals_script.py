#this is for val - in case you forgets
#
#  created by UnderBreezy

import time
from os import system

system('clear')

food_list = ['brezlin','brez','pretzel','beer']
women_list = ['bitches','bitchez','pussy','whores','hookers','women','tiddies','titties']


# this is the start screen - select what to do
def start_screen():
	print('   ')
	print('   PLAY   --   EXIT  --  UPGRADE  --  GO FUCK YOURSELF  ')
	print('   ')
	first_selection = input('what you wanna do, player?   ').lower()
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
'''	elif first_selection == 'go fuck youself':
		print('')
		print('HAH GAE!')
		start_screen()
'''
#add to this later




# this is the brezlin/bitches section
def brezlin():

	while 1 == 1:
		print('')
		print('')
		print('')
		is_brezlin = input("     system: what is the best?    val:  ").lower()

		if is_brezlin in food_list:
			time.sleep(1)
			print('')
			print('      system: you aint nevuh lied ')
			print('                           ')
			time.sleep(1)
			print('       system: good game, player')
			print('')
			time.sleep(1)
			print(r"""\
	                       __       __
	                     .'  `'._.'`  '.
	                    |  .--;   ;--.  |
	                    |  (  /   \  )  |
	                     \  ;` /^\ `;  /
	                      :` .'._.'. `;
	                      '-`'.___.'`-'
				""")
			break
		elif is_brezlin in women_list:
			print('well then heres a bitch for you...')
			time.sleep(5)
			print(r"""\

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
 _....------""""""            _..--".-'   \::..     `. 
(::..              _...----"""  _.-'       `---:..    `-.
 \::..      _.-' '   `""---""                `::...___)
  `\:._.-"                             
			""")
			break   
		else:
			time.sleep(3)
			print('     ...wrong. try again, you gabagool mothafucka  ')
			print('')
			time.sleep(2)

start_screen()