from abc import ABC, abstractmethod


class Worker(ABC):
    @abstractmethod
    def do_magic(self):
        pass
    @abstractmethod
    def do_print(self):
        pass
