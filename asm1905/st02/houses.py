from __future__ import annotations
from abc import ABCMeta, abstractmethod  # Python's built-in abstract class library

class house(object):
    is_constructed = True
    
    def __init__ (self, material_type, owner_name="no name", square=0):  
        self.owner_name = owner_name 
        self.square = square 
        self._material_type = material_type
        
    def outputAllInfo(self):
        print("Owner name: ", self.owner_name)
        print("House square: ", self.square, " m2")
        self.material_type()
        
    def setAllInfo(self, owner_name, square):
        self.owner_name = owner_name if owner_name else self.owner_name
        self.square = square if square else self.square
        #self.material_type = material_type

    #@property
    def material_type(self):
        """
        Контекст хранит ссылку на один из объектов Стратегии. Контекст не знает
        конкретного класса стратегии. Он должен работать со всеми стратегиями
        через интерфейс Стратегии.
        """
        self._material_type.do_algorithm()
        
    # @material_type.setter
    # def material_type(self, material_type: materialType) -> None:
        # """
        # Обычно Контекст позволяет заменить объект Стратегии во время выполнения.
        # """
        # self._material_type = material_type
    
    
class materialType(object):
    __metaclass__ = ABCMeta
    """
    Интерфейс Стратегии объявляет операции, общие для всех поддерживаемых версий
    некоторого алгоритма.

    Контекст использует этот интерфейс для вызова алгоритма, определённого
    Конкретными Стратегиями.
    """
    @abstractmethod
    def do_algorithm(self):
        """Required Method"""
        pass