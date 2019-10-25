from abc import ABC


class Student(ABC):

    def __init__(self, type_student, behavior, data=None):
        self._student = type_student
        self._behavior = behavior
        self.input_info() if data is None else self.input_info(data)

    def input_info(self, data=None):
        self._behavior.do_input(self._student) if data is None else self._behavior.do_input(self._student, data)

    def print_info(self, index):
        return self._behavior.do_print(self._student, index)

    def edit_student(self, data=None):
        return self._behavior.do_edit(self._student) if data is None else self._behavior.do_edit(self._student, data)

    def magic(self):
        return self._behavior.do_magic(self._student)
