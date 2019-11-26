import behaviour


class Tea:

    def set_behaviour(self, beh):
        self._behaviour = beh()

    def behaviour(self):
        return self._behaviour.action()

    def set(self, data):
        self.type = data["type"]
        self.form = data["form"]


class ChineseTea(Tea):
    var = "chinese"

    def __init__(self):
        self.set_behaviour(behaviour.Chinese_Tea_Behaviour)


class IndianTea(Tea):
    var = "indian"

    def __init__(self):
        self.set_behaviour(behaviour.Indian_Tea_Behaviour)
