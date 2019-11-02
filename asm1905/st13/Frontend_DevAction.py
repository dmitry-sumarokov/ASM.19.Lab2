from CommonActions import CommonActions
from random import randint


class Frontend_DevAction:
    def __init__(self):
        pass

    def hire_alter_employee(frontend, hire_alter):
        CommonActions.hire_alter_employee(frontend, hire_alter)

        if hire_alter == 0:
            print('Enter the number of eaten fruits per day: ')
        elif hire_alter == 1:
            print('Enter a new number of eaten fruits per day: ')
        while True:
            new_val = input()
            if new_val and new_val.isdigit():
                frontend.fruits = int(new_val)
                break
            else:
                print('Enter a NUMBER!!!')
                # pass

    # def alter_emp_params(frontend):
    #     CommonActions.hire_alter_employee(frontend, 1)
    #
    #     print('Enter a new number of eaten fruits per day: ')
    #     while True:
    #         new_val = input()
    #         if new_val and new_val.isdigit():
    #             frontend.fruits = int(input())
    #         else:
    #             print('Enter a NUMBER or just press \'ENTER\'!!!')
    #             pass

    def print_employees(frontend, number):
        CommonActions.print_employees(frontend, number)
        print('   Position - Frontend Dev. Number of eaten fruits per day - %s' % (frontend.fruits))

    def print_special_action(frontend):
        rd = randint(0, 10)
        try:
            if frontend.fruits / rd > 3:
                msg = 'Om-nom-nom'
            else:
                msg = 'True JS Dev can\'t live without fruits. My precious '
        except Exception as e:
            msg = 'Something went wrong! f@!% '
            pass
        print(msg)

    def print_brief(frontend, number):
        CommonActions.print_brief(frontend, number)
        pass