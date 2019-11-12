from .employee import Behavior
from .commonFunctions import return_number


class ScrumMaster:
    __slots__ = ('name', 'age', 'projects')

    def __init__(self):
        pass


class ScrumMasterBehavior:
    @staticmethod
    def addition(employee):
        Behavior.input_data(employee)
        employee.projects = return_number('Projects: ')

    @staticmethod
    def show(employee):
        print('Scrum master:')
        Behavior.show_data(employee)
        print('Projects: ', str(employee.projects))

    @staticmethod
    def edit(employee):
        Behavior.edit(employee)
        employee.projects = return_number('Projects: ')

    @staticmethod
    def personal():
        print('We are only one month late!')
