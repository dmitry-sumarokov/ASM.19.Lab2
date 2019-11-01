from flask import render_template
from flask import request
from director import Director
from finansist import Finansist
from designer import Designer
from person import Person
import pickle

class Company:
    def __init__(self):
        try:
            self.load()
        except:
            self.staff = {}
            self.maxid = int(0)

    def PrintHeader(self):
        return render_template("header.tpl")

    def load(self):
        with open('staff.db', 'rb') as f:
            (self.maxid, self.staff) = pickle.load(f)

    def store(self):
        with open('staff.db', 'wb') as f:
            pickle.dump((self.maxid, self.staff), f)

    def ShowStaff(self):
        r = ""
        n = ""
        for (key, i) in self.staff.items():
            n = i.__class__.__name__
            r += i.Show(f"i_{n}.tpl")
        r += render_template("menu.tpl")
        return r

    def AddStaff(self, type):
        if type==0:
            return Director().Show("director.tpl")
        elif type==1:
            return Finansist().Show("finansist.tpl")
        else: return Designer().Show("designer.tpl")

    def Add(self, type):
        id = int(request.form.get('id', 0))

        if id==0:
            if type==0:
                i = Director()
            elif type==1:
                i = Finansist()
            else: i = Designer()

            i.SetData()
            self.maxid += 1
            i.id = self.maxid
            self.staff[i.id] = i
        else:
            i = self.staff[id]
            i.SetData()
            self.staff[id] = i
        return self.ShowStaff()

    def Edit(self, id):
        return self.staff[id].Show(f"{self.staff[id].__class__.__name__}.tpl")

    def DeleteItem(self, id):
        del(self.staff[id])
        if id >= 1:
            print(self.maxid)
            for i in range(id+1,self.maxid+1):
                self.staff[i].id -= 1
                self.staff[i-1] = self.staff[i]
                del(self.staff[i])
        self.maxid -= 1
        print(self.maxid)
        return self.ShowStaff()

    def DeleteStaff(self):
        self.staff.clear()
        self.maxid = 0
        return self.ShowStaff()
    
