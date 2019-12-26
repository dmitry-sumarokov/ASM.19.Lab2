from abc import ABC, abstractmethod

class Technic(ABC):
    ___dict__ = ('_brend', '_color', '_year')
    @abstractmethod
    def do_it(self):
        pass
    @abstractmethod
    def do_print(self):
        pass
