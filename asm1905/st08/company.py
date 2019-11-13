import pickle
import os
from flask import render_template
from flask import request


class EmployerBehaviour():
    def ShowForm(self, h):
        return render_template("formEmployer.tpl", **h.__dict__)

    def Show (self, h):
        return render_template("employer.tpl", **h.__dict__)

class ManagerBehaviour():
    def ShowForm(self, h):
        return render_template("formManager.tpl", **h.__dict__)

    def Show (self, h):
        return render_template("manager.tpl", **h.__dict__)

class Simple:

    def __init__(self):
        self.id = 0
        self.fullname = ''
        self.pay = ''
        self.age = ''

    def SetData(self):
        self.id = request.form.get('id')
        self.fullname = request.form.get('fullname')
        self.pay = request.form.get('pay')
        self.age = request.form.get('age')


class Employer(Simple):
    behaviour = EmployerBehaviour()
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

class Manager(Employer):
    behaviour = ManagerBehaviour()
    def __init__(self):
        Simple.__init__(self)
        self.employers_count = ''

    def SetData(self):
        Simple.SetData(self)
        self.employers_count = request.form.get('employers_count')
        self.email = request.form.get('email')

class Company():

    def __init__(self):
        try:
            self.load()
        except:
            self.humans = {}
            self.reuseId = 0

    def GetItem(self, id, f):
        if id <= 0:
            if f == 1:
                return Employer()
            if f == 2:
                return Manager()
        else:
            return self.humans[id]

    def load(self):
        with open('company.db', 'rb') as f:
            (self.reuseId, self.humans) = pickle.load(f)

    def store(self):
        with open('company.db', 'wb') as f:
            pickle.dump((self.reuseId, self.humans), f)

    def PrintHeader(self):
        return render_template("header.tpl")

    def PrintFooter(self):
        return render_template("footer.tpl")

    def ShowCompany(self):
        buf = ""
        for (key, item) in self.humans.items():
            buf += item.Show()
        buf += render_template("add.tpl")
        return buf

    def CompanyBehaviour(self, id, f):
        obj = self.GetItem(id, f)
        return obj.ShowForm()

    def AddManager(self):
        id = int(request.form.get('id', 0))
        item = self.GetItem(id,2)
        item.SetData()
        if id <=0:
            self.reuseId +=1
            item.id = self.reuseId
            self.humans[item.id] = item
        return self.ShowCompany()

    def AddEmployer(self):
        id = int(request.form.get('id', 0))
        item = self.GetItem(id,1)
        item.SetData()
        if id <=0:
            self.reuseId +=1
            item.id = self.reuseId
            self.humans[item.id] = item
        return self.ShowCompany()

    def DeleteItem(self, id):
        del(self.humans[id])
        return self.ShowCompany()
