# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:24:00 2019

@author: us211
"""

from flask import render_template
from flask import request
from student import Bachelor, Master, Graduate_student
import pickle    


class Students:

    IO_behaviour = None

    def __init__(self):
        try:
            self.load()
        except:
            self.items = {}
            self.maxid = 0

    def GetItem(self, id, f):
        if id <= 0:
            if f == 0:
                return Bachelor()
            if f == 1:
                return Master()
            if f == 2:
                return Graduate_student()
        else:
            return self.items[id]

    def AddItemBachelor(self):
        id = int(request.form.get('id', 0))
        item = self.GetItem(id,0)
        item.SetData()
        if id <=0:
            self.maxid +=1
            item.id = self.maxid
            self.items[item.id] = item
        return self.ShowStudents()

    def AddItemMaster(self):
        id = int(request.form.get('id', 0))
        item = self.GetItem(id,1)
        item.SetData()
        if id <=0:
            self.maxid +=1
            item.id = self.maxid
            self.items[item.id] = item
        return self.ShowStudents()

    def AddItemGraduate_student(self):
        id = int(request.form.get('id', 0))
        item = self.GetItem(id,2)
        item.SetData()
        if id <=0:
            self.maxid +=1
            item.id = self.maxid
            self.items[item.id] = item
        return self.ShowStudents()

    def PrintHeader(self):
        return render_template("header.tpl")

    def PrintFooter(self):
        return render_template("footer.tpl")



    def load(self):
        with open('group.db', 'rb') as f:
            (self.maxid, self.items) = pickle.load(f)

    def store(self):
        with open('group.db', 'wb') as f:
            pickle.dump((self.maxid, self.items), f)

    def ShowStudents(self):
        r = ""
        for (key, item) in self.items.items():
            r += item.Show()
        r += render_template("add.tpl")
        return r

    def DeleteItem(self, id):
        del(self.items[id])
        return self.ShowStudents()

    def StudentBehaviour(self, id, f):
        obj = self.GetItem(id, f)
        return obj.ShowForm()        