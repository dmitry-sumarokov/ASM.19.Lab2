from abc import ABC, abstractmethod

class Tancor2(ABC):
    ___dict__ = ('_name', '_age', '_stazh')
    @abstractmethod
    def do_magic(self):
        pass
    @abstractmethod
    def do_print(self):
        pass