from CommonActions import CommonActions
from random import randint


class Backend_DevAction:
    def __init__(self):
        pass

    def hire_alter_employee(backend, hire_alter):
        CommonActions.hire_alter_employee(backend, hire_alter)

        if hire_alter == 0:
            print('Enter the number of PHP bugs per day: ')
        elif hire_alter == 1:
            print('Enter a new number of PHP bugs: ')
        while True:
            new_val = input()
            if new_val and new_val.isdigit():
                backend.bugs = int(new_val)
                break
            else:
                print('Enter a NUMBER!!!')
                pass

    # def alter_emp_params(backend):
    #     CommonActions.hire_alter_employee(backend, 1)
    #
    #     print('Enter a new number of PHP bugs: ')
    #     while True:
    #         new_val = input()
    #         if new_val and new_val.isdigit():
    #             backend.bugs = int(input())
    #         else:
    #             print('Enter a NUMBER or just press \'ENTER\'!!!')
    #             pass

    def print_employees(backend, number):
        CommonActions.print_employees(backend, number)
        print('Position - Backend Dev. Number of PHP bugs per day - %s' % (backend.bugs))

    def print_special_action(backend):
        rd = randint(0, 10)
        try:
            if backend.bugs * rd > 100:
                msg = 'Need fixing! As faster as can'
            else:
                msg = 'Nobody will believe you anyway'
        except Exception as e:
            msg = 'Something went wrong! f@!% '
            pass
        print(msg)

    def print_brief(backend, number):
        CommonActions.print_brief(backend, number)
        pass
