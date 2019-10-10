from .Employee import Employee
from random import randint

class Frontend_Dev(Employee):
    def enter_emp_params(self):
        print('Enter the number of eaten fruits per day: ')
        while True:
            new_val = input()
            if new_val and new_val.isdigit():
                self.fruits = int(new_val)
                break
            else:
                print('Enter a NUMBER!!!')
                # pass

    def print_emp_params(self):
        return ('Position - Frontend Dev. Number of eaten fruits per day - %s' % (self.fruits))

    def print_emp_brief(self):
        pass

    def alter_emp_params(self):
        print('Enter a new number of eaten fruits per day: ')
        while True:
            new_val = input()
            if new_val and new_val.isdigit():
                self.fruits = int(input())
            else:
                print('Enter a NUMBER or just press \'ENTER\'!!!')
                pass

    def emp_special_action(self):
        rd = randint(0, 10)
        try:
            if self.fruits / rd > 3:
                msg = 'Om-nom-nom'
            else:
                msg = 'True JS Dev can\'t live without fruits. My precious '
        except Exception as e:
            msg = 'Something went wrong! f@!% '
            pass
        return msg