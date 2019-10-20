from abc import ABC, abstractmethod
from Basic import Basic

class Headman(Basic):
    def __init__(self, fio = None, age = None, tel_number = None):
        super().__init__(fio, age)
        self.tel_number = tel_number
        self.type = "Староста"
