import os.path
import pickle

from colorama import Fore

from .commonFunctions import return_number
from .employee import Employee
from .menuItems import ADDITION_MENU


class ScrumTeam:
    __slots__ = ('lala', 'employees')

    def __init__(self):
        self.employees = []

    @staticmethod
    def get_fields(num) -> list:
        e = ADDITION_MENU[num]
        employee = Employee(e[1], e[2])
        return employee.fields_list()

    def add_employee(self, employee):
        return self.employees.append(employee)

    def edit_employee(self):
        self.employees[return_number()].edit()
        print(Fore.YELLOW + 'Saved!')

    def remove_employee(self):
        self.employees.pop(return_number())
        print(Fore.YELLOW + 'Deleted!')

    def show_scrum_team(self):
        for i, employee in enumerate(self.employees):
            print(Fore.MAGENTA + '~Employee №' + str(i) + '~')
            employee.print_data()

    def listen_personal(self):
        self.employees[return_number()].saying()

    # The pickle module implements binary protocols for serializing and de-serializing a Python object structure.
    # “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling”
    # is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back
    # into an object hierarchy.
    def save_to_file(self):
        fn = input(Fore.CYAN + 'Enter file name: ')
        try:
            file = open(
                os.path.join(os.path.abspath(__name__).replace('.st21.scrumTeam', '/st21'),
                             fn
                             ), 'wb')
        except IOError:
            file = open(os.path.join(os.path.abspath(__name__).replace('.st21.scrumTeam', '/st21'),
                                     fn
                                     ), 'xb')
        pickle.dump(self.employees, file)
        print(Fore.MAGENTA + 'Saved to "' + fn + '" file!')

    def load_from_file(self):
        # fn = input(Fore.CYAN + 'Enter file name: ')
        try:
            print(os.path.abspath(__name__))
            file = open('afaf', 'rb')
            self.employees = pickle.load(file)
            # print(Fore.MAGENTA + 'Loaded from "' + fn + '" file!')
        except IOError:
            print(Fore.MAGENTA + 'File doesn`t exist!')
