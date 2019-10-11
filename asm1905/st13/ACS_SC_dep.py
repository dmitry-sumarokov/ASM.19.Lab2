import os
import pickle

from .Employee import Employee
from .Analyst import Analyst
from .DevOps import DevOps
from .DB_Dev import DB_Dev
from .Backend_Dev import Backend_Dev
from .Frontend_Dev import Frontend_Dev


class ACS_SC_dep:
    def __init__(self):
        self.menu = (('Add Analyst', Analyst),
                     ('Add DevOps', DevOps),
                     ('Add BD Dev', DB_Dev),
                     ('Add Backend Dev', Backend_Dev),
                     ('Add Frontend Dev', Frontend_Dev))
        self.employees = []

    def main_menu(self):
        print("------------------------------")
        for i, item in enumerate(self.menu):
            print("{0:2}. {1}".format(i, item[0]))
        print("------------------------------")
        return int(input())

    def special_action(self):
        for i, item in enumerate(self.employees):
            item.print_emp_brief(i)

        print('Enter a number of employee you\'d like to show special action or just press \'ENTER\': ')
        while True:
            n_emp = input()
            if n_emp.isdigit():
                self.employees[int(n_emp)].emp_special_action()
                break
            elif n_emp == '':
                return
            else:
                print('You should enter a NUMBER or just press \'ENTER\'')
                pass

    def hire_employee(self):
        emp = self.menu[self.main_menu()][1]()
        emp.enter_emp_params()
        self.employees.append(emp)
        print('Hired successfully')

    def fire_employee(self):
        for i, item in enumerate(self.employees):
            item.print_emps_brief(i)

        print('Enter a number of employee you\'d like to fire or just press \'ENTER\': ')
        while True:
            n_emp = input()
            if n_emp.isdigit():
                self.employees.pop(int(n_emp))
                break
            elif n_emp == '':
                return
            else:
                print('You should enter a NUMBER or just press \'ENTER\'')
                pass
        print('Fired successfully')

    def close_dep(self):
        self.employees.clear()
        print('Dep closed successfully')

    def alter_employee(self):
        for i, item in enumerate(self.employees):
            print('%s.  Nickname - %s\n'
                  % (i, item.employee.nickname))

        print('Enter a number of employee you\'d like to alter or just press \'ENTER\': ')
        while True:
            n_emp = input()
            if n_emp.isdigit():
                self.employees[int(n_emp)].alter_emp_params()
                self.employees[int(n_emp)].alter_emp_unique_param()
                break
            elif n_emp == '':
                return
            else:
                print('You should enter a NUMBER or just press \'ENTER\'')
                pass
        print('Altered successfully')
        # pass

    def print_emp_list(self):
        for i, item in enumerate(self.employees):
            item.print_emps(i)
            item.print_unique_param()

    def save_to_file(self):
        if self.employees:
            with open(os.path.join(os.path.abspath(__name__).replace('.st13.ACS_SC_dep', '/st13'), 'dep.dat'), 'wb') as f:
                pickle.dump(self.employees, f)
            f.close()
            print('Saved successfully')
        else:
            print('Nothing to save')

    def load_from_file(self):
        with open(os.path.join(os.path.abspath(__name__).replace('.st13.ACS_SC_dep', '/st13'), 'dep.dat'), 'rb') as f:
            self.employees = pickle.load(f)
        f.close()
        print('Load successfully')

    # def f(self):
    # 	print("asm1905.st13.group.f()")
