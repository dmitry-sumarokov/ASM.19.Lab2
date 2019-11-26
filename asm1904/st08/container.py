import pickle
from os import path

import tea as _tea


class Container:

    _database = "asm1904/st08/database.dat"

    def __init__(self):
        self._list = []
        self.tea = [_tea.ChineseTea, _tea.IndianTea]

    def add_new(self, data):
        tea = self.tea[int(data["var"])]()
        tea.set(data)
        self._list.append(tea)
        self.save_list()

    def edit(self, data):
        self._list[int(data["id"]) - 1].set(data)
        self.save_list()

    def behaviour(self, id):
        return self._list[int(id) - 1].behaviour()

    def delete(self, id):
        del self._list[int(id) - 1]
        self.save_list()

    def clear(self):
        self._list.clear()
        self.save_list()

    def save_list(self):
        with open(self._database, "wb") as f:
            pickle.dump(self._list, f)

    def laod_list(self):
        if path.exists(self._database):
            with open(self._database, "rb") as f:
                self._list = pickle.load(f)
