import os
import pickle
from flask import render_template, request, redirect

from Employee import Employee

from CommonActions import CommonActions

from Analyst import Analyst
from AnalystAction import AnalystAction

# from DevOps import DevOps
# from DevOpsAction import DevOpsAction

from DB_Dev import DB_Dev
from DB_DevAction import DB_DevAction

# from Backend_Dev import Backend_Dev
# from Backend_DevAction import Backend_DevAction
#
# from Frontend_Dev import Frontend_Dev
# from Frontend_DevAction import Frontend_DevAction


class ACS_SC_dep:
    def __init__(self):
        # self.employees = []
        self.menu = (('Add Analyst', Analyst, AnalystAction),
                     ('Add DB Dev', DB_Dev, DB_DevAction))
        try:
            self.load_from_file()
        except:
            self.employees = []

    def Dep(self):
        dep = ''
        for i, emp in enumerate(self.employees):
            dep += emp.print_emp_params(i, 1)
        dep += render_template("actions.tpl")
        return dep

    def Head(self):
        return render_template("head.tpl")

    def Body(self):
        return render_template("body.tpl")

    def Get_Employee(self, id):
        if id < 0:
            emp = Employee(self.menu[-id-1][1], self.menu[-id-1][2])
            return emp
        else:
            return self.employees[id]

    def Alter_Employee(self, id):
        # return render_template("hire.tpl")
        # return id
        # return emp.nickname
        # return render_template("hire.tpl", **emp.dict(id))
        emp = self.Get_Employee(id)
        return emp.print_emp_params(id, 0)
        # render_template("hire.tpl", **emp.print_emp_params(int(id)))
        # context = {'nickname': 'self.nickname', 'exp': 0, 'sex': 'self.sex', 'age': 18, 'id': id}
        # return render_template("hire.tpl", **context)

    def Hire_Employee(self):
        id = int(request.form.get('id', None))

        emp = self.Get_Employee(id)
        emp.alter_emp_params()

        if id < 0:
            self.employees.append(emp)
            # return render_template("hire.tpl")

        return self.Dep()


    def Delete_Employee(self, id):
        self.employees.pop(id)
        return self.Dep()
    # def main_menu(self):
    #     print("------------------------------")
    #     for i, item in enumerate(self.menu):
    #         print("{0:2}. {1}".format(i, item[0]))
    #     print("------------------------------")
    #     while True:
    #         emp_type = input()
    #         if emp_type.isdigit():
    #             break
    #         else:
    #             print('Enter a NUMBER!')
    #             pass
    #     return int(emp_type)

    # def special_action(self):
    #     for i, item in enumerate(self.employees):
    #         item.print_emp_brief(i)
    #
    #     print('Enter a number of employee you\'d like to show special action or just press \'ENTER\': ')
    #     while True:
    #         n_emp = input()
    #         if n_emp.isdigit():
    #             self.employees[int(n_emp)].emp_special_action()
    #             break
    #         elif n_emp == '':
    #             return
    #         else:
    #             print('You should enter a NUMBER or just press \'ENTER\'')
    #             pass
    #
    # def hire_employee(self):
    #     n = self.main_menu()
    #     self.employees.append(Employee(self.menu[n][1], self.menu[n][2]))
    #     print('Hired successfully')
    #
    # def fire_employee(self):
    #     for i, item in enumerate(self.employees):
    #         item.print_emp_brief(i)
    #
    #     print('Enter a number of employee you\'d like to fire or just press \'ENTER\': ')
    #     while True:
    #         n_emp = input()
    #         if n_emp.isdigit():
    #             self.employees.pop(int(n_emp))
    #             break
    #         elif n_emp == '':
    #             return
    #         else:
    #             print('You should enter a NUMBER or just press \'ENTER\'')
    #             pass
    #     print('Fired successfully')
    #
    # def close_dep(self):
    #     self.employees.clear()
    #     print('Dep closed successfully')
    #
    # def alter_employee(self):
    #     for i, item in enumerate(self.employees):
    #         item.print_emp_brief(i)
    #
    #     print('Enter a number of employee you\'d like to alter or just press \'ENTER\': ')
    #     while True:
    #         n_emp = input()
    #         if n_emp.isdigit():
    #             self.employees[int(n_emp)].alter_emp_params()
    #             break
    #         elif n_emp == '':
    #             return
    #         else:
    #             print('You should enter a NUMBER or just press \'ENTER\'')
    #             pass
    #     print('Altered successfully')
    #
    # def print_emp_list(self):
    #     for i, item in enumerate(self.employees):
    #         item.print_emp_params(i)
    #
    def save_to_file(self):
        with open(os.path.join(os.path.abspath(__name__).replace('\Dep', '\\'), 'dep.dat'), 'wb') as f:
            pickle.dump(self.employees, f)
        # f.close()
        # print('Saved successfully')

    def load_from_file(self):
        with open(os.path.join(os.path.abspath(__name__).replace('\Dep', '\\'), 'dep.dat'), 'rb') as f:
            self.employees = pickle.load(f)
        # f.close()
        # print('Load successfully')

    # def f(self):
    # 	print("asm1905.st13.group.f()")
