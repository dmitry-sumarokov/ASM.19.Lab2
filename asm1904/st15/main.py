import os
import flask
import cgi
__path__ = [os.path.dirname(os.path.abspath(__file__))]
from .Office import Office
from .functions import *
office = Office()
MENU = {"1": ['Add a department', office.Add_Department],
		"2": ['Add an employee', office.Add_Employee],
		"3": ['Edit Database', office.EditDB],
		"4": ['Show Database', office.ShowDB],
		"5": ['Save Database', office.SaveDB],
		"6": ['Load Database', office.loadDB],
		"7": ['Clear the Database', office.ClearDB],
		"8": ['Exit']
		}


def main():
	show_menu(MENU)
	while (True):
		choice = input("Choose item from menu")
		if is_int(choice):
			if int(choice) == 8:
				break
			for i in MENU:
				if (i==choice):
					MENU[choice][1]()
		else:
			print("Choose smth!")


if __name__ == "__main__":
	main()





