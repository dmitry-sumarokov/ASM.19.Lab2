import pickle

from flask import request, render_template
from human import Engineer, Specialist, Department

        
class group:

    IO_behavior = None

    def __init__(self):
        try:
            self.load()
        except:
            self.items = {}
            self.maxid = 0

    def GetItem(self, id, f):
        if id <= 0:
            if f == 0:
                return Engineer()
            if f == 1:
                return Specialist()
            if f == 2:
                return Department()
        else:
            return self.items[id]

    def AddItemEngineer(self):
        id = int(request.form.get('id', 0))
        item = self.GetItem(id, 0)
        item.SetData()
        if id <= 0:
            self.maxid += 1
            item.id = self.maxid
            self.items[item.id] = item
        return self.ShowGroup()

    def AddItemSpecialist(self):
        id = int(request.form.get('id', 0))
        item = self.GetItem(id, 1)
        item.SetData()
        if id <= 0:
            self.maxid += 1
            item.id = self.maxid
            self.items[item.id] = item
        return self.ShowGroup()

    def AddItemDepartment(self):
        id = int(request.form.get('id', 0))
        item = self.GetItem(id, 2)
        item.SetData()
        if id <= 0:
            self.maxid += 1
            item.id = self.maxid
            self.items[item.id] = item
        return self.ShowGroup()

    def PrintHeader(self):
        return render_template("header.tpl")

    def PrintFooter(self):
        return render_template("footer.tpl")

    def DeleteItem(self, id):
        del (self.items[id])
        return self.ShowGroup()

    def load(self):
        with open('group.db', 'rb') as f:
            (self.maxid, self.items) = pickle.load(f)

    def store(self):
        with open('group.db', 'wb') as f:
            pickle.dump((self.maxid, self.items), f)

    def ShowGroup(self):
        r = ""
        for (key, item) in self.items.items():
            r += item.Show()
        r += render_template("add.tpl")
        return r

    def HumanBehaviour(self, id, f):
        obj = self.GetItem(id, f)
        return obj.ShowForm()
