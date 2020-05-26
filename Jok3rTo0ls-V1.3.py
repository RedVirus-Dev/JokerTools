                ##############$ BY:. $#################
#                      ~=>> Red_Vairus6 <<=~                     #
                ############## $ V1.3 $################

##############& Imported Modules

from os import system, path #####R
from time import sleep ######ed
from base64 import *   ########Vairus6
from webbrowser import open_new_tab as tab

##########################
#Tool Style
##########################
gr, r, g, y, b, p, c, w=[
'\033[1;30m',
'\033[1;31m',
'\033[1;32m',
'\033[1;33m',
'\033[1;34m',
'\033[1;35m',
'\033[1;36m',
'\033[1;37m' ]
    
def color(text):
    col = [gr, r, g, y, b, p ,c, w]
    text= text.replace('GR@',col[0])
    text= text.replace('R@',col[1])
    text= text.replace('G@',col[2])
    text= text.replace('Y@',col[3])
    text= text.replace('B@',col[4])
    text= text.replace('P@',col[5])
    text= text.replace('C@',col[6])
    text= text.replace('W@',col[7])
    return text
       
######################
#MetaSploit Starting Chr
#######################         
def cptl(text):
    
    for n in range(0,3):
        c = len(text)
        for z in range(0, c):
            f = ("R@" + text[:z].lower() + "G@" + text[z].upper())
            print(color(f),end="\r")
            sleep(.2)
        
#cptl('starting joker tools ')

######################
#Loadbar | ####
#######################
def loadbar():
    print(" ")
    for l in range(0, 8):
        z="#"
        x=z*l
        print(color(" G@Loading C@| B@" + x + ">"),end="\r")
        sleep(.5)

######################
#Banners         #1 Meta Banner
#######################
def meta_bnr():
	#from ToolStyle import color
    print(color("R@+++++++++++++++++++++++++++++++++++++++++++++++++++++++++"))
    sleep(.1)
    print(color("+Y@      _       _   C@V1.3      ____        _       _ _    R@+"))
    sleep(.1)
    print(color("+G@     | | ___ | | _____ _ __/ ___| _ __ | | ___ (_) |_  R@+"))
    sleep(.1)
    print(color("+C@  _  | |/ _ \| |/ / _ \ '__\___ \| '_ \| |/ _ \| | __| R@+"))
    sleep(.1)
    print(color("+B@ | |_| | (_) |   <  __/ |   ___) | |_) | | (_) | | |_  R@+"))
    sleep(.1)
    print(color("+R@  \___/ \___/|_|\_\___|_|  |____/| .__/|_|\___/|_|\__| R@+"))
    sleep(.1)
    print(color("+W@                                 |_|                   R@+  "))
    sleep(.1)
    print(color("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++"))
    print(" ")

###########  Tool Banner
def tool_bnr():
    print(color(" W@+++++++++++++++++++++++++++++++++++++++++++++++++++++++"))
    sleep(.1)
    print(color(" +G@      _       _       W@V1.3G@    _____           _      W@+"))
    sleep(.1)
    print(color(" +Y@     | | ___ | | _____ _ __  |_   _|__   ___ | |___  W@+"))
    sleep(.1)
    print(color(" +C@  _  | |/ _ \| |/ / _ \ '__|   | |/ _ \ / _ \| / __| W@+"))
    sleep(.1)
    print(color(" +B@ | |_| | (_) |   <  __/ |      | | (_) | (_) | \__ \ W@+"))
    sleep(.1)
    print(color(" +R@  \___/ \___/|_|\_\___|_|      |_|\___/ \___/|_|___/ W@+"))
    sleep(.1)
    print(color(" +++++++++++++++++++++++++++++++++++++++++++++++++++++++"))
    print(" ")


#############  Ternux Banner
def linux_bnr():
    print(color("       C@+++++++++++++++++++++++++++++++++++++"))
    sleep(.1)
    print(color("       +B@  _____                   C@V1.3     C@+"))
    sleep(.1)
    print(color("       +R@ |_   _|__ _ __ _ __  _   ___  __  C@+"))
    sleep(.1)
    print(color("       +G@   | |/ _ \ '__| '_ \| | | \ \/ /  C@+"))
    sleep(.1)
    print(color("       +Y@   | |  __/ |  | | | | |_| |>  <   C@+"))
    sleep(.1)
    print(color("       +W@   |_|\___|_|  |_| |_|\__,_/_/\_\  C@+"))
    sleep(.1)
    print(color("       +++++++++++++++++++++++++++++++++++++"))
    print(" ")


##############Dark Encode Banner
def hash_bnr():
    print(color("G@++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"))
    sleep(.1)
    print(color("+R@  ____             _      _____         G@V1.3R@        _     G@  +"))
    sleep(.1)
    print(color("+Y@ |  _ \  __ _ _ __| | __ | ____|_ __   ___ ___   __| | ___  G@+"))
    sleep(.1)
    print(color("+B@ | | | |/ _` | '__| |/ / |  _| | '_ \ / __/ _ \ / _` |/ _ \ G@+"))
    sleep(.1)
    print(color("+C@ | |_| | (_| | |  |   <  | |___| | | | (_| (_) | (_| |  __/ G@+"))
    sleep(.1)
    print(color("+W@ |____/ \__,_|_|  |_|\_\ |_____|_| |_|\___\___/ \__,_|\___| G@+"))
    sleep(.1)
    print(color("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"))
    print(" ")
             
    
############  Websites Banner  
def sites_bnr():
    print(color("  Y@++++++++++++++++++++++++++++++++++++++++++++++++++"))
    sleep(.1)
    print(color("  +    G@      Y@V1.3G@     _         _ _                Y@+"))
    sleep(.1)
    print(color("  +    C@ __      _____| |__  ___(_) |_ ___  ___     Y@+"))
    sleep(.1)
    print(color("  +    B@ \ \ /\ / / _ \ '_ \/ __| | __/ _ \/ __|   Y@ +"))
    sleep(.1)
    print(color("  +    R@  \ V  V /  __/ |_) \__ \ | ||  __/\__ \\   Y@ +"))
    sleep(.1)
    print(color("  +    W@   \_/\_/ \___|_.__/|___/_|\__\___||___/   Y@ +"))
    sleep(.1)    
    print("  ++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(" ")

#################   Drawer Banner
def Art_bnr():
	print(color("         W@+R@~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~W@+"))
	print(color("         W@| G@V1.3 B@_      R@____   Y@ _____  R@__   __   W@|"))
	print(color("         R@|     C@/ \    G@|  _ \  G@|_   _| B@\ \ / /   R@|"))
	print(color("         W@|    Y@/ _ \   Y@| |_) |   R@| |    C@\ V /    W@|"))
	print(color("         R@|   G@/ ___ \  C@|  _ <    B@| |     Y@| |     R@|"))
	print(color("         W@|  R@/_/   \_\ B@|_| \ \   C@|_|     G@|_|     W@|"))
	print(color("         R@|  G@_______________\ \________________  R@|"))
	print(color("         W@| G@|__________________________________| W@|"))
	print(color("         R@+W@~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~R@+"))


######################
# Joker Banner
######################
def joker_banner():
	print(color("W@mNNNNNNNNNNNMMMNNmo/:B@---W@/dNNNNNmdddmhs+-G@``````        ```"))
	sleep(.2)                   
	print(color("W@NNNNNNNMNNNNNNNNhs+:B@-----W@/yNNNNNNmddmds/G@.``.```        `````"))
	sleep(.2)               
	print(color("W@mNNNNNNNNNNNNNNNs--B@..----:W@+dMMMMNNmdmmh+.G@``..```     ` ````"))
	sleep(.2)         
	print(color("W@mmmmmmmmmNNNNNmNy-B@.....--:/W@hNNNMMMNmmmds-G@``..```"))       
	sleep(.2)           
	print(color("W@dddddhhddddmdddh-B@........./sW@hNNNNMMNNmdy/.G@```.````````  ")) 
	sleep(.2)              
	print(color("W@yhhhhooyysyyhyo/B@-...```...-./+W@ydNNMNNmdh+.G@````...`````"))  
	sleep(.2)             
	print(color("W@yyysy++osssso//B@:-....`...-..::/W@sshhdmNmdo.G@``````-::-.-:.`"))  
	sleep(.2)               
	print(color("W@sssso/:::////---::-.-.::/:::/:///++ohdmmy:.G@``  `.-:/:///-```")) 
	sleep(.2)         
	print(color("W@ooos+/-.--::---:://///:///:---:---:/ohmNd+.G@.`   ```.:/:-::-`")) 
	sleep(.2)      
	print(color("W@ooo+/::----:::::::---..-----..-::::/ohNNmy:.G@``````   `......``"))  
	sleep(.2)  
	print(color("W@osso+/:----:-..`....``..--::::--://+ohmNNm+-...-`` `  G@``-.")) 
	sleep(.2) 
	print(color("W@yyys+/-.``..```....` `.-.---...::/+oyhmNNNh-...--```  G@``.-.```.`")) 
	sleep(.2)       
	print(color("W@hdddyo-...``````.........----::+ooyydmNNNMm/```.-``     G@`..-```"))  
	sleep(.2)      
	print(color("W@mmNmmh/--:-``````...-----:::+syhdhhdmNNNNNNo.``.-.      G@`....``")) 
	sleep(.2)     
	print(color("W@NNNNNmy//:-B@-````````......../W@syyhhhdmmNNNNmo.``-:.`    G@ `.``-")) 
	sleep(.2)          
	print(color("W@NNNNMMmso+/:.B@````````````.-/W@oshyhhddmmNNNNm+.``./.    G@ ````..```"))
	sleep(.2)    
	print(color("W@NNNNMMNdyoo++:.B@.````````.-:W@+osyhdmmmmmmmmmd:..`.-.     G@``````"))  
	sleep(.2)         
	print(color("W@MMMMMMMmdyosooo/B@--.````.-/W@osyyhdddmNmmddddh-.``.-`     G@`.```")) 
	sleep(.2)           
	print(color("W@MMMMMMMNmdyyyssys/B@---.-+W@/syhddddmmmmdddhhhs--.-/:`      G@` `"))  
	sleep(.2)             
	print(color("W@MMMMMMMMNmddddddhso-B@..-W@oyhddhhhhddddhhhyhho.:/+s:``` G@  ` `"))  
	sleep(.2)              
	print(color("W@NdddmMMMNmdhhdmmmmy/-B@..W@hddddddhyyhhhhhyyhh+-::+o-`.`  G@  ``"))  
	sleep(.2)              
	print(color("W@R@o///+shR@W@NMNmdyosyhmmy:-/hmmdhhhhyyyyyyyyyhd+G@/--.-/.  `'")) 
	sleep(.2)               
	print(color("W@R@oo+////+hR@W@NMMMdo+osyy/-smmdmdhyysyssyyyyyhh:G@-.``.-````    `"))  
	sleep(.2)              
	print(color("W@R@/+++//:::sR@W@NNNNy/://o//ymNmmddyysyysssyyhho`G@``````.-..    ``")) 
	sleep(.2)              
	print(color("W@R@-::-:::::/oR@W@/:+hs+:-:/ohmmNNmmdyyyssssyyyh+G@``  `-/-`-` `--.`"))  
	sleep(.2)         
	print(color("W@R@-.-.-----:--R@W@odmdhs+:/+sydmNNmdddhssssoyyh:G@` ``-//...-.:/.`")) 
	sleep(.2)           
	print(color("W@R@`.``..`..-:sR@W@dmmmmmhs++oyyhdmmdhhhso/R@:-W@shh-G@  `-+/.``-`..````  ``"))   
	sleep(.2)          
	print(color("W@R@.```````-+hR@W@dmmNNNmdhy++syyhddyss+/-R@../W@yhh`G@ ``..`   `` ``"))  
	sleep(.2)            
	print(color("W@R@--..--.-/sR@W@ddmmmmmmdyoss+syhhhs-R@--..-W@+sydyG@` ``` "))   
	sleep(.2)                 
	print(color("W@//::+o::ohhdhdmdddhhs+o+:oo+/R@:.`.-W@/ssyyd+  G@``   ```..`  `")) 
	sleep(.2)             
	print(color("W@:::+so/+osyyyyhyyyso/-R@..``.---.-W@:osssysh- G@ ```.``.-.`.```   ``"))
	sleep(.2)            
	print(color("R@........---:::--.-.......`..--:+W@syyyysss` G@`  ````.``....``")) 
	sleep(.2)               
	print(color("R@`.................```....`..-+W@ossssssss- G@`     `   `````````")) 
	sleep(.2)             
	print(color("R@``````````````....````......+W@soo+oooss:  G@`             `....``")) 
	sleep(.2)             
	print(color("W@...--::://///R@:--.--..```...:W@yoo+ooooo/` G@ `     `   `   `.````"))  
	sleep(.2)            
	print(color("R@...--::::----------...``.-/W@yso++o++o:`` G@ `       ``.`  `..`"))   
	sleep(.2)             
	print(color("R@``````.......------.....:W@+syssoo+o+-`G@           `````  `.``"))  
	sleep(.2)              
	print(color("R@`````````....----....-W@/+oyhsoooo+/.` G@          .``     ````"))  
	sleep(.2)              
	print(color("R@```````.....------::W@+sssyhhysys+/G@``` `        ``"))    
	sleep(.2)             
	print(color("R@```````.......-::/W@/sdhhyhdhyyo+/-G@``         ```")) 
	sleep(.2)                
	print(color("R@.....---::-::::/W@+ohdmmddddhso+/:.G@``          `  ```"))  
	sleep(.2)                
	print(color("R@.--:://++////+W@osshmmmmmdyos+//:G@:```          ````"))  
	sleep(.2)                  
	print(color("R@-.----:::://W@oyhmNmmmmdhy+/////:G@-`````         ``"))  
	sleep(.2)                  
	print(color("R@------::/W@+oosmmNNNmdhyo/:////:-G@.``````        `````")) 
	sleep(.2)
	print(color("R@++/:://W@+oyhddNmNNNmho/:::////:-G@` ```````       ```` `")) 
	sleep(.2)  
	print(color("W@ssssssyyhdhyhhdddhs+:::///:/::G@.`  ```````     `...`.```"))   
	sleep(.2)  
	print(color("W@sssssysooo+ossyso//::////::/:-G@``   `````````````...``.`..")) 
	sleep(.2)   
	print(color("W@/++++///////////:////:/::///:G@-``     ``..`````````` `")) 
	sleep(.2)
	print(color("W@::://://::::::://+///:::////:R@.``  ``  ``...``````"))
	sleep(.2)
	print(color("W@---..------:://+///:::://///-R@`````````  ````````"))
	sleep(.2)
	print(color("W@.......----:::/+//:::::/+//-`R@.` ````````` ```````"))
	sleep(.2)
	print(color("W@.........---::/::-:::::///-`.`R@````..````````` ````."))
	sleep(.2)
	print(color("W@..........-----:----::::-.`..R@` ```...``````````````..----.."))
	sleep(.2)
	print(color("R@W@.........----..----R@-.``..``````....`````..-......-.--:::::--")) 
	sleep(.2)     
	print(color("R@``W@`.....`............R@..``.-.` ```........------...-.-..-:-:::"))    
	sleep(.2)
	print(color("R@```````````..........```.-.` ````............---.```````..------::"))
	sleep(.2)
	print(color("R@````````````````````````..`` ````..............---.```````...----::"))
	sleep(.2)
	print(color("R@``````````````````````...``  ```...............----.````````....---:"))
	sleep(.2)
	print(color("R@`````````````````````.-..`  `````..............------.````````...----:"))
	sleep(.2)
	print(color("R@````````````````````...``   ````................--::---.```````...----:"))
	print("\n\n")



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                                   
#######################restart()
def restart():
    system('clear')
    tool_bnr()
    print("     \033[1;33mWelcome Back >_* ..")
    Main_page()
         
######################
#.
#######################
def con_termux():
    print('\n\n')
    print(color("            \033[1;33m+#####################+"))
    sleep(.1)
    print(color("            +[\033[1;32m99\033[1;33m] \033[1;37mMain Menu     \033[1;33m  +"))
    sleep(.1)
    print(color("            +>[\033[1;32m00\033[1;33m] \033[1;31mExit          \033[1;33m +"))
    sleep(.1)
    print(color("            +##########+##########+"))
    sleep(.1)
    print(color("             +#########+"))
    sleep(.1)
    
    con = int(input(color("             +####>$\ \033[1;32m")))
    
    if con ==99:
       	restart()        
                    
    elif con ==00:
    	print(" ")
    	for s in range(0, 3):
    		print(color(" Y@[R@!Y@]R@ E x i t i n g ..G@/"),end="\r")
    		sleep(.2)
    		print(color(" Y@[R@!Y@]R@ E x i t i n g ..G@-"),end="\r")
    		sleep(.2)
    		print(color(" Y@[R@!Y@]R@ E x i t i n g ..G@\\"),end="\r")
    		sleep(.2)
    	system('reset')
    	exit()

    
    else:
        for r in range(0,4):
	            print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. R@x"),end='\r')
	            sleep(.5)
	            print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. R@X"),end="\r")
	            sleep(.5)
        system('clear')
        con_termux()
                  
######################
#part1
#######################   
def up_termux():
	system("clear")
	tool_bnr()
	if OS ==1:
		print("\n>> [*] Commands Runs With Sudo Mode To Continue..")
		#print(color("\nW@[!]R@ Please Enter Your Password To Continue Upgrade.."))
		sleep(3)
		system('sudo apt-get update -y')
		print('\n\033[1;37mUpdated successfully √')
		print(' ')
		sleep(2)
		system('sudo apt-get upgrade -y')
		print('\n\033[1;31mUpgraded Successfully √')
		sleep(3)
		system("sudo apt-get install git -y -y")
		system("sudo apt-get install perl -y")
		system("sudo apt-get install nano -y")
		system('sudo apt-get install cowsay -y')
		system('sudo apt-get install ruby -y')
		system('sudo apt-get install curl -y')
		system('sudo apt-get install wget -y')
		system('sudo apt-get install requests -y')
		system('clear')
		tool_bnr()
		print(color('\nG@System Updated And Fixed Proplems Successfully √'))
		print(color("\n#### C@Tool Restarting After 4s .."))
		sleep(4)
		system('clear')
		restart()

	elif OS==2:
		system("pkg update -y")
		print('\n\033[1;37mUpdated successfully √')
		print(' ')
		sleep(2)
		system("pkg upgrade -y")
		print('\n\033[1;31mUpgraded Successfully √')
		sleep(2)
		system("pkg install git -y -y")
		system("pkg install perl -y")
		system("pkg install nano -y")
		system('pkg install cowsay -y')
		system('pkg install ruby -y')
		system('pkg install curl -y')
		system('pkg install wget -y')
		system('pkg install requests -y')
		system('clear')
		tool_bnr()
		print(color('\nG@Termux Updated And Fixed Proplems Successfully √'))
		print(color("\n#### C@Tool Restarting After 4s .."))
		sleep(4)
		system('clear')
		restart()


######################
#part2
####################### 
def Ttools():
	system("clear")
	tool_bnr()
	print(" \033[1;31m╔════════════════════════╦════════════════════════╗ ")
	print(" ╠[\033[1;36m1\033[1;31m] \033[1;33mInstall Zip & Unzip \033[1;31m╠[\033[1;36m2\033[1;31m] \033[1;33mLazymux \033[1;31m            ║")
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(" ╠[\033[1;36m3\033[1;31m] \033[1;33mTool-x  \033[1;31m            ╠[\033[1;36m4\033[1;31m] \033[1;33mSpammer-Grab\033[1;31m        ║")
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(" ╠[\033[1;36m5\033[1;31m]\033[1;33m Install Crunch \033[1;31m     ╠[\033[1;36m6\033[1;31m]\033[1;33m Wordpresscan  \033[1;31m      ║")
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(" ╠[\033[1;36m7\033[1;31m] \033[1;33m4nonimizer  \033[1;31m        ╠[\033[1;36m8\033[1;31m] \033[1;33mWifite  \033[1;31m            ║")
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(" ╠[\033[1;36m9\033[1;31m] \033[1;33mAutsystemixie   \033[1;31m    ╠[\033[1;36m10\033[1;31m]\033[1;33m Cewl\033[1;31m               ║")
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(" ╠[\033[1;36m11\033[1;31m] \033[1;33mJohnny \033[1;31m            ╠[\033[1;36m12\033[1;31m] \033[1;33mHunner \033[1;31m            ║")
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(" ╠[\033[1;36m13\033[1;31m] \033[1;33mNano \033[1;32m(Editor)  \033[1;31m    ╠[\033[1;36m14\033[1;31m] \033[1;33mAirCrack-ng \033[1;31m       ║")
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(" ╠[\033[1;36m15\033[1;31m] \033[1;33mWPScan \033[1;31m            ╠[\033[1;36m16\033[1;31m] \033[1;33mHydra  \033[1;31m            ║")
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(" ╠[\033[1;36m17\033[1;31m] \033[1;33mAndrospy \033[1;31m          ╠[\033[1;36m18\033[1;31m] \033[1;33mCurl     \033[1;31m          ║")
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(" ╠[\033[1;36m19\033[1;31m] \033[1;33mFsociety           \033[1;31m╠[\033[1;36m20\033[1;31m] \033[1;33mADB-Toolkit        \033[1;31m║")
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(" ╠[\033[1;36m21\033[1;31m] \033[1;33mWirless-Info       \033[1;31m╠[\033[1;36m22\033[1;31m] \033[1;33mHt-Wps-Breaker \033[1;31m    ║")
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(" ╠[\033[1;36m23\033[1;31m] \033[1;33mTrack My Location  \033[1;31m╠[\033[1;36m24\033[1;31m] \033[1;33mFluxion           \033[1;31m ║")
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(" ╠[\033[1;36m25\033[1;31m] \033[1;33mTermux Style \033[1;31m      ╠[\033[1;36m26\033[1;31m] \033[1;33mBeef               \033[1;31m║")
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(" ╠[\033[1;36m27\033[1;31m] \033[1;33mA-Rat  \033[1;31m            ╠[\033[1;36m28\033[1;31m] \033[1;33mDark Sploit\033[1;31m        ║")
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(" ╠[\033[1;36m29\033[1;31m] \033[1;33mReaver Wps \033[1;31m        ╠[\033[1;36m30\033[1;31m] \033[1;33m3vil Twin Attacker \033[1;31m║")
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(" ╠[\033[1;36m31\033[1;31m] \033[1;33mNgrok  \033[1;31m            ╠[\033[1;36m32\033[1;31m] \033[1;33mTermux Api \033[1;31m        ║")
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(" ╠[\033[1;36m33\033[1;31m] \033[1;33mWifi Scan  \033[1;31m        ╠[\033[1;36m34\033[1;31m] \033[1;33mEasy Hack  \033[1;31m        ║")
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(" ╠[\033[1;36m35\033[1;31m] \033[1;33mV7x Tool  \033[1;31m         ╠[\033[1;36m36\033[1;31m] \033[1;33mV7x Fishing  \033[1;31m      ║")
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@37R@] Y@Buildozer R@         ╠[C@38R@] Y@V7xStyle  R@         ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@39R@] Y@Figlet    R@         ╠[C@40R@] Y@Easymap        R@    ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@41R@] Y@InstaHack         R@ ╠[C@42R@] Y@Zarp  R@             ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@43R@] Y@HashCat           R@ ╠[C@44R@] Y@Hasher         R@    ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@45R@] Y@Medusa    R@         ╠[C@46R@] Y@Wfuzz          R@    ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@47R@] Y@Ettercap  R@         ╠[C@48R@] Y@PassGen        R@    ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@49R@] Y@AndroZenmap        R@╠[C@50R@] Y@Snitch         R@    ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@51R@] Y@AstraNmap          R@╠[C@52R@] Y@Devploit       R@    ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@53R@] Y@Xshell             R@╠[C@54R@] Y@Namechk        R@    ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@55R@] Y@Sqlscan            R@╠[C@56R@] Y@ddcrypt        R@    ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@57R@] Y@Torshammer         R@╠[C@58R@] Y@Black-Hydra    R@    ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@59R@] Y@Cupp               R@╠[C@60R@] Y@ASU            R@    ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@61R@] Y@Hash-Buster        R@╠[C@62R@] Y@Websploit      R@    ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@63R@] Y@Apktool            R@╠[C@64R@] Y@Brutal         R@    ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@65R@] Y@KnockMail          R@╠[C@66R@] Y@Hac            R@    ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@67R@] Y@Rang3r             R@╠[C@68R@] Y@SH33LL         R@    ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@69R@] Y@SpiderBot          R@╠[C@70R@] Y@Ecode          R@    ║"))
	print(color(" ╠════════════════════════╩════════════════════════╣"))
	print(color(" ║      G@}>>> Information Gathering Tools <<<{      R@║"))                      
	print(color(" ╠════════════════════════╦════════════════════════╣"))
	print(color(" ╠[C@71R@] Y@RED_HAWK           R@╠[C@72R@] Y@D-TECT          R@   ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@73R@] Y@TheChoice          R@╠[C@74R@] Y@Pureblood       R@   ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@75R@] Y@userrecon          R@╠[C@76R@] Y@ReconDog        R@   ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@77R@] Y@Infoga             R@╠[C@78R@] Y@Crips           R@   ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@79R@] Y@EvilURL            R@╠[C@80R@] Y@IPGeoLocation   R@   ║"))
	sleep(.1)
	print(color(" ╠════════════════════════╩════════════════════════╣"))
	print(color(" ║           B@}>>> DDos, Dos Attacks <<<{     R@      ║"))  
	sleep(.1)                    
	print(color(" ╠════════════════════════╦════════════════════════╣"))
	print(color(" ╠[C@81R@] Y@Hammer             R@╠[C@82R@] Y@DDos-Attack     R@   ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@83R@] Y@GoldenEye          R@╠[C@84R@] Y@Slowloris       R@   ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@85R@] Y@Xerxes             R@╠[C@86R@] Y@Hulk            R@   ║"))
	sleep(.1)
	print(color(" ╠════════════════════════╩════════════════════════╣"))
	print(color(" ║       C@ }>>> Social Engneering ToOls <<<{    R@    ║")) 
	sleep(.1)                     
	print(color(" ╠════════════════════════╦════════════════════════╣"))
	print(color(" ╠[C@87R@] Y@shellphish         R@╠[C@88R@] Y@weeman          R@   ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@89R@] Y@blackeye           R@╠[C@90R@] Y@SocialFish      R@   ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@91R@] Y@HiddenEye          R@╠[C@92R@] Y@SocialEngineer T.kR@ ║"))
	sleep(.1)
	print(color(" ╠════════════════════════╩════════════════════════╣"))
	print(color(" ║            W@}>>> Scanning ToOls <<<{      R@       ║")) 
	sleep(.1)                     
	print(color(" ╠════════════════════════╦════════════════════════╣"))
	print(color(" ╠[C@93R@] Y@OWScan             R@╠[C@94R@] Y@Nmap            R@   ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@95R@] Y@CMSmap             R@╠[C@96R@] Y@ClickJackingTester R@║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@97R@] Y@TM-scanner         R@╠[C@98R@] Y@AndroBugsFrameworkR@ ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@99R@] Y@Sqliscan           R@╠[C@100R@] Y@Commix         R@   ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@101R@] Y@WPSeku            R@╠[C@102R@] Y@RouterSploit   R@   ║"))
	sleep(.1)
	print(" ╠════════════════════════╬════════════════════════╣")
	print(color(" ╠[C@103R@] Y@Nikto             R@╠[C@104R@] Y@Credmap        R@   ║"))
	sleep(.1)	
	print(" ╚══════════════╦═════════╩═════════╦══════════════╝")
	print("                ║  \033[1;31m[\033[1;33m999\033[1;31m] \033[1;37mMain Menu  \033[1;31m║")
	sleep(.1)
	print("                ╚═════════╦═════════╝")
	print("                ╔═════════╩═════════╗")
	sleep(.1)
	print("                ║    \033[1;33m[\033[1;37m00\033[1;33m] \033[1;37mExit  \033[1;31m    ║")
	print("                ╚═════════╦═════════╝")
	sleep(.1)
	print(" ╔════════════════════════╝")

	tools =int(input(' ╚══[*] Enter Tool Number To install =>$\ \033[1;36m'))
	if tools ==1:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo sudo apt-get upgrade -y')
			system('sudo apt-get install zip')
			system('sudo apt-get install unzip')

		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install zip')
			system('pkg install unzip')
		print("")
		print('\n [*]\033[1;33mZip & \033[1;37mUnzip Tool \033[1;32mInstalled Successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools ==2:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo sudo apt-get upgrade -y')
			system('sudo sudo apt-get install git -y')

		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Gameye98/Lazymux.git')
		system('mv Lazymux ../')
		print('\n\033[1;31m[*] \033[1;33mLazyMux installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools ==3:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo sudo apt-get upgrade -y')
			system('sudo sudo apt-get install git -y')
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com\rajkumrdusad/Tool-X.git')
		system('mv Tool-X ../')
		print('\n\033[1;31m[*] \033[1;33m Tool-X installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools ==4:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo sudo apt-get upgrade -y')
			system('sudo sudo apt-get install git -y')

		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/WattanaGaming/Spammer-Grab-1.git')
		system('mv Spammer-Grab-1 ../')
		print('\n\033[1;31m[*] \033[1;33mSpammer-Grab installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools ==5:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo sudo apt-get upgrade -y')
			system('sudo apt-get install crunch')

		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install crunch')
		print('\n\033[1;31m[*] \033[1;33mCrunch installed successfully √ ')
		sleep(1)
		system('clear')
		Ttools()

	elif tools ==6:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo sudo apt-get upgrade -y')
			system('sudo sudo apt-get install git -y')

		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/swisskyrepo/Wordpresscan')
		system('mv Wordpresscan ../') 
		print('\n\033[1;31m[*]\033[1;33m Wordpresscan installed successfully √')
		sleep(1)
		system('clear')
		Ttools()
	
	elif tools ==7:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo sudo apt-get upgrade -y')
			system('sudo sudo apt-get install git -y')

		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Hackplayers/4nonimizer.git.git')
		system('mv 4nonimizer ../')
		print('\n\033[1;31m[*] \033[1;33m4nonimizer installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools ==8:
		if OS ==1:
			system("sudo apt-get update -y")
			system("sudo sudo apt-get upgrade -y")
			system('sudo sudo apt-get install git -y')

		elif OS ==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system("pkg install git -y")
		system('git clone https://github.com/derv82/wifite.git')
		system('mv wifite ../') 
		print('\n\033[1;31m[*]\033[1;33m Wifite installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools ==9:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo sudo apt-get upgrade -y')
			system('sudo sudo apt-get install git -y')

		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/nxxxu/AutsystemixieWps.git')
		system('mv AutsystemixieWps ../')
		print('\n\033[1;31m[*]\033[1;33m Autsystemixie installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools==10:
		if OS ==1:
			system('sudo apt-get update -y')
			system('sudo sudo apt-get upgrade -y')
			system('sudo sudo apt-get install git -y')

		elif OS ==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system("pkg install git -y")
		system('git clone https://github.com/digininja/CeWL.git')
		system('mv CeWL ../')
		print('\n\033[1;31m[*] \033[1;33mCewl installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools==11:
		if OS ==1:
			system('sudo apt-get update -y')
			system("sudo sudo apt-get upgrade -y")
			system('sudo sudo apt-get install git -y')

		elif OS ==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/shinnok/johnny.git')
		system('mv johnny ../')
		print('\n\033[1;31m[*] \033[1;33mJohnny installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools==12:
		if OS ==1:
			system('sudo apt-get update -y')
			system('sudo sudo apt-get upgrade -y')
			system('sudo sudo apt-get install git -y')

		elif OS ==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/b3-v3r/Hunner.git')
		system('mv Hunner ../')
		print('\n\033[1;31m[*] \033[1;33mHunner installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==13:
		if OS ==1:
			system('sudo apt-get update -y')
			system('sudo sudo apt-get upgrade -y')
			system('sudo apt-get install nano -y')

		elif OS ==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install nano -y')
		print('\n\033[1;31m[*] \033[1;33mNano installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools==14:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo sudo apt-get upgrade -y')
			system('sudo sudo apt-get install git -y')

		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/aircrack-ng/aircrack-ng.git')
		system('mv aircrack-ng ../')
		print('\n\033[1;31m[*] \033[1;33mAircrack-ng installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools==15:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo sudo apt-get upgrade -y')
			system('sudo sudo apt-get install git -y')

		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/wpscanteam/wpscan.git')
		system('mv wpscan ../')
		print('\n\033[1;31m[*] \033[1;33mWPScan installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools==16:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo sudo apt-get upgrade -y')
			system('sudo apt-get install hydra')

		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install hydra')
		print('\n\033[1;31m[*]\033[1;33m Hydra installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools==17: 
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo sudo apt-get upgrade -y')
			system('sudo sudo apt-get install git -y')

		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/TunisianEagles/Androspy.git')
		system('mv Androspy ../')
		print('\n\033[1;31m[*] \033[1;33mAndrospy installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools==18:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo sudo apt-get upgrade -y')
			system('sudo apt-get install curl')

		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install curl')
		print('\n\033[1;31m[*] \033[1;33mCurl installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools ==19:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo sudo apt-get upgrade -y')
			system('sudo sudo apt-get install git -y')

		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Manisso/fsociety.git')
		system('mv fsociety ../')
		print('\n\033[1;31m[*] \033[1;33mFSociety installed successfully √')
		sleep(1)
		system('clear')
		Ttools()
	elif tools==20:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo sudo apt-get upgrade -y')
			system('sudo sudo apt-get install git -y')

		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/ASHWIN990/ADB-Toolkit.git')
		system('mv ADB-Toolkit ../')
		print('\n\033[1;31m[*]\033[1;33m ADB-Toolkit installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools==21:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo sudo apt-get upgrade -y')
			system('sudo sudo apt-get install git -y')

		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/UbuntuForums/wireless-info.git')
		system('mv wireless-info ../')
		print('\n\033[1;31m[*] \033[1;33mWireless Info installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools==22:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo sudo apt-get upgrade -y')
			system('sudo sudo apt-get install git -y')

		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/SilentGhostX/HT-WPS-Breaker.git')
		system('mv HT-WPS-Breaker ../')
		print('\n\033[1;31m[*] \033[1;33mHt Wps Breaker installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools==23:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo sudo apt-get upgrade -y')
			system('sudo sudo apt-get install git -y')

		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/abdularis/Track-My-Location.git')
		system('mv Track-My-Location ../')
		print('\n\033[1;31m[*] \033[1;33mTrack My Location installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools==24:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo sudo apt-get upgrade -y')
			system('sudo sudo apt-get install git -y')

		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/wi-fi-analyzer/fluxion')
		system('mv fluxion ../')
		print('\n\033[1;31m[*]\033[1;33m Fluxion installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools==25:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')

		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/adi1090x/termux-style.git')
		print('\n\033[1;31m[*]\033[1;33m Termux Style installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools==26:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')

		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/beefproject/beef.git')
		system('mv beef ../')
		print('\n\033[1;31m[*]\033[1;33m Beef installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools==27:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')

		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Xi4u7/A-Rat.git')
		system('mv A-Rat ../')
		print('\n\033[1;31m[*]\033[1;33m A-Rat installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools==28:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')

		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/anthrax3/DarkSploit.git')
		system('mv DarkSploit ../')
		print('\n\033[1;31m[*]\033[1;33m Dark Sploit installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools==29:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')

		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/t6x/reaver-wps-fork-t6x.git')
		system('mv reaver-wps-fork-t6x ../')
		print('\n\033[1;31m[*] \033[1;33mRever Wps installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools==30:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')

		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/wi-fi-analyzer/3vilTwinAttacker')
		system('mv 3vilTwinAttacker ../')
		print('\n\033[1;31m[*] \033[1;33m3vil Twin Attacker installed successfully √')
		sleep(1)
		system('clear')
		Ttools()

	elif tools==31:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/inconshreveable/ngrok.git')
		system('mv ngrok ../')
		print('\n\033[1;31m[*] \033[1;33mNgrok installed successfully √')
		sleep(1)
		system('clear')
		Ttools()
		
	elif tools==32:
		system('pkg update -y')
		system('pkg upgrade -y')
		system('apt install termux-api')
		print('\n\033[1;31m[*] \033[1;33mTermux Api installed successfully √')
		sleep(1)
		system('clear')
		Ttools()
	
	elif tools==33:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/bmegli/wifi-scan.git')
		system('mv wifi-scan ../')
		print('\n\033[1;31m[*] \033[1;33mWifi Scan installed successfully √')
		sleep(1)
		system('clear')
		Ttools()
		
	elif tools==34:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/sabri-zaki/EasY_HaCk')
		system('mv EasY_HaCK ../')
		print('\n\033[1;31m[*]\033[1;33m Easy Hack installed successfully √')
		sleep(2)
		system('clear')
		Ttools()
	
	elif tools==35:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone 1-git clone https://github.com/Vairous7x/V7x-Tool')
		system('mv V7x-Tool ../')
		print('\n\033[1;31m[*]\033[1;33m V7x ToOl installed successfully √')
		sleep(2)
		system('clear')
		Ttools()
		
	elif tools==36:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Vairous7x/V7x-Fishing.git')
		system('mv V7x-Fishing ../')
		print('\n\033[1;31m[*]\033[1;33m V7x Fishing installed successfully √')
		sleep(2)
		system('clear')
		Ttools()
		
	elif tools==37:
		if OS ==1:		
			system('apt-get update -y')
			system('sudo apt-get upgrade -y')
			system("sudo apt-get install git -y")
		if OS==2:
			system("pkg update -y")
			system("pkg upgrade -y")
			system("pkg install git -y")
		system('pip install buildozer')
		system("git clone https://github.com/kivy/buildozer")
		system("cd buildozer && python setup.py build && pip install -e")
		print('\n\033[1;31m[*]\033[1;33m Buildozer installed successfully √')
		sleep(2)
		system('clear')
		Ttools()
		
	elif tools==38:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
		system('pip install V7xStyle')
		print('\n\033[1;31m[*]\033[1;33m V7x Style installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==39:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
			system("apt-get install figlet -y")
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
			system("pkg install figlet -y")
		print('\n\033[1;31m[*]\033[1;33m Figlet installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==40:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Cvar1984/Easymap')
		system('mv Easymap ../')
		print('\n\033[1;31m[*]\033[1;33m Easymap installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==41:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Slayeri4/instahack')
		system('mv instahack ../')
		print('\n\033[1;31m[*]\033[1;33m instahack installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==42:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/hatRiot/zarp')
		system('mv zarp ../')
		print('\n\033[1;31m[*]\033[1;33m zarp installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==43:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
			system("apt install hashcat -y")
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
			system("pkg install hashcat -y")
		print('\n\033[1;31m[*]\033[1;33m HashCat installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==44:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/CiKu370/hasher.git')
		system('mv hasher ../')
		print('\n\033[1;31m[*]\033[1;33m hasher installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==45:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/pymedusa/Medusa.git')
		system('mv Medusa ../')
		print('\n\033[1;31m[*]\033[1;33m Medusa installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==46:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/xmendez/wfuzz.git')
		system('mv wfuzz ../')
		print('\n\033[1;31m[*]\033[1;33m wfuzz installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==47:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Ettercap/ettercap.git')
		system('mv ettercap ../')
		print('\n\033[1;31m[*]\033[1;33m Ettercap installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==48:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Cvar1984/PassGen')
		system('mv PassGen ../')
		print('\n\033[1;31m[*]\033[1;33m PassGen installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==49:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
			system('apt install nmap curl')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
			system('pkg install nmap curl')
		system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/androzenmap.sh')
		system('mkdir ~/AndroZenmap')
		system('mv androzenmap.sh ~/AndroZenmap')
		print('\n\033[1;31m[*]\033[1;33m Easymap installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==50:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Smaash/snitch')
		system('mv snitch ../')
		print('\n\033[1;31m[*]\033[1;33m snitch installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==51:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Gameye98/AstraNmap')
		system('mv AstraNmap ../')
		print('\n\033[1;31m[*]\033[1;33m AstraNmap installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==52:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/joker25000/Devploit')
		system('mv Devploit ../')
		print('\n\033[1;31m[*]\033[1;33m Devploit installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==53:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Ubaii/Xshell')
		system('mv Xshell ../')
		print('\n\033[1;31m[*]\033[1;33m Xshell installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==54:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/HA71/Namechk')
		system('mv Namechk ../')
		print('\n\033[1;31m[*]\033[1;33m Namechk installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==55:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone http://www.github.com/Cvar1984/sqlscan')
		system('mv sqlscan ../')
		print('\n\033[1;31m[*]\033[1;33m sqlscan installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==56:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Gameye98/ddcrypt')
		system('mv ddcrypt ../')
		print('\n\033[1;31m[*]\033[1;33m ddcrypt installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==57:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/dotfighter/torshammer')
		system('mv torshammer ../')
		print('\n\033[1;31m[*]\033[1;33m torshammer installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==58:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Gameye98/Black-Hydra')
		system('mv Black-Hydra ../')
		print('\n\033[1;31m[*]\033[1;33m Black-Hydra installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==59:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Mebus/cupp')
		system('mv cupp ../')
		print('\n\033[1;31m[*]\033[1;33m cupp installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==60:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/LOoLzeC/ASU')
		system('mv ASU ../')
		print('\n\033[1;31m[*]\033[1;33m ASU installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==61:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/s0md3v/Hash-Buster')
		system('mv Hash-Buster ../')
		print('\n\033[1;31m[*]\033[1;33m Hash-Buster installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==62:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/The404Hacking/websploit')
		system('mv websploit ../')
		print('\n\033[1;31m[*]\033[1;33m websploit installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==63:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Lexiie/Termux-Apktool')
		system('mv Termux-Apktool ../')
		system("cd ../Termux-Apktool && dpkg -i *.deb")
		print('\n\033[1;31m[*]\033[1;33m Termux-Apktool installed successfully √')
		print(color("###### G@Type 'apktool' to start."))
		sleep(2)
		system('clear')
		Ttools()

	elif tools==64:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Screetsec/Brutal')
		system('mv Brutal ../')
		print('\n\033[1;31m[*]\033[1;33m Brutal installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==65:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/4w4k3/KnockMail')
		system('mv KnockMail ../')
		print('\n\033[1;31m[*]\033[1;33m KnockMail installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==66:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Cvar1984/Hac')
		system('mv Hac ../')
		print('\n\033[1;31m[*]\033[1;33m Hac installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==67:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/floriankunushevci/rang3r')
		system('mv rang3r ../')
		print('\n\033[1;31m[*]\033[1;33m Rang3r installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==68:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/LOoLzeC/SH33LL')
		system('mv SH33LL ../')
		print('\n\033[1;31m[*]\033[1;33m SH33LL installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==69:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Cvar1984/SpiderBot')
		system('mv SpiderBot ../')
		print('\n\033[1;31m[*]\033[1;33m SpiderBot installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==70:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Cvar1984/Ecode')
		system('mv Ecode ../')
		print('\n\033[1;31m[*]\033[1;33m Ecode installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==71:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
		system('mv RED_HAWK ../')
		print('\n\033[1;31m[*]\033[1;33m RED_HAWK installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==72:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/shawarkhanethicalhacker/D-TECT')
		system('mv D-TECT ../')
		print('\n\033[1;31m[*]\033[1;33m D-TECT installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==73:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/thelinuxchoice/thechoice')
		system('mv thechoice ../')
		print('\n\033[1;31m[*]\033[1;33m thechoice installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==74:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/cr4shcod3/pureblood')
		system('mv pureblood ../')
		print('\n\033[1;31m[*]\033[1;33m pureblood installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==75:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/thelinuxchoice/userrecon')
		system('mv userrecon ../')
		print('\n\033[1;31m[*]\033[1;33m userrecon installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==76:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/UltimateHackers/ReconDog')
		system('mv ReconDog ../')
		print('\n\033[1;31m[*]\033[1;33m ReconDog installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==77:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/m4ll0k/Infoga')
		system('mv Infoga ../')
		print('\n\033[1;31m[*]\033[1;33m Infoga installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==78:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Manisso/Crips')
		system('mv Crips ../')
		print('\n\033[1;31m[*]\033[1;33m Crips installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==79:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/UndeadSec/EvilURL.git')
		system('mv EvilURL ../')
		print('\n\033[1;31m[*]\033[1;33m EvilURL installed successfully √')
		sleep(2)
		system('clear')
		Ttools()
	elif tools==80:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/maldevel/IPGeoLocation')
		system('mv IPGeoLocation ../')
		print('\n\033[1;31m[*]\033[1;33m IPGeoLocation installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==81:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/CruzTed/Hammer')
		system('mv Hammer ../')
		print('\n\033[1;31m[*]\033[1;33m Hammer installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==82:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Ha3MrX/DDos-Attack')
		system('mv DDos-Attack ../')
		print('\n\033[1;31m[*]\033[1;33m DDos-Attack installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==83:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/jseidl/GoldenEye')
		system('mv GoldenEye ../')
		print('\n\033[1;31m[*]\033[1;33m GoldenEye installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==84:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/gkbrk/slowloris.git')
		system('mv slowloris ../')
		print('\n\033[1;31m[*]\033[1;33m slowloris installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==85:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/zanyarjamal/xerxes')
		system('mv xerxes ../')
		print('\n\033[1;31m[*]\033[1;33m xerxes installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==86:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/grafov/hulk')
		system('mv hulk ../')
		print('\n\033[1;31m[*]\033[1;33m Hulk installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==87:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/thelinuxchoice/shellphish')
		system('mv shellphish ../')
		print('\n\033[1;31m[*]\033[1;33m shellphish installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==88:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/evait-security/weeman')
		system('mv weeman ../')
		print('\n\033[1;31m[*]\033[1;33m weeman installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==89:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/thelinuxchoice/blackeye')
		system('mv blackeye ../')
		print('\n\033[1;31m[*]\033[1;33m BlackEye installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==90:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/UndeadSec/SocialFish.git')
		system('mv SocialFish ../')
		print('\n\033[1;31m[*]\033[1;33m SocialFish installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==91:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/DarkSecDevelopers/HiddenEye.git')
		system('mv HiddenEye ../')
		print('\n\033[1;31m[*]\033[1;33m HiddenEye installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==92:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/trustedsec/social-engineer-toolkit')
		system('mv social-engineer-toolkit ../')
		print('\n\033[1;31m[*]\033[1;33m Social-Engineer-Toolkit installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==93:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Gameye98/OWScan')
		system('mv OWScan ../')
		print('\n\033[1;31m[*]\033[1;33m OWScan installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==94:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
			system("apt-get install nmap -y")
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
			system("pkg install nmap -y")
		system('mv Nmap ../')
		print('\n\033[1;31m[*]\033[1;33m Nmap installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==95:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/Dionach/CMSmap.git')
		system('mv CMSmap ../')
		print('\n\033[1;31m[*]\033[1;33m CMSmap installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==96:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/D4Vinci/Clickjacking-Tester')
		system('mv Clickjacking-Tester ../')
		print('\n\033[1;31m[*]\033[1;33m Clickjacking-Tester installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==97:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/TechnicalMujeeb/TM-scanner')
		system('mv TM-scanner ../')
		print('\n\033[1;31m[*]\033[1;33m TM-scanner installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==98:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/AndroBugs/AndroBugs_Framework')
		system('mv AndroBugs_Framework ../')
		print('\n\033[1;31m[*]\033[1;33m AndroBugs_Framework installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==99:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/thelinuxchoice/sqliscan')
		system('mv sqliscan ../')
		print('\n\033[1;31m[*]\033[1;33m sqliscan installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==100:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/commixproject/commix')
		system('mv commix ../')
		print('\n\033[1;31m[*]\033[1;33m commix installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==101:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/m4110k/WPSeku')
		system('mv WPSeku ../')
		print('\n\033[1;31m[*]\033[1;33m WPSeku installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==102:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/reverse-shell/routersploit.git')
		system('mv routersploit ../')
		print('\n\033[1;31m[*]\033[1;33m RouterSploit installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==103:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/sullo/nikto')
		system('mv nikto ../')
		print('\n\033[1;31m[*]\033[1;33m Nikto installed successfully √')
		sleep(2)
		system('clear')
		Ttools()

	elif tools==104:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system('sudo apt-get install git -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install git -y')
		system('git clone https://github.com/lightos/credmap')
		system('mv credmap ../')
		print('\n\033[1;31m[*]\033[1;33m Credmap installed successfully √')
		sleep(2)
		system('clear')
		Ttools()
		
	elif tools ==999:
		sleep(0.8)
		restart()
	
	elif tools ==00:
		print(" ")
		for s in range(0, 3):
			print(color(" Y@[R@!Y@]R@ E x i t i n g ..G@/"),end="\r")
			sleep(.2)
			print(color(" Y@[R@!Y@]R@ E x i t i n g ..G@-"),end="\r")
			sleep(.2)
			print(color(" Y@[R@!Y@]R@ E x i t i n g ..G@\\"),end="\r")
			sleep(.2)
		system("reset")
		exit()
						
	else:
		print(" ")
		for r in range(0,4):
				print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@x"),end='\r')
				sleep(.5)
				print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@X"),end="\r")
				sleep(.5)
		system('clear')
		Ttools()

######################
#part 3 meta
####################### 
def Meta():
	system("clear")
	meta_bnr()   
	print(color("W@         +===================================+"))
	sleep(.1)
	print(color("         +[G@1W@] G@Install Metasploit W@	     +"))
	sleep(.1)
	print(color("         +===================================+"))
	sleep(.1)
	print(color("         +[G@2W@] G@Update Metasploit W@	     +"))
	sleep(.1)
	print(color("         +===================================+"))
	sleep(.1)
	print(color("         +[G@3W@] G@Remove Metasploit		     W@+"))
	sleep(.1)
	print(color("         +===================================+"))
	sleep(.1)
	print(color("         +[G@4W@] G@Fix Database Problems W@	     +"))
	sleep(.1)
	print(color("         +===================================+"))
	sleep(.1)
	print(color("         +[]>[C@99W@] C@Main Menu W@		     +"))
	sleep(.1)
	print(color("         +===================================+"))
	sleep(.1)
	print(color("         +═[]>[R@00W@]R@ Exit W@		     +"))
	sleep(.1)
	print(color("         +=================+=================+"))
	sleep(.1)
	print(color("          +================+"))
	
	meta = int(input(color('          +==>$\ C@')))
	if meta ==1:
		install = input('\033[1;31m[!]  \033[1;33mDo you have \033[1;37m500MB \033[1;33mfree in your storage??(\033[1;32my \033[1;33m/ \033[1;31mn\033[1;33m) : \033[1;36m')
		if install =='y' or install =='Y':
			if OS ==1:
				system('sudo apt-get update -y')
				system('sudo apt-get upgrade -y')
				system('sudo apt install unstable-repo -y')
			elif OS ==2:
				system('pkg update -y')
				system('pkg upgrade -y')
				system('apt install unstable-repo -y')
				system('pkg install metasploit -y')

			print(' ')
			print('\033[1;31m[*]\033[1;36m Metasploit Installed Successfully √')
			print(color("\nG@### Y@Enter 'msfconsole' To Run Metasploit"))
			sleep(3)
			Meta()
	
		elif install =='n' or install =='N':
			loadbar()
			Meta()
	
		else:
			print(" ")
			for r in range(0,4):
				print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@x"),end='\r')
				sleep(.5)
				print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@X"),end="\r")
				sleep(.5)
			restart()
	
	elif meta ==2:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system("sudo apt install unstable-repo -y")
			system("sudo apt-get install metasploit")
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install unstable-repo -y')
			system('pkg install metasploit')
		system('msfupdate')
		print(' ')
		print('\033[1;32m[*] \033[1;37mMetasploit Updated Successfully √')
		sleep(1)
		Meta()
	
	elif meta ==3:		
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
			system("apt install unstable-repo -y")
			system("apt remove metasploit")
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
			system('pkg install unstable-repo -y')
			system('pkg remove metasploit')
		print(' ')
		print('\033[1;32m[*] \033[1;37mMetasploit Removed Successfully √')
		sleep(0.8)
		Meta()
		
	elif meta == 4:
		if OS==1:
			system('sudo apt-get update -y')
			system('sudo apt-get upgrade -y')
		
		elif OS==2:
			system('pkg update -y')
			system('pkg upgrade -y')
		system ("mkdir -p $PREFIX/var/lib/postgresql")
		system ("initdb  $PREFIX/var/lib/postgresql")
		system ("pg_ctl -D $PREFIX/var/lib/postgresql")
		system ('gem install bundle')
		system ('gem install bundler')
		system ('pip2 install bundle')
		system ('bundle config build.nokogiri --use-system-libraries')
		system ('bundle install')
		system ('bundle update nokogiri')
		system ('gem install nokogiri')
		system ('gem install nokogiri -- --use-system-libraries')
		system ('gem install pkg-config -v "~> 1.1" ')
		system ('pkg-config')
		system ('bundle update nokogiri')
		print(color("\nG@### Done √"))
		sleep(2)
		Meta()
		
	elif meta ==99:
		loadbar()
		system('clear')
		restart()
	
	elif meta ==00:
		print(" ")
		for s in range(0, 3):
			print(color(" Y@[R@!Y@]R@ E x i t i n g ..G@/"),end="\r")
			sleep(.2)
			print(color(" Y@[R@!Y@]R@ E x i t i n g ..G@-"),end="\r")
			sleep(.2)
			print(color(" Y@[R@!Y@]R@ E x i t i n g ..G@\\"),end="\r")
			sleep(.2)
		system('reset')
		exit()
	
	else:
		print(" ")
		for r in range(0,4):
			print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@x"),end='\r')
			sleep(.5)
			print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@X"),end="\r")
			sleep(.5)
		restart()             

######################
#part 4 termux-linux
#######################
def Linux():
	system("clear")
	linux_bnr()
	print(color("        C@╔═════════════════════════════════╗"))
	sleep(.1)
	print(color("        ╠[W@1C@] G@Install Termux-Kali          C@║"))
	sleep(.1)
	print("        ╠═════════════════════════════════╣")
	sleep(.1)
	print(color("        ╠[W@2C@] G@Install Termux-FedoraC@        ║"))
	sleep(.1)
	print("        ╠═════════════════════════════════╣")
	sleep(.1)
	print(color("        ╠[W@4C@] G@Install NetHunterC@            ║"))
	sleep(.1)
	print("        ╠═════════════════════════════════╣")
	sleep(.1)
	print(color("        ╠[W@5C@] G@Install BackBoxC@              ║"))
	sleep(.1)
	print("        ╠═════════════════════════════════╣")
	sleep(.1)
	print(color("        ╠[W@5C@] G@Install CentOs               C@║"))
	sleep(.1)
	print("        ╠═════════════════════════════════╣")
	sleep(.1)
	print(color("        ╠[W@6C@] G@Install Arch-Linux           C@║"))
	sleep(.1)
	print("        ╚══════╦═══════════════════╦══════╝")
	sleep(.1)
	print(color("               ║  [Y@99C@] Y@Main Menu  C@ ║"))
	sleep(.1)
	print("               ╠═══════════════════╣")
	sleep(.1)
	print(color("               ║     [R@00C@] R@Exit     C@║"))
	sleep(.1)
	print("               ╚═════════╦═════════╝")
	sleep(.1)
	print("              ╔══════════╝")
	sleep(.1)
	
	linux = int(input(color('              ╚═══>\033[1;33m$\ W@')))
	
	if linux ==1:
		kali =input('\033[1;31m[!]  \033[1;33mDo you have \033[1;37m500MB \033[1;33mfree in your storage??(\033[1;32my \033[1;33m/ \033[1;31mn\033[1;33m) : \033[1;36m')
	
		if kali =='y' or kali =='Y':   
			if OS ==1:
				system('sudo apt-get update -y')
				system('sudo apt-get upgrade -y')
				system("sudo apt-get install wget proot -y && wget -y")
				system("sudo apt-get install git -y")
			elif OS ==2:
				system('pkg update -y')
				system("pkg upgrade -y")
				system("pkg install wget proot -y && wget -y")
				system("pkg install git -y")
			system('git clone https://github.com/MasterDevX/Termux-Kali.git')
			system('mv Termux-Kali ../')
			print(' ')
			print('\033[1;31m[*] \033[1;33mTermux-Kali Installed Successfully √')
			sleep(2)
			system("clear")
			Linux()
	
		elif kali=='n' or kali =='N':
			loadbar()
			Linux()
	
		else:
			print(" ")
			for r in range(0,4):
				print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@x"),end='\r')
				sleep(.5)
				print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@X"),end="\r")
				sleep(.5)
			Linux()
			
	
	elif linux ==2:
		fedora =input('\033[1;31m[!]  \033[1;33mDo you have \033[1;37m500MB \033[1;33mfree in your storage??(\033[1;32my \033[1;33m/ \033[1;31mn\033[1;33m) : \033[1;36m')
	
		if fedora =='y' or fedora =='Y':
			if OS ==1:
				system('sudo apt-get update -y')
				system('sudo apt-get upgrade -y')
				system('sudo apt-get install wget proot -y && wget -y')
				system('sudo apt-get install git -y')
			elif OS ==2:
				system('pkg update -y')
				system('pkg upgrade -y')
				system('pkg install wget proot -y && wget -y')
				system('pkg install git -y')
			system('git clone https://github.com/nmilosev/termux-fedora.git')
			system('mv termux-fedora ../')
			print(' ')
			print('\033[1;33m[*] \033[1;36mFedora-termux installed successfully √')
			sleep(2)
			Linux()
		
		elif fedora =='n' or fedora =='N':
			loadbar()
			Linux()
		
		else:
			print('\033[1;31m[\033[1;33m!\033[1;31m] Error..Please try again ~')
			sleep(2)
			system("clear")
			linux_bnr()
			Linux()

	elif linux ==3:
		ubuntu =input('\033[1;31m[!]  \033[1;33mDo you have \033[1;37m500MB \033[1;33mfree in your storage??(\033[1;32my \033[1;33m/ \033[1;31mn\033[1;33m) : \033[1;36m')

		if ubuntu =='y' or ubuntu =='Y':
			if OS ==1:
				system('sudo apt-get update -y')
				system('sudo apt-get upgrade -y')
				system("apt-get install wget proot -y && wget -y")
				system('sudo apt-get install git -y')
			elif OS ==2:
				system("pkg update -y")
				system('pkg upgrade -y')
				system("pkg install wget proot -y && wget -y")
				system("pkg install git -y")
			system('git clone https://github.com/Neo-Oli/termux-ubuntu.git')
			system('mv termux-ubuntu ../')
			print('\n\033[1;32m[*] \033[1;37mTermux-ubuntu installed successfully √')
			sleep(2)
			system("clear")
			linux_bnr()
			Linux()

		elif ubuntu =='n' or ubuntu =='N':
			con_termux()

		else:
			print(" ")
			for r in range(0,4):
				print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@x"),end='\r')
				sleep(.5)
				print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@X"),end="\r")
				sleep(.5)
			Linux()

	elif linux ==4:
		hunter =input(color('R@[!]  Y@Do you have W@500MB Y@free in your storage??(G@y Y@/ R@nY@) : C@'))

		if hunter =='y' or hunter =='Y':
			if OS ==1:
				system('sudo apt-get update -y')
				system("sudo apt-get upgrade -y")
				system("sudo apt-get install wget proot -y && wget -y")
				system("sudo apt-get install git -y")
				system('sudo apt-get install wget openssl-tool proot -y && hash -r && wget https:/\raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/BackBox/backbox.sh && bash backbox.sh')
			elif OS ==2:
				system("pkg update -y")
				system("pkg upgrade -y")
				system('pkg install wget proot -y && wget -y')
				system("pkg install git -y")
				system('pkg install wget openssl-tool proot -y && hash -r && wget https:/\raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/BackBox/backbox.sh && bash backbox.sh')
			
			print('\n\033[1;32m[*] \033[1;37mNetHunter installed successfully √')
			sleep(2)
			system("clear")
			Linux()

		elif hunter =='n' or hunter =='N':
			loadbar()
			Linux()

		else:
			print(" ")
			for r in range(0,4):
				print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@x"),end='\r')
				sleep(.5)
				print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@X"),end="\r")
				sleep(.5)
			Linux()

	elif linux ==5:
		bbox =input('\033[1;31m[!]  \033[1;33mDo you have \033[1;37m500MB \033[1;33mfree in your storage??(\033[1;32my \033[1;33m/ \033[1;31mn\033[1;33m) : \033[1;36m')

		if bbox =='y' or bbox =='Y':
			if OS ==1:
				system('sudo apt-get update -y')
				system('sudo apt-get upgrade -y')
				system('sudo apt-get install wget proot -y && wget -y')
				system("sudo apt-get install git -y")
				system('sudo apt-get install wget openssl-tool proot -y && hash -r && wget https:/\raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/BackBox/backbox.sh && bash backbox.sh')
			elif OS ==2:
				system('pkg update -y')
				system("pkg upgrade -y")
				system("pkg install wget proot -y && wget -y")
				system("pkg install git")
				system('pkg install wget openssl-tool proot -y && hash -r && wget https:/\raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/BackBox/backbox.sh && bash backbox.sh')
				
			print('\n\033[1;32m[*] \033[1;37mBackBox installed successfully √')
			sleep(2)
			system("clear")
			Linux()

		elif bbox =='n' or bbox =='N':
			loadbar()
			Linux()

		else:
			print(" ")
			for r in range(0,4):
				print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@x"),end='\r')
				sleep(.5)
				print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@X"),end="\r")
				sleep(.5)
			Linux()

	elif linux ==6:
		centos =input('\033[1;31m[!]  \033[1;33mDo you have \033[1;37m500MB \033[1;33mfree in your storage??(\033[1;32my \033[1;33m/ \033[1;31mn\033[1;33m) : \033[1;36m')

		if centos =='y' or centos =='Y':
			if OS ==1:
				system("sudo apt-get update -y")
				system("sudo apt-get upgrade -y")
				system('sudo apt-get install wget openssl-tool proot tar -y && hash -r && wget https:/\raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/CentOS/centos.sh && bash centos.sh')
			elif OS ==2:
				system("pkg update -y")
				system("pkg upgrade -y")
				system('pkg install wget openssl-tool proot tar -y && hash -r && wget https:/\raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/CentOS/centos.sh && bash centos.sh')
			
			print('\n\033[1;32m[*] \033[1;37mCent-OS installed successfully √')
			sleep(2)
			Linux()

		elif centos =='n' or centos =='N':
			loadbar()
			Linux()

		else:
			print(" ")
			for r in range(0,4):
				print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@x"),end='\r')
				sleep(.5)
				print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@X"),end="\r")
				sleep(.5)
			Linux()

	elif linux ==7:
		arch =input('\033[1;31m[!]  \033[1;33mDo you have \033[1;37m500MB \033[1;33mfree in your storage??(\033[1;32my \033[1;33m/ \033[1;31mn\033[1;33m) : \033[1;36m')

		if arch =='y' or arch =='Y':
			if OS ==1:
				system('sudo apt-get update -y')
				system("sudo apt-get upgrade -y")
				system('sudo apt-get install wget openssl-tool proot tar -y && hash -r && wget https:/\raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Arch/armhf/arch.sh && bash arch.sh')
			elif OS ==2:
				system("pkg update -y")
				system('pkg upgrade -y')
				system("pkg install wget openssl-tool proot tar -y && hash -r && wget https:/\raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Arch/armhf/arch.sh && bash arch.sh")
			print('\n\033[1;32m[*] \033[1;37mArch-Linux installed successfully √')
			sleep(2)
			Linux()

		elif arch =='n' or arch =='N':
			loadbar()
			Linux()

		else:
			print(" ")
			for r in range(0,4):
				print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@x"),end='\r')
				sleep(.5)
				print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@X"),end="\r")
				sleep(.5)
			Linux()

	elif linux ==99:
		restart()

	elif linux ==00:
		print(" ")
		for s in range(0, 3):
			print(color(" Y@[R@!Y@]R@ E x i t i n g ..G@/"),end="\r")
			sleep(.2)
			print(color(" Y@[R@!Y@]R@ E x i t i n g ..G@-"),end="\r")
			sleep(.2)
			print(color(" Y@[R@!Y@]R@ E x i t i n g ..G@\\"),end="\r")
			sleep(.2)
		system('reset')
		exit()

	else:
		print(" ")
		for r in range(0,4):
			print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@x"),end='\r')
			sleep(.5)
			print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@X"),end="\r")
			sleep(.5)
		Linux()
    
######################
#part5.   hasing
####################### 
class hashing_class:
    def encode_py(en_py):
        #This is for encode python scripts
   
        with open(en_py, 'rb') as m:
            file = m.read()

        hash =b64encode(file)

        with open (en_py, 'wb') as n:
            data = n.write(hash)
    
        with open(en_py, 'r')as r:
            encoded = r.read()
    
        with open(en_py, 'w') as w:
    	    w.write('import base64\n')
    	    w.write('x=("')
    	    w.write(encoded)
    	    w.write('")')
    	    w.write('\nexec(base64.b64decode(x))')
    	   	   
    def decode_py(de_py):
        #this is for decode python scripts

        with open(de_py, 'rb') as file:
            f=file.read()
            f=f.replace(b'import base64',b'')
            f=f.replace(b'x=("',b'')
            f=f.replace(b'")',b'')
            f=f.replace(b'exec(base64.b64decode(x))',b'')
    
        decoded =b64decode(f)

        with open(de_py, 'wb') as b:
            b.write(decoded)
        
     
    def encode_media(en_media):
        #this is for encode any media file (mp4, mp3, jpg, png, 3gp, img, pdf, txt, csv, Ai, ps, apk)
        
        with open(en_media, 'rb') as m:
            file = m.read()

        hash =b64encode(file)

        with open (en_media, 'wb') as n:
            data = n.write(hash)
    
        with open(en_media, 'r')as r:
            encoded = r.read()
    
        with open(en_media, 'w') as w:
    	    w.write(encoded)
    	    system("mv " + str(en_media) + " " + str(en_media) + ".encoded")
    
    def decode_media(de_media):
        #this is for decode any media file encoded by this script only
         
         with open(de_media, 'rb') as file:
            f=file.read()           
    
         decoded =b64decode(f)
        
         q = len(de_media)
         w=q-8
         e=de_media[0:w]
        
         with open(de_media, 'wb') as b:
             b.write(decoded)
         
         system("mv " + str(de_media) + " " + str(e))
    
      
       
    def encode_text(text):
        #this is for encode texts
        
        hash = b64encode(text.encode("ascii"))
        
        return str(hash)             

    def decode_text(text):
        #this is for decode texts
                
        hash = b64decode(text)
        
        return str(hash)

def dark_encode():
	system("clear")
	hash_bnr()
	print(color("	   R@+==================================+"))
	sleep(.1)
	print(color("	   R@+>Y@[G@1Y@] G@Encode Python Files          R@+"))
	sleep(.1)
	print(color("	   R@+  Y@(Encode Your Python Scripts)    R@+"))
	sleep(.1)
	print(color("	   R@+==================================+"))
	sleep(.1)
	print(color("	   R@+>Y@[G@2Y@] G@Decode Python Files     R@     +"))
	sleep(.1)
	print(color("	   R@+  Y@(Decode Your Python Scripts)    R@+"))
	sleep(.1)
	print(color("	   R@+##################################+"))
	sleep(.1)
	print(color("	   R@+>Y@[G@3Y@] G@Encode Other Files Types R@    +"))
	sleep(.1)
	print(color("	   R@+  Y@(Encode Mp4 ,Mp3 ,Apk ,Jpg ,..) R@+"))
	sleep(.1)
	print(color("	   R@+==================================+"))
	sleep(.1)
	print(color("	   R@+>Y@[G@4Y@] G@Decode Other Files Types R@    +"))
	sleep(.1)
	print(color("	   R@+  Y@(Decode Mp4 ,Mp3 ,Apk ,Jpg ,..) R@+"))
	sleep(.1)
	print(color("	   R@+##################################+"))
	sleep(.1)
	print(color("	   R@+>Y@[G@5Y@] G@Encode Your Text       R@      +"))
	sleep(.1)
	print(color("	   R@+  Y@(Enter Text To Encode It)       R@+"))
	sleep(.1)
	print(color("	   R@+==================================+"))
	sleep(.1)
	print(color("	   R@+>Y@[G@6Y@] G@Decode Your Text         R@    +"))
	sleep(.1)
	print(color("	   R@+  Y@(Enter Text To Decode It)       R@+"))
	sleep(.1)
	print(color("	   R@+##################################+"))
	sleep(.1)
	print(color("	   R@+>G@[Y@99G@] Y@Main Menu               R@    +"))
	sleep(.1)
	print(color("	   R@+  W@(Go To Main Page)               R@+"))
	sleep(.1)
	print(color("	   R@+==================================+"))
	sleep(.1)
	print(color("	   R@+>Y@[R@00Y@] R@Exit                  R@      +"))
	sleep(.1)
	print(color("	   R@+  W@(Close From ToOl)               R@+"))
	sleep(.1)
	print(color("	   R@+=================+================+"))
	sleep(.1)
	print(color("        R@                     +"))
	sleep(.1)
	print(color("         R@   +================+"))
	sleep(.1)
	de = int(input(color("  R@          +> G@")))

	if de ==1:
		en_py = input(color("\nR@[*]W@ Enter File Path #>Y@ "))
		
		if path.exists(en_py):
			hashing_class.encode_py(en_py)
			loadbar()
			print(color("\n\nR@###> G@Done √"))
			sleep(2)
			dark_encode()

		else:
			print(color("\n R@{Y@!R@} File Not Exists .."))
			sleep(2)
			dark_encode()

	elif de ==2:
		de_py = input(color("\nR@[*]W@ Enter File Path #>Y@ "))

		if path.exists(de_py):
			hashing_class.decode_py(de_py)
			loadbar()
			print(color("\n\nR@###> G@Done √"))
			sleep(2)
			dark_encode()

		else:
			print(color("\n R@{Y@!R@} File Not Exists .."))
			sleep(2)
			dark_encode()

	elif de ==3:
		en_media = str(input(color("\nR@[*] W@Enter File Path #>Y@ ")))

		if path.exists(en_media):
			hashing_class.encode_media(en_media)
			loadbar()
			print(color("\n\nR@###> G@Done √"))
			sleep(2)
			dark_encode()

		else:
			print(color("\n R@{Y@!R@} File Not Exists .."))
			sleep(2)
			dark_encode()

	elif de ==4:
		de_media = input(color("\nR@[*] W@Enter File Path #> Y@"))

		if path.exists(de_media):
			hashing_class.decode_media(de_media)
			loadbar()
			print(color("\n\nR@###> G@Done √"))
			sleep(2)
			dark_encode()

		else:
			print(color("\n R@{Y@!R@} File Not Exists .."))
			sleep(2)
			dark_encode()

	elif de ==5:
		text = input(color("\nR@[*] W@Enter Text To Encode #> Y@"))
		en_txt = hashing_class.encode_text(text)
		loadbar()
		print(color("\n\nW@##> Original Text: G@" + str(text)))
		print(color("\nB@###> Encoded Text: W@" + str(en_txt)))
		print(color("\n\n  {*} If You Want To Decode Text ,Copy Text Between ' ' Only "))
		
		print(color("G@\n\n-> {99} Use Again ~"))
		print(color("R@-> {00} Main Menu"))
		again = int(input(color("\n+-> ")))
		if again ==99:
			system("clear")
			dark_encode()

		elif again ==00:
			system("clear")
			restart()

		else:
			print(" ")
			for r in range(0,4):
				print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@x"),end='\r')
				sleep(.5)
				print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@X"),end="\r")
				sleep(.5)
			system("clear")
			dark_encode()

	elif de ==6:
		text = input(color("\n[*] Enter Text To Decode #> "))
		de_txt = hashing_class.decode_text(text)
		loadbar()
		print(color("\n\nW@##> Encoded Text: G@" + str(text)))
		print(color("\n\nB@###> Decoded Text: W@" + str(de_txt)))
		
		print(color("G@\n\n-> {99} Use Again ~"))
		print(color("R@-> {00} Main Menu"))
		again = int(input(color("\n+-> ")))
		if again ==99:
			system("clear")
			dark_encode()

		elif again ==00:
			system("clear")
			restart()

		else:
			print(" ")
			for r in range(0,4):
				print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@x"),end='\r')
				sleep(.5)
				print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@X"),end="\r")
				sleep(.5)
			system("clear")
			dark_encode()

	elif de ==99:
		loadbar()
		system('clear')
		restart()

	elif de ==00:
		print(" ")
		for s in range(0, 3):
			print(color(" Y@[R@!Y@]R@ E x i t i n g ..G@/"),end="\r")
			sleep(.2)
			print(color(" Y@[R@!Y@]R@ E x i t i n g ..G@-"),end="\r")
			sleep(.2)
			print(color(" Y@[R@!Y@]R@ E x i t i n g ..G@\\"),end="\r")
			sleep(.2)
		system('reset')
		exit()

	else:
		print(" ")
		for r in range(0,4):
			print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@x"),end='\r')
			sleep(.5)
			print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@X"),end="\r")
			sleep(.5)
		dark_encode()

#######################
#part6
#######################
def Websites():
    system("clear")
    sites_bnr()
    print(color("    Y@ ++++++++++++++++++++++++++++++++++++++++++++"))
    print(color("     +              R@[1] Ip Logger  Y@             +"))
    print(color("     +  G@(Inject Any link To Get Phone Location) Y@+"))
    print(color("     +   C@ >>> | https://iplogger.org/ | <<<    Y@ +"))
    sleep(.2)
    print(color("     +##########################################+"))
    print(color("     +           R@  [2] Ascii World             Y@ +"))
    print(color("     +   G@(Write Text To Art And Select Style)  Y@ +"))
    print(color("     + C@>>> | https://www.asciiworld.com/ | <<< Y@ +"))
    sleep(.2)
    print(color("     +##########################################+"))
    print(color("     +           R@  [3] Virus Total              Y@+"))
    print(color("     +  G@(Scan Links And Files Before Open It)   Y@+"))
    print(color('     + C@>>> | https://www.virustotal.com/ | <<<  Y@+'))
    sleep(.2)
    print(color("     +##########################################+"))
    print(color("     +           R@     [4] Mohmal               Y@ +"))
    print(color('     +      G@  (Creat Timed Fake Email)          Y@+'))
    print(color('     +  C@ >>> | https://www.mohmal.com/ | <<<    Y@+'))
    sleep(.2)
    print(color("     +##########################################+"))
    print(color('     +            R@   [5] Smikta                 Y@+'))
    print(color("     +  G@ (Fake Websites For Social Engneering) Y@ +"))
    print(color("     +  C@ >>> | https://www.smikta.net/ | <<<    Y@+"))
    sleep(.2)
    print(color("     +##########################################+"))
    print(color('     +            R@ [6] Joker-Dz                Y@ +'))
    print(color('     +  G@ (Fake Websites For Social Engneering) Y@ +'))
    print(color('     +   C@  >>> | https://jokerdz.com/ | <<<     Y@+'))
    sleep(.2)
    print(color('     +##########################################+'))
    print(color('     +            R@  [7] Shraidar                Y@+'))
    print(color('     +   G@(Fake Websites For Social Engneering)  Y@+'))
    print(color('     +  C@ >>> | https://myshraidar.com/ | <<<    Y@+'))
    sleep(.2)
    print(color('     +##########################################+'))
    print(color('     +         R@[8] Who IS Hosting This          Y@+'))
    print(color('     +    G@(Enter Host Name To Get Host Ip)      Y@+'))
    print(color('     + C@> | http://www.whoishostingthis.com/ | < Y@+'))
    sleep(.2)
    print(color('     +##########################################+'))
    print(color('     +          R@  [9] Ip2Location              Y@ +'))
    print(color('     +    G@  (Enter Ip To Get Ip Location)       Y@+'))
    print(color('     +  C@>>> | http://www.ip2location.com/ | <<< Y@+'))
    sleep(.2)
    print(color('     +##########################################+'))
    print(color("     +          R@      [10] Arin                Y@ +"))
    print(color('     +       G@ (Get Any Ip Informations)         Y@+'))
    print(color('     +    C@>>> | https://www.arin.net/ | <<<     Y@+'))
    sleep(.2)
    print(color('     +##########################################+'))
    print(color("     +             R@  [11] Archive              Y@ +"))
    print(color('     +  G@(See Sites Update And Archive History) Y@ +'))
    print(color("     +  C@   >>> | ‫‪http‬‬ ‫‪://archive.org/ | <<<     Y@+"))
    sleep(.2)
    print(color('     +##########################################+'))
    print(color('     +           R@   [12] Just-Ping             Y@ +'))
    print(color('     +  G@ (Ping Any Ip And Get Informations)    Y@ +'))
    print(color('     + C@ >>> | ‫‪http://cloudmonitor.ca.com/‬‬ | <<< Y@+'))
    sleep(.2)
    print(color('     +##########################################+'))
    print(color('     +          R@  [13] Pen-Test Tools           Y@+'))
    print(color('     +  G@(Scan Ports And Get Ports Inforamtion)  Y@+'))
    print(color('     +   C@>>> | http://pentest-tools.com/ | <<<  Y@+'))
    sleep(.2)
    print(color("     +##########################################+"))
    print(color("     +         R@   [14] You Get Signal           Y@+"))
    print(color("     + G@ (Scan Ports And Get Ports Inforamtion)  Y@+"))
    print(color('     + C@>>> | http://www.yougetsignal.com/ | <<< Y@+'))
    sleep(.2)
    print(color("     +##########################################+"))
    print(color('     +         R@     [15] Net Craft             Y@ +'))
    print(color('     + G@(Get Device Information From Ip Or Host) Y@Y@+'))
    print(color('     + C@>>> | http://toolbar.netcraft.com/ | <<< Y@+'))
    sleep(.2)
    print(color("     +##########################################+"))
    print(color("     +        R@  [16] Hide My Ass Proxy          Y@+"))
    print(color('     +  G@(Get Free Proxy To Hide Your Browsing)  Y@+'))
    print(color('     +  C@ >>> | http://www.hidemyass.com/ | <<<  Y@+'))
    sleep(.2)
    print(color('     +##########################################+'))
    print(color("     +         R@   [17] Vypr Vpn Proxy           Y@+"))
    print(color('     + G@ (Get Free Proxy To Hide Your Browsing)  Y@+'))
    print(color('     + C@ >>> | http://www.goldenfrog.com/ | <<<  Y@+'))
    sleep(.2)
    print(color('     +==========================================+'))
    print(color('     +                                        Y@  +'))
    print(color('     +             R@{C@99R@} B@Main Menu            Y@   +'))
    print(color('     +                                        Y@  +'))
    sleep(.2)
    print(color('     +==========================================+'))
    print(color('     +                                       Y@   +'))
    print(color('     +                {R@00Y@} R@Exit                Y@ +'))
    print(color('     +                                         Y@ +'))
    sleep(.2)
    print(color('     +=====================+====================+'))
    
    if OS ==1:
        print(color('         W@Enter Site Number Y@+ W@To Visit ItY@'))
        
    elif OS ==2:
        print(color('                           +'))
    
    print(color('         +=================+'))
    sites= int(input((color('         +=> R@'))))
    if OS ==1:
        if sites==1:
            tab("https://iplogger.org/")
            sleep(.3)
            Websites()
        
        elif sites==2:
            tab("https://www.asciiworld.com/")
            sleep(.3)
            Websites()
            
        elif sites ==3:
            tab("https://www.virustotal.com/")
            sleep(.3)
            Websites()
            
        elif sites ==4:
            tab("https://www.mohmal.com/")
            sleep(.3)
            Websites()
            
        elif sites==5:
            tab("https://www.smikta.net/")
            sleep(.3)
            Websites()
        
        elif sites ==6:
            tab("https://jokerdz.com/")
            sleep(.3)
            Websites()
            
        elif sites ==7:
            tab("https://myshraidar.com/")
            sleep(.3)
            Websites()
            
        elif sites==8:
            tab("http://www.whoishostingthis.com/")
            sleep(.3)
            Websites()
            
        elif sites==9:
            tab("http://www.ip2location.com/")
            sleep(.3)
            Websites()
        
        elif sites==10:
            tab("https://www.arin.net/")
            sleep(.3)
            Websites()
        
        elif sites==11:
            tab("http‬‬ ‫‪://archive.org/")
            sleep(.3)
            Websites()
            
        elif sites ==12:
            tab("http://cloudmonitor.ca.com")
            sleep(.3)
            Websites()
            
        elif sites==13:
            tab("http://pentest-tools.com/")
            sleep(.3)
            Websites()
            
        elif sites ==14:
            tab("http://www.yougetsignal.com/")
            sleep(.3)
            Websites()
        
        elif sites ==15:
            tab("http://toolbar.netcraft.com/ ")
            sleep(.3)
            Websites()
            
        elif sites==16:
            tab("http://www.hidemyass.com/")
            sleep(.3)
            Websites()
        
        elif sites==17:
            tab("http://www.goldenfrog.com/")
            sleep(.3)
            Websites()
        
        elif sites ==99:
            restart()
            for s in range(0, 3):
                print(color(" Y@[R@!Y@]R@ E x i t i n g ..G@/"),end="\r")
                sleep(.2)
                print(color(" Y@[R@!Y@]R@ E x i t i n g ..G@-"),end="\r")
                sleep(.2)
                print(color(" Y@[R@!Y@]R@ E x i t i n g ..G@\\"),end="\r")
                sleep(.2)
            system("reset")
            exit()

        else:
            print(" ")
            for r in range(0,4):
                print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@x"),end='\r')
                sleep(.5)
                print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@X"),end="\r")
                sleep(.5)
            Websites()

    elif OS ==2:            
        if sites==99:
            restart()

        elif sites==00:
            print(" ")
            for s in range(0, 3):
                print(color(" Y@[R@!Y@]R@ E x i t i n g ..G@/"),end="\r")
                sleep(.2)
                print(color(" Y@[R@!Y@]R@ E x i t i n g ..G@-"),end="\r")
                sleep(.2)
                print(color(" Y@[R@!Y@]R@ E x i t i n g ..G@\\"),end="\r")
                sleep(.2)
            system("reset")
            exit()

        else:
            print(" ")
            for r in range(0,4):
                print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@x"),end='\r')
                sleep(.5)
                print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@X"),end="\r")
                sleep(.5)
            Websites()
#####################
# Art
#####################	
def Art():
	system("clear")
	Art_bnr()

	if OS ==1:
		system("sudo apt-get install figlet -y")

	elif OS ==2:
		system('pkg install figlet -y')
		
	system('clear')
	Art_bnr()
	
	sleep(.1)
	print(color("\n\nC@       +--------------------Y@^_^C@-------------------+\n     B@  +                                          +"))
	sleep(.1)
	
	art =input(color('       +R@===>G@Enter Text To Art B@-> W@'))
	
	sleep(.1)
	print(color("R@       +                                          +\n    Y@   +------------------------------------------+"))
	sleep(.1)
	print("       +")
	sleep(.1)
	print(color("       +R@>>>>>>>>>>>>>>Y@+"))
	sleep(.1)
	for m in range(0, 3):
		sleep(.1)
		print(color("Y@                      ▼     B@/"),end="\r")
		sleep(.1)
		print(color("  Y@                    ▼     B@-"),end="\r")
		sleep(.1)
		print(color("    Y@                  ▼     B@\\"),end="\r")
	print(color("G@"))
	
	system('figlet '+str(art))
	sleep(2)
	
	print(color("\n\n-> {99} Use Again ~"))
	print(color("-> {00} Main Menu"))
	
	arty = int(input(color("\n+-> ")))
	if arty ==99:
		system("clear")
		Art()

	elif arty ==00:
		system("clear")
		restart()

	else:
		print(" ")
		for r in range(0,4):
			print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@x"),end='\r')
			sleep(.5)
			print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@X"),end="\r")
			sleep(.5)
		system("clear")
		Art()

######################
#Main
#######################   
def main():
    print("""      \033[1;36m+===========================================+""")
    sleep(.2)
    print("      +[\033[1;31m1\033[1;36m] \033[1;32mUpgrade System √ & Fix Problems >_< \033[1;36m   +")
    sleep(.2)
    print(color("      +\033[1;34m#################### G@JB@ ####################\033[1;36m+"))
    sleep(.2)
    print("      +[\033[1;31m2\033[1;36m] \033[1;32mJoker Tools >_O\033[1;36m                        +")
    sleep(.2)
    print(color("      +\033[1;34m#################### G@oB@ ####################\033[1;36m+"))
    sleep(.2)
    print("      +[\033[1;31m3\033[1;36m] \033[1;32mMetasploit (M.S.F.W)\033[1;36m                   +")
    sleep(.2)
    print(color("      +\033[1;34m#################### G@kB@ ####################\033[1;36m+"))
    sleep(.2)
    print("      +[\033[1;31m4\033[1;36m] \033[1;32mLinux In Termux \033[1;36m                       +")
    sleep(.2)
    print(color("      +\033[1;34m#################### G@eB@ ####################\033[1;36m+"))
    sleep(.2)
    print("      +[\033[1;31m5\033[1;36m] Dark Encode\033[1;32m(Encode & Decode AnyThing)\033[1;36m  +")
    sleep(.2)
    print(color("      +\033[1;34m#################### G@rB@ ####################\033[1;36m+"))
    sleep(.2)
    print("      +[\033[1;31m6\033[1;36m] \033[1;32mWebSites For You ^_^\033[1;36m                   +")
    sleep(.2)
    print(color("      +\033[1;34m#################### G@TB@ ####################\033[1;36m+"))
    sleep(.2)
    print("      +[\033[1;31m7\033[1;36m] \033[1;32mArt Your Text ◕‿-\033[1;36m                      +")
    sleep(.2)
    print(color("      +\033[1;34m#################### G@oB@ ####################\033[1;36m+"))
    sleep(.2)
    print("      +[\033[1;32m88\033[1;36m] \033[1;37mAbout Me  \033[1;36m                            +")
    sleep(.2) 
    print(color("      +\033[1;34m#################### G@oB@ ####################\033[1;36m+"))
    sleep(.2)
    print("      +[\033[1;32m99\033[1;36m] \033[1;33mCheck Lastest Version   \033[1;36m              +")
    sleep(.2)
    print(color("      +\033[1;34m#################### G@lB@ ####################\033[1;36m+"))
    sleep(.2)
    print("      +[\033[1;33m00\033[1;36m] \033[1;31mExit Tool \033[1;36m                            +")
    sleep(.2)
    print("""      +=====================+=====================+
          +=================+""") 

                                                                        
#########select a tool def#######$$$
def Main_page():
    main()
    sel = int(input("          +===>$\ \033[1;33m "))
    
    if sel ==1:
        up_termux()
        sleep(6)
        restart() 
    
    elif sel == 2:
        Ttools()

    elif sel ==3:
    	Meta()                      
    
    elif sel ==4:
    	Linux()

    elif sel ==5:
    	dark_encode()
    
    elif sel ==6:
    	Websites()

    elif sel==7:
    	Art()   	
 	 
    elif sel == 88:
        system('clear')
        tool_bnr()
        print("")
        with open("README.md", "r")as info:
            info = info.read()
            print(info)
        sleep(1)
        con_termux()

    elif sel ==99:
        system('clear')
        tool_bnr()
        print('''\033[1;33m
Tool Version : '1.3'

To Check The Latest Version, Please Visit:-

https://github.com/redVirus-Dev/JokerTools

And Download Lateset Version From Website ◕‿-''')
        sleep(0.6)
        con_termux()

    elif sel == 00 :
        print(" ")
        for s in range(0, 3):
        	print(color(" Y@[R@!Y@]R@ E x i t i n g ..G@/"),end="\r")
        	sleep(.2)
        	print(color(" Y@[R@!Y@]R@ E x i t i n g ..G@-"),end="\r")
        	sleep(.2)
        	print(color(" Y@[R@!Y@]R@ E x i t i n g ..G@\\"),end="\r")
        	sleep(.2)
        system("reset")
        exit()

    else :
    	print(" ")
    	for r in range(0,4):
    		print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@x"),end='\r')
    		sleep(.5)
    		print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@X"),end="\r")
    		sleep(.5)
    	print (color("\nG@[!] R e s t a r t I n g..."))
    	sleep(0.8)
    	restart()
################

system("chmod +x JokerTools-V1.3.py")
system('clear')
joker_banner()
print(color("R@{P@!R@} Y@What Are You Using??"))
print(color("\n#> [C@1Y@] C@Linux OS"))
print(color("\nY@##> [W@2Y@] W@Termux"))

OS = int(input(color("\nB@###> G@")))

if OS==1 or OS==2:
	print(color("\n\n =$\\ Done ..\n\n"))
	cptl(" starting joker tools ")
	system("clear")
	tool_bnr()
	Main_page()

else:
	print(" ")
	for r in range(0,4):
		print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@x"),end='\r')
		sleep(.5)
		print(color(" R@{Y@!R@}Y@ Oops Err .. Please try again .. C@X"),end="\r")
	sleep(2)
	system("python3 JokerTools-V1.3.py")