from .commonFunctions import return_number
from .employee import Behavior


class ScrumMaster:
    __slots__ = ('name', 'age', 'projects')

    def __init__(self):
        pass


class ScrumMasterBehavior:
    @staticmethod
    def get_full_fields() -> list:
        temp = Behavior.get_basic_fields()
        temp.append('Projects')
        return temp

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
