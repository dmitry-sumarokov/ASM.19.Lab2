from .commonFunctions import return_number
from .employee import Behavior


class ProductOwner:
    __slots__ = ('name', 'age', 'payment')

    def __init__(self):
        pass


class ProductOwnerBehavior:
    @staticmethod
    def get_full_fields() -> list:
        temp = Behavior.get_basic_fields()
        temp.append('Payment (EUR)')
        return temp

    @staticmethod
    def edit(employee):
        Behavior.edit(employee)
        employee.payment = return_number('Payment (EUR): ')

    @staticmethod
    def personal():
        print('Can you make this black AND white at the same time?')
