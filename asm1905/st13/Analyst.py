from Employee import Employee
from random import randint


class Analyst:
    def __init__(self):
        self.avg_calls_per_day = 0
        pass

    # def __init__(self):
    #     super().__init__()
    #     self.hire_employee()
    #
    # def enter_emp_params(self):
    #     # self.hire_employee()
    #     print('Enter an average number of calls per day: ')
    #     while True:
    #         new_val = input()
    #         if new_val and new_val.isdigit():
    #             self.avg_calls_per_day = int(new_val)
    #             break
    #         else:
    #             print('Enter a NUMBER!!!')
    #             # pass
    #
    # def print_emp_params(self):
    #     return('Position - 			 Analyst\n	Average number of calls per day - %s'%(self.avg_calls_per_day))
    #
    # def print_emp_brief(self):
    #     pass
    #
    # def alter_emp_params(self):
    #     print('Enter a new average number of calls per day: ')
    #     while True:
    #         new_val = input()
    #         if new_val and new_val.isdigit():
    #             self.avg_calls_per_day = int(new_val)
    #             break
    #         else:
    #             print('Enter a NUMBER or just press \'ENTER\'!!!')
    #             pass
    #
    # def emp_special_action(self):
    #     rd = randint(0, 5)
    #     try:
    #         if (self.avg_calls_per_day/rd)%2 == 0:
    #             msg = 'What are you doing???'
    #         else:
    #             msg = 'Are you kidding me??? What does it mean?'
    #     except Exception as e:
    #         msg = 'Something went wrong! f@!%'
    #         pass
    #     return msg
