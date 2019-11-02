from CommonActions import CommonActions
from random import randint


class DevOpsAction:
    def __init__(self):
        pass

    def hire_alter_employee(devops, hire_alter):
        CommonActions.hire_alter_employee(devops, hire_alter)

        if hire_alter == 0:
            print('Enter a salary for almighty one: ')
        elif hire_alter == 1:
            print('Enter a new salary: ')
        while True:
            new_val = input()
            if new_val and new_val.isdigit():
                devops.salary = int(new_val)
                break
            else:
                print('Enter a NUMBER!!!')
                pass

    # def alter_emp_params(devops):
    #     CommonActions.hire_alter_employee(devops, 1)
    #
    #     print('Enter a new salary: ')
    #     while True:
    #         new_val = input()
    #         if new_val and new_val.isdigit():
    #             devops.salary = int(input())
    #         else:
    #             print('Enter a NUMBER or just press \'ENTER\'!!!')
    #             pass

    def print_employees(devops, number):
        CommonActions.print_employees(devops, number)
        print('    Position - DevOps. Salary - %s' % (devops.salary))

    def print_special_action(devops):
        rd = randint(0, 10)
        try:
            if devops.salary * rd > devops.salary * 5:
                msg = 'God mode is ON!!!'
            else:
                msg = 'You lost your privileges)'
        except Exception as e:
            msg = 'Something went wrong! f@!%'
            pass
        print(msg)

    def print_brief(devops, number):
        CommonActions.print_brief(devops, number)
        pass
