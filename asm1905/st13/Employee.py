from abc import ABC


class Employee(ABC):
    def __init__(self):
        self.nickname = ''
        self.exp = 0
        self.sex = ''
        self.age = 0
        self.type = None

    def enter_emp_params(self):
        pass

    def print_emp_params(self, n):
        pass

    def print_emp_brief(self, n):
        pass

    def print_unique_param(self):
        pass

    def alter_emp_params(self):
        pass

    def emp_special_action(self):
        pass
