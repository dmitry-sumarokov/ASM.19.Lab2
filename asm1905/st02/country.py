import pickle
import os
from flask import render_template
from flask import request


class StoneBehaviour():
    def ShowForm(self, h):
        return render_template("formStone.tpl", **h.__dict__)

    def Show (self, h):
        return render_template("stone.tpl", **h.__dict__)

class WoodBehaviour():
    def ShowForm(self, h):
        return render_template("formWood.tpl", **h.__dict__)

    def Show (self, h):
        return render_template("wood.tpl", **h.__dict__)

class Simple:

    def __init__(self):
        self.id = 0
        self.fullname = ''
        self.square = 0

    def SetData(self):
        self.id = request.form.get('id')
        self.fullname = request.form.get('fullname')
        self.square = request.form.get('square')


class Stone(Simple):
    behaviour = StoneBehaviour()
    def __init__(self):
        Simple.__init__(self)
        self.email = ''

    def SetData(self):
        Simple.SetData(self)
        self.email = request.form.get('email')

    def ShowForm(self):
        return self.behaviour.ShowForm(self)

    def Show(self):
        return self.behaviour.Show(self)

    def execute(self):
        self.behaviour.execute(self.name)

class Wood(Stone):
    behaviour = WoodBehaviour()
    def __init__(self):
        Simple.__init__(self)

    def SetData(self):
        Simple.SetData(self)
        self.email = request.form.get('email')

class Country():

    def __init__(self):
        try:
            self.load()
        except:
            self.houses = {}
            self.reuseId = 0

    def GetItem(self, id, f):
        if id <= 0:
            if f == 1:
                return Stone()
            if f == 2:
                return Wood()
        else:
            return self.houses[id]

    def load(self):
        with open('country.db', 'rb') as f:
            (self.reuseId, self.houses) = pickle.load(f)

    def store(self):
        with open('country.db', 'wb') as f:
            pickle.dump((self.reuseId, self.houses), f)

    def PrintHeader(self):
        return render_template("header.tpl")

    def PrintFooter(self):
        return render_template("footer.tpl")

    def ShowCountry(self):
        buf = ""
        for (key, item) in self.houses.items():
            buf += item.Show()
        buf += render_template("add.tpl")
        return buf

    def CountryBehaviour(self, id, f):
        obj = self.GetItem(id, f)
        return obj.ShowForm()

    def AddWood(self):
        id = int(request.form.get('id', 0))
        item = self.GetItem(id,2)
        item.SetData()
        if id <=0:
            self.reuseId +=1
            item.id = self.reuseId
            self.houses[item.id] = item
        return self.ShowCountry()

    def AddStone(self):
        id = int(request.form.get('id', 0))
        item = self.GetItem(id,1)
        item.SetData()
        if id <=0:
            self.reuseId +=1
            item.id = self.reuseId
            self.houses[item.id] = item
        return self.ShowCountry()

    def DeleteItem(self, id):
        del(self.houses[id])
        return self.ShowCountry()
