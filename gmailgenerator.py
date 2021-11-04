
import time, os, colorama
import sys
import getpass
from colorama import Fore, init
from time import sleep


init(convert=True)
storage = []
banner = (f'''{Fore.RED}
    
░█████╗░░█████╗░░░███╗░░  ░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗░████║░░  ██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██║██║░░██║██╔██║░░  ██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░██║██║░░██║╚═╝██║░░  ██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝╚█████╔╝███████╗  ╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░░╚════╝░╚══════╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

created by 001 Discord : ! 001#6666

    {Fore.RESET}''')
print (banner)

def Clear():
    os.system('cls')

def ask_username():
    username = ""
    while not username:
        temp = input(" > gmaileto bede xD(bedon @gmail.com) ")
        if "@" in temp:
            Clear()
            print(banner)
            print(" >  @ ino nazar kos kesh gaiidi :/ ")
            time.sleep(1.5)
        else:
            Clear()
            print(banner)

            username = temp
    return username


def shuffle(obj, init_pos):
    global storage
    temp = ""
    for i in range(init_pos, len(obj)):
        temp = obj[:i] + "." + obj[i:]
        if temp not in storage:
            if ".." not in temp:
                storage.append(temp)
                shuffle(temp, init_pos+2)
    return storage

target = ask_username().replace(".", "")
shuffle(target, 1)
file = open('001.txt', 'w')
for i in storage:
    temp = str(i) + "@gmail.com"
    file.write(temp)
    file.write("\n")

Clear()
print(banner)
print(" > ok sicktir")
time.sleep(2)
