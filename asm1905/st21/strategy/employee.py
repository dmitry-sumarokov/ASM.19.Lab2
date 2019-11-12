from abc import ABC
from .commonFunctions import return_number
from colorama import Fore


class Employee(ABC):

    def __init__(self, e_type, behavior):
        self._employee = e_type
        self._behavior = behavior
        self._input_data()

    def _input_data(self):
        self._behavior.addition(self._employee)

    def print_data(self):
        self._behavior.show(self._employee)

    def edit(self):
        self._behavior.edit(self._employee)

    def saying(self):
        self._behavior.personal()


class Behavior:
    @staticmethod
    def input_data(employee):
        employee.name = input('Name: ')
        employee.age = return_number('Age: ')

    @staticmethod
    def show_data(employee):
        print(Fore.GREEN + 'Name: ' + employee.name + '\nAge: ' + str(employee.age))

    @staticmethod
    def edit(employee):
        employee.name = input('Name: ')
        employee.age = return_number('Age: ')
