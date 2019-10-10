from .Employee import Employee
from .Common_Params import Common_Params
from random import randint

class Analyst(Common_Params):
    def __init__(self):
        super().__init__()
        self.avg_calls_per_day = None
        self.employee = Employee
        Common_Params.hire_employee(self)

    def enter_emp_params(self):


        print('Enter an average number of calls per day: ')
        while True:
            new_val = input()
            if new_val and new_val.isdigit():
                self.avg_calls_per_day = int(new_val)
                break
            else:
                print('Enter a NUMBER!!!')
                # pass

    def print_emp_params(self, n):
        Common_Params.print_emps(self, n)

    def print_unique_param(self):
        print('    Position - 			 Analyst\n    Average number of calls per day - %s\n\n\n' % self.avg_calls_per_day)

    def print_emp_brief(self, n):
        Common_Params.print_emps_brief(self, n)

    def alter_emp_params(self):
        Common_Params.alter_emp(self)

    def alter_emp_unique_param(self):
        print('Enter a new average number of calls per day: ')
        while True:
            new_val = input()
            if new_val and new_val.isdigit():
                self.avg_calls_per_day = int(new_val)
                break
            else:
                print('Enter a NUMBER or just press \'ENTER\'!!!')
                pass

    def emp_special_action(self):
        rd = randint(0, 5)
        try:
            if (self.avg_calls_per_day/rd)%2 == 0:
                msg = 'What are you doing???'
            else:
                msg = 'Are you kidding me??? What does it mean?'
        except Exception as e:
            msg = 'Something went wrong! f@!%'
            pass
        return msg
