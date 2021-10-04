try:
    import pyautogui
    import time
    import random
    import colorama
    import os
    from colorama import Fore, init
except:
    print("u fucking moron. run 'pip install -r requirements.txt'")
    exit()


init(autoreset=True)
os.system("mode con: cols=70 lines=20")
os.system("cls")
print(Fore.RED + """
   __ _     _        __            _
  / _(_)   | |      / _|          | |
 | |_ _ ___| |__   | |_ _   _  ___| | _____ _ __
 |  _| / __| '_ \  |  _| | | |/ __| |/ / _ \ '__|
 | | | \__ \ | | | | | | |_| | (__|   <  __/ |
 |_| |_|___/_| |_| |_|  \__,_|\___|_|\_\___|_|      v0.1 Alpha Build
""")

while True:
    if pyautogui.locateOnScreen('fishCaught.png') != None:
        print(f"{Fore.GREEN}fuck fuck fuck theres a fucking fish. catch that bitch.")
        pyautogui.click(button='right')
        time.sleep(random.randint(0,1))
        pyautogui.click(button='right')
        time.sleep(2)
    else:
        print(f"{Fore.RED}no fucking fish detected :/")
