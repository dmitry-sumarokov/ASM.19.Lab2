from .commonFunctions import return_number
from .employee import Behavior


class Developer:
    __slots__ = ('name', 'age', 'experience')

    def __init__(self):
        pass


class DeveloperBehavior:
    @staticmethod
    def get_full_fields() -> list:
        temp = Behavior.get_basic_fields()
        temp.append('Experience (years)')
        return temp

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
