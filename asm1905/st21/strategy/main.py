from .scrumTeam import ScrumTeam
from colorama import init
from colorama import Fore
from .menuItems import MENU
from .commonFunctions import get_menu_input
import os

scrumTeam = ScrumTeam()


def main():
    init()
    print(Fore.MAGENTA + '~~~ You were accepted as head of our HR Departament! ~~~')
    print(Fore.CYAN + 'Feel free to change/add/delete positions')

    try:
        while 1:
            getattr(scrumTeam, MENU[int(get_menu_input(MENU))][1])()
    except Exception as e:
        print(Fore.MAGENTA + e + ' ~YOU DIED~ ')


if __name__ == '__main__':
    main()
