from .employee import Behavior
from .commonFunctions import return_number


class ProductOwner:
    __slots__ = ('name', 'age', 'payment')

    def __init__(self):
        pass


class ProductOwnerBehavior:
    @staticmethod
    def addition(employee):
        Behavior.input_data(employee)
        employee.payment = return_number('Payment (EUR): ')

    @staticmethod
    def show(employee):
        print('Product owner:')
        Behavior.show_data(employee)
        print('Payment: ', str(employee.payment))

    @staticmethod
    def edit(employee):
        Behavior.edit(employee)
        employee.payment = return_number('Payment (EUR): ')

    @staticmethod
    def personal():
        print('Can you make this black AND white at the same time?')
