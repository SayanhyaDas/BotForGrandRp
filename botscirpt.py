import os
import sys
import time
import random
import pyautogui
from colorama import Fore, init
from pynput import keyboard
from pynput.keyboard import Key, Controller
from tqdm import trange

init (autoreset=True)
keyboard = Controller()

print("""Disclaimer (Read this you Lazyass  Person) :
              <>This Script Dose not transmites any Data from you PC
              <>While The Script is Running Better to switch windows to Rage Multiplayer to avoid error
              <>If you get banned for using this AntiAfk and E Spammer Bot We are not REsponsible
              <>If you want to Join Our Discord Server link : discord.gg/PgpKb7bz4S
 """)

choicealpha=input("Do you Wish to continue type (yes to continue) ")



if choicealpha == "yes":

    for i in trange(100):
        time.sleep(0.1)

    print(f"""{Fore.RED}  
     ███████ ██    ██  ██████ ██   ██       ██    ██  ██████  ██    ██        █████  ██████  ███    ███ ██ ███    ██ ███████ 
     ██      ██    ██ ██      ██  ██         ██  ██  ██    ██ ██    ██       ██   ██ ██   ██ ████  ████ ██ ████   ██ ██      
     █████   ██    ██ ██      █████   █████   ████   ██    ██ ██    ██ █████ ███████ ██   ██ ██ ████ ██ ██ ██ ██  ██ ███████ 
     ██      ██    ██ ██      ██  ██           ██    ██    ██ ██    ██       ██   ██ ██   ██ ██  ██  ██ ██ ██  ██ ██      ██ 
     ██       ██████   ██████ ██   ██          ██     ██████   ██████        ██   ██ ██████  ██      ██ ██ ██   ████ ███████ """)

    print("""[1] <> Anti Afk
    [2] <> E Spamming Bott""")
    choice=input("Choose Which to Start : ")

    if choice == "1":
        timer = 5
        loopamount = 10
        print("""
         █████  ███    ██ ████████ ██          █████  ███████ ██   ██ 
        ██   ██ ████   ██    ██    ██         ██   ██ ██      ██  ██  
        ███████ ██ ██  ██    ██    ██         ███████ █████   █████   
        ██   ██ ██  ██ ██    ██    ██         ██   ██ ██      ██  ██  
        ██   ██ ██   ████    ██    ██ ███████ ██   ██ ██      ██   ██ 
                                    <> Undetectable One <>""")   
        print("Timer to hold down key is : ", timer)
        print("Amount to loop : ", loopamount)
        print("starting after 5 secs")
        time.sleep(5)
        for i in range(1, loopamount):
            keyboard.press('w')
            print("pressed+", i)
            time.sleep(timer)
            keyboard.release('w')
            print("pressed-", i)
            time.sleep(timer)
        for i in trange(loopamount):
                time.sleep(0.1)
        print(Fore.GREEN + 'Stopped')

    if choice == "2":
        print("""
        
        ███████         ██████   ██████  ████████ 
        ██              ██   ██ ██    ██    ██    
        █████           ██████  ██    ██    ██    
        ██              ██   ██ ██    ██    ██    
        ███████ ███████ ██████   ██████     ██ """)
        timer1 = 3
        loopamount1 = 400
        print("Timer to hold down key is : ", timer1 )
        print("Amount to loop : ", loopamount1 )
        print("starting after 5 secs")
        time.sleep(5)
        for i in range(1, loopamount1):
            keyboard.press('e')
            print("pressed+", i)
            time.sleep(timer1)
            keyboard.release('e')
            print("pressed-", i)
            time.sleep(timer1)  
        print(Fore.GREEN + 'Stopped')

    else:
        print("Wrong choice Dumbass")
else:
    print("Wrong choice Dumbass")