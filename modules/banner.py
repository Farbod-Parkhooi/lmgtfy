from modules import open
from colorama import init, Fore, Back, Style
from random import randint
from os import system 
from platform import uname
from time import sleep as sp
init()
RESET = Fore.RESET + Back.RESET + Style.RESET_ALL
def clear():
    plat = uname()[0].lower()
    if plat.startswith("win"): system("cls")
    else: system("clear")
def banner():
    banners = ["""
░▒█░░░░░░▒█▀▄▀█░░░▒█▀▀█░░░▀▀█▀▀░░░▒█▀▀▀░░░▒█░░▒█
░▒█░░░░░░▒█▒█▒█░░░▒█░▄▄░░░░▒█░░░░░▒█▀▀░░░░▒▀▄▄▄▀
░▒█▄▄█░░░▒█░░▒█░░░▒█▄▄▀░░░░▒█░░░░░▒█░░░░░░░░▒█░░
""", """
 __        __  __       ___      ____      ____      _  _ 
(  )      (  \/  )     / __)    (_  _)    ( ___)    ( \/ )
 )(__      )    (     ( (_-.      )(       )__)      \  / 
(____)    (_/\/\_)     \___/     (__)     (_)        (__) 
""", """
 ___               _____ ______           ________          _________        ________       ___    ___ 
|\  \             |\   _ \  _   \        |\   ____\        |\___   ___\     |\  _____\     |\  \  /  /|
\ \  \            \ \  \\\__\ \  \       \ \  \___|        \|___ \  \_|     \ \  \__/      \ \  \/  / /
 \ \  \            \ \  \\|__| \  \       \ \  \  ___           \ \  \       \ \   __\      \ \    / / 
  \ \  \____        \ \  \    \ \  \       \ \  \|\  \           \ \  \       \ \  \_|       \/  /  /  
   \ \_______\       \ \__\    \ \__\       \ \_______\           \ \__\       \ \__\      __/  / /    
    \|_______|        \|__|     \|__|        \|_______|            \|__|        \|__|     |\___/ /     
                                                                                          \|___|/   
""", """
88         8b    d8      dP""b8     888888     888888     Yb  dP 
88         88b  d88     dP   `"       88       88__        YbdP  
88  .o     88YbdP88     Yb  "88       88       88""         8P   
88ood8     88 YY 88      YboodP       88       88          dP   
""", """
██╗         ███╗   ███╗     ██████╗     ████████╗    ███████╗    ██╗   ██╗
██║         ████╗ ████║    ██╔════╝     ╚══██╔══╝    ██╔════╝    ╚██╗ ██╔╝
██║         ██╔████╔██║    ██║  ███╗       ██║       █████╗       ╚████╔╝ 
██║         ██║╚██╔╝██║    ██║   ██║       ██║       ██╔══╝        ╚██╔╝  
███████╗    ██║ ╚═╝ ██║    ╚██████╔╝       ██║       ██║            ██║   
╚══════╝    ╚═╝     ╚═╝     ╚═════╝        ╚═╝       ╚═╝            ╚═╝ 
"""]
    rand = randint(0, (len(banners) - 1))
    print(f"{Fore.CYAN + banners[rand]}")
    print(f"{Style.DIM}                Let Me Google It For You!                {RESET}")
def get_opts():
    query = input(f"{Fore.WHITE}[{Fore.YELLOW}+{Fore.WHITE}] {Fore.GREEN}Please write your query{Fore.WHITE}: {RESET}")
    print(f"{Fore.WHITE}[{Fore.YELLOW}+{Fore.WHITE}]{Fore.GREEN} The URL is: '{Fore.LIGHTBLUE_EX}{query}{Fore.GREEN}'{Fore.WHITE}. {RESET}")
    sp(3)
    clear()
    banner()
    out_url = open.create_url(query=query)
    print(f"{Fore.WHITE}[{Fore.YELLOW}+{Fore.WHITE}]{Fore.GREEN} Your URL is: '{Fore.LIGHTBLUE_EX}{out_url}{Fore.GREEN}'{Fore.WHITE}.{RESET}")