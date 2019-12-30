from abc import ABC

from colorama import Fore

from .commonFunctions import return_number


class Employee(ABC):

    def __init__(self, e_type, behavior):
        self._employee = e_type
        self._behavior = behavior

    def fields_list(self) -> list:
        return self._behavior.get_full_fields()

    def print_data(self):
        self._behavior.show(self._employee)

    def edit(self):
        self._behavior.edit(self._employee)

    def saying(self):
        self._behavior.personal()


class Behavior:
    @staticmethod
    def get_basic_fields() -> list:
        return ['Name', 'Age', 'Type']

    @staticmethod
    def show_data(employee):
        print(Fore.GREEN + 'Name: ' + employee.name + '\nAge: ' + str(employee.age))

    @staticmethod
    def edit(employee):
        employee.name = input('Name: ')
        employee.age = return_number('Age: ')
