# from .Employee import Employee
# from random import randint


class Backend_Dev:
    def __init__(self):
        self.bugs = 0
        pass


    # def enter_emp_params(self):
    #     print('Enter the number of PHP bugs per day: ')
    #     while True:
    #         new_val = input()
    #         if new_val and new_val.isdigit():
    #             self.bugs = int(new_val)
    #             break
    #         else:
    #             print('Enter a NUMBER!!!')
    #
    # def print_emp_params(self):
    #     return ('Position - Backend Dev. Number of PHP bugs per day - %s' % (self.bugs))
    #
    # def print_emp_brief(self):
    #     pass
    #
    # def alter_emp_params(self):
    #     print('Enter a new number of PHP bugs: ')
    #     while True:
    #         new_val = input()
    #         if new_val and new_val.isdigit():
    #             self.bugs= int(input())
    #         else:
    #             print('Enter a NUMBER or just press \'ENTER\'!!!')
    #             pass
    #
    # def emp_special_action(self):
    #     rd = randint(0, 10)
    #     try:
    #         if self.bugs * rd > 100:
    #             msg = 'Need fixing! As faster as can'
    #         else:
    #             msg = 'Nobody will believe you anyway'
    #     except Exception as e:
    #         msg = 'Something went wrong! f@!% '
    #         pass
    #     return msg
