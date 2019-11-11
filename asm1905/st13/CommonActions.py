# from .Employee import Employee
from random import randint
from flask import render_template, request


class CommonActions:
    def __init__(self):
        pass

    def hire_alter_employee(employee):
        employee.nickname = request.form.get('nickname')
        employee.exp = request.form.get('exp')
        employee.sex = request.form.get('sex')
        employee.age = int(request.form.get('age'))

    def print_employees(employee, id):
        context = {'nickname': employee.nickname, 'exp': employee.exp, 'sex': employee.sex, 'age': employee.age, 'id': id}
        return context

    def print_brief(employee, number):
        print('%s.  Nickname - %s\n'
            % (number, employee.nickname))


    # def alter_emp_params(employee):
    #
    #
    #     print('Enter employee\'s nickname: ')
    #     new_nickname = input()
    #     if new_nickname:
    #         employee.employee.nickname = new_nickname
    #
    #     print('Enter employee\'s working experience: ')
    #     while True:
    #         new_exp = input()
    #         if new_exp.isdigit():
    #             employee.employee.exp = int(new_exp)
    #             break
    #         else:
    #             print('You should enter a NUMBER or just press \'ENTER\'')
    #             pass
    #
    #     print('Enter employee\'s sex (M - man or F - female): ')
    #     while True:
    #         new_sex = input().upper()
    #         if new_sex in ('M', 'F'):
    #             employee.employee.sex = new_sex
    #             break
    #         else:
    #             print('You should enter M or F or just press \'ENTER\'')
    #             pass
    #
    #     print('Enter employee\'s age: ')
    #     while True:
    #         new_age = input()
    #         if new_age.isdigit():
    #             employee.employee.age = int(new_age)
    #             break
    #         else:
    #             print('You should enter a NUMBER or just press \'ENTER\'')
    #             pass

    # def print_emp_params(self, number):
    #     self.employee.print_employees(number)
    #
    # def print_emp_brief(self, number):
    #     print('%s.  Nickname - %s\n'
    #           % (number, self.employee.nickname))
    #
    #
    #
    # def emp_special_action(self):
    #     print(self.employee.emp_special_action())
