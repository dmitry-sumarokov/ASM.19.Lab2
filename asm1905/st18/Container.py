from abc import ABC, abstractmethod
import pickle
from enum import Enum

from Basic import Basic
from Student import Student
from Headman import Headman

element_type = Enum('element_type', 'student headman')

class Container():
    def __init__(self):
        self.ids = 1
        self.my_list = []
    def read_data(self, filename):
        with open(filename, 'rb') as f:
            my_list_new = []
            my_list_new = pickle.load(f)
            for el in my_list_new:
                el.ids = self.ids
                self.my_list.append(el)
                self.ids += 1
    def write_data(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.my_list, f)
    def add_element(self, element):
        element.ids = self.ids
        self.ids += 1
        self.my_list.append(element)
    def del_element(self, ids):
        idx = self.find_index(ids)
        if(idx >= 0):
            self.my_list.pop(idx)
    def edit_element(self, element, idx):
        self.my_list[idx] = element
    def clear(self):
        self.my_list.clear()
        self.ids = 1
    def find_index(self, ids):
        count = 0
        for el in self.my_list:
            if(int(el.ids) == int(ids)):
                return count
            count += 1
        return (-1)
