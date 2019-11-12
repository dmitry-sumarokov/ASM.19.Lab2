from .employee import Behavior
from .commonFunctions import return_number


class Developer:
    __slots__ = ('name', 'age', 'experience')

    def __init__(self):
        pass


class DeveloperBehavior:
    @staticmethod
    def addition(employee):
        Behavior.input_data(employee)
        employee.experience = return_number('Experience (years): ')

    @staticmethod
    def show(employee):
        print('Developer:')
        Behavior.show_data(employee)
        print('Experience (years): ', str(employee.experience))

    @staticmethod
    def edit(employee):
        Behavior.edit(employee)
        employee.experience = return_number('Experience (years): ')

    @staticmethod
    def personal():
        print('We will release new feature on Friday!')
