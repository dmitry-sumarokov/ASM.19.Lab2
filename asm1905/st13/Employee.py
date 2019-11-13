from abc import ABC
from flask import render_template, request


class Employee(ABC):
    def __init__(self, emp_type, action):
        self.employee = emp_type
        self.action = action
        self.nickname = ''
        self.exp = 0
        self.sex = ''
        self.age = 0
        self.unique = self.enter_emp_params()

    def enter_emp_params(self):
        self.action.hire_alter_employee(self.employee, 0)

    def print_emp_params(self, id, act):
        # context = [id,'nickname', 'exp', 'sex', 'age']
        # context['id'] = id
        # context['nickname'] = self.nickname
        # context['exp'] = self.exp
        # context['sex'] = self.sex
        # context['age'] = self.age
        # return render_template(tpl, **context)
        context = {'nickname': self.nickname, 'exp': self.exp, 'sex': self.sex, 'age': self.age, 'unique': self.unique, 'id': id}
        tpl = self.action.print_employees(self.employee, act)
        return render_template(tpl, **context)
        # render_template("hire.tpl", **context)



    def print_emp_brief(self, number):

        self.action.print_brief(self.employee, number)
        pass

    def alter_emp_params(self):
        self.nickname = request.form.get('nickname')
        self.exp = int(request.form.get('exp'))
        self.sex = request.form.get('sex')
        self.age = int(request.form.get('age'))
        self.unique = self.action.hire_alter_employee(self.employee, 1)

    def emp_special_action(self):
        self.action.print_special_action(self.employee)
        pass

    def dict(self, id):
        context = {'nickname': self.nickname, 'exp': self.exp, 'sex': self.sex, 'age': self.age, 'id': id}
        return context

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
