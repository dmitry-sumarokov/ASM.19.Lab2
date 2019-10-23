from abc import ABC, abstractmethod

class Basic(ABC):
    @abstractmethod
    def __init__(self, fio = None, age = None):
        self.ids = 0
        self.fio = fio
        self.age = age
        self.type = None
