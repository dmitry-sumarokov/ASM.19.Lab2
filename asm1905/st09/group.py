import os
import pickle

from employee import Chief, Engeneer, Specialist, ChiefSpecialist

MENU = [
    ('Начальник', Chief),
    ('Инженер', Engeneer),
    ('Специалист', Specialist),
    ('Главного специалист', ChiefSpecialist)
]


class Group:

    def __init__(self):
        self.employee_list = []

    @staticmethod
    def get_employee_type(obj):
        for x in MENU:
            if obj.__class__.__name__ == x[1].__name__:
                return x[0]

    def add_employee(self, cls_idx, **kwargs):
        context = MENU[int(cls_idx)][1]()
        context.do_init(kwargs)
        self.employee_list.append(context)

    def edit_employee(self, emp_idx, **kwargs):
        self.employee_list[emp_idx].do_init(kwargs)

    def remove_employee(self, emp_idx):
        self.employee_list.pop(emp_idx)

    def clear_group(self):
        self.employee_list.clear()

    def save_to_file(self):
        filepath = './save.pkl'
        with open(filepath, 'wb') as f:
            pickle.dump(self.employee_list, f)

    def load_from_file(self):
        filepath = './save.pkl'
        with open(filepath, 'rb') as f:
            self.employee_list = pickle.load(f)

    def do_magic(self, emp_idx):
        self.employee_list[emp_idx].do_magic_logic()
