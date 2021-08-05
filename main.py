# code by nerd-ops

import pyautogui as pa
from time import sleep

print("""
                    _                 
 _ __   ___ _ __ __| |      ___ _ __  
| '_ \ / _ \ '__/ _` |_____/ __| '_ \ 
| | | |  __/ | | (_| |_____\__ \ |_) |
|_| |_|\___|_|  \__,_|     |___/ .__/ 
                               |_|
         simple spammer owo
""")

# that's a simple spammer in python

def clicker(r):
    try:
        for i in range(0,int(r)):
            pa.click()
        print("end >:D")
    except Exception as e:
        print(f"ERROR - \n{e}")
def text_spammer(r):
    try:
        for i in range(0,int(r)):
            pa.hotkey("ctrl","v")
            pa.press("enter")
        print("end :D")
    except Exception as e:
        print(f"ERROR - \n{e}")
def menu():
    option = input("""
    HIIIIIIIIIII
    what's ur option?
    1. autoclicker
    2. text spammer
    
    select please : """)

    if option in ["1","2"]:
        if option == "1":
            print("\nOkay :D, put your mouse on the part where you want it to click")
            r = input("amount : ")
            print("in 20 seconds we start nwn")
            sleep(20)
            clicker(r)
        else:
            print("\nOkay :D, copy the text you want to use for spam and put ur mouse in the 'input text' of the page")
            r = input("amount : ")
            print("in 20 seconts we start nwn")
            sleep(20)
            pa.click()
            text_spammer(r)
    else:
        print("please select the correct option")
        sleep(3)
        menu()
menu()
