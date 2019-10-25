from abc import ABC, abstractmethod
from Basic import Basic

class Student(Basic):
    def __init__(self, fio = None, age = None, email = None):
        super().__init__(fio, age)
        self.email = email
        self.type = "Студент"
