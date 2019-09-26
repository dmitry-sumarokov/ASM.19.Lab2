from abc import ABC, abstractmethod


class Worker(ABC):
    ___dict__ = ('_first_name', '_second_name', '_gender', '_age')
    @abstractmethod
    def do_magic(self):
        pass
    @abstractmethod
    def do_init(self):
        pass
    @abstractmethod
    def do_print(self):
        pass


