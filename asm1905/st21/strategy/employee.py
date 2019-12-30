from abc import ABC

from .commonFunctions import return_number


class Employee(ABC):

    def __init__(self, e_type, behavior):
        self._employee = e_type
        self._behavior = behavior

    def get_type(self) -> str:
        return self._employee.__name__

    def fields_list(self) -> list:
        return self._behavior.get_full_fields()

    def edit(self):
        self._behavior.edit(self._employee)

    def saying(self):
        self._behavior.personal()


class Behavior:
    @staticmethod
    def get_basic_fields() -> list:
        return ['Name', 'Age']

    @staticmethod
    def edit(employee):
        employee.name = input('Name: ')
        employee.age = return_number('Age: ')
