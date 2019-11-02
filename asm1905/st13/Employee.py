from abc import ABC


class Employee(ABC):
    def __init__(self, emp_type, action):
        self.employee = emp_type
        self.action = action
        self.nickname = ''
        self.exp = 0
        self.sex = ''
        self.age = 0
        self.enter_emp_params()

    def enter_emp_params(self):
        self.action.hire_alter_employee(self.employee, 0)
        pass

    def print_emp_params(self, number):
        self.action.print_employees(self.employee, number)
        pass

    def print_emp_brief(self, number):
        self.action.print_brief(self.employee, number)
        pass

    def alter_emp_params(self):
        self.action.hire_alter_employee(self.employee, 1)
        pass

    def emp_special_action(self):
        self.action.print_special_action(self.employee)
        pass

    # def hire_employee(self):
    #     print('Enter employee\'s nickname: ')
    #     self.nickname = input()
    #
    #     print('Enter employee\'s working experience: ')
    #     while True:
    #         exp = input()
    #         if exp.isdigit():
    #             self.exp = int(exp)
    #             break
    #         else:
    #             print('Enter a NUMBER!')
    #             pass
    #
    #     print('Enter employee\'s sex (M - man or F - female): ')
    #     while True:
    #         sex = input().upper()
    #         if sex in ('M', 'F'):
    #             self.sex = sex
    #             break
    #         else:
    #             print('Enter M or F!')
    #             pass
    #
    #     print('Enter employee\'s age: ')
    #     while True:
    #         age = input()
    #         if age.isdigit():
    #             self.age = int(age)
    #             break
    #         else:
    #             print('Enter a NUMBER!')
    #             pass
    #
    #     self.enter_emp_params()
    #
    # def print_employees(self, number):
    #     print('%s.  Nickname - 			 %s\n    Working experience - %s\n    Sex - 				 %s\n    Age - 	'
    #           '			 %s\n%s'
    #           % (number, self.nickname, self.exp, self.sex, self.age,
    #              self.print_emp_params()))
#
