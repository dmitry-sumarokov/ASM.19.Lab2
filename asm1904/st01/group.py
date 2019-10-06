# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:24:00 2019

@author: us211
"""

from flask import render_template
from flask import request
import pickle    

class Human():
     
    def __init__(self):
        self.id = 0
        self.name = ''
        self.age = ''
        self.email = ''
        
    def SetData(self):
        self.id = request.form.get('id')
        self.name = request.form.get('name')
        self.age = request.form.get('age')
        self.email = request.form.get('email')

class IOWebStudent():
    def ShowForm(self, id):
        return self.GetItem(id,0).Show("formstudent.tpl")
    
    def Show (self):
        return self.render_template("student.tpl", **self.__dict__)    
    
class IOWebStarosta():
    def ShowForm(self, id):
        return self.GetItem(id,1).Show("formstarosta.tpl")    

    def Show (self):
        return self.render_template("starosta.tpl", **self.__dict__)    
    
class IOWebProforg():
    def ShowForm(self, id):
        return self.GetItem(id,2).Show("formproforg.tpl")
    
    def Show (self):
        return self.render_template("proforg.tpl", **self.__dict__)
    
class Student(Human):
    IO_behaviour = IOWebStudent()
    
class Starosta(Human):
    IO_behaviour = IOWebStarosta()

class Proforg(Human):  
    IO_behaviour = IOWebProforg()
        
class group:
        
    IO_behaviour = None
    
    def __init__(self):
        try:
            self.load()
        except:
            self.items = {}
            self.maxid = 0
            
    def ShowForm(self, id):
        self.IO_behaviour.ShowForm(self)
        
    def Show(self):
        self.IO_behaviour.Show(self)

    def GetItem(self, id, f):
        if id <= 0:
            if f == 0:
                return Student()
            if f == 1:
                return Starosta()
            if f == 2:
                return Proforg()
        else:
            return self.items[id]

    def AddItemStudent(self):
        id = int(request.form.get('id', 0))
        item = self.GetItem(id,0)
        item.SetData()
        if id <=0:
            self.maxid +=1
            item.id = self.maxid
            self.items[item.id] = item
        return self.ShowGroup()
    
    def AddItemStarosta(self):
        id = int(request.form.get('id', 0))
        item = self.GetItem(id,1)
        item.SetData()
        if id <=0:
            self.maxid +=1
            item.id = self.maxid
            self.items[item.id] = item
        return self.ShowGroup()
    
    def AddItemProforg(self):
        id = int(request.form.get('id', 0))
        item = self.GetItem(id,2)
        item.SetData()
        if id <=0:
            self.maxid +=1
            item.id = self.maxid
            self.items[item.id] = item
        return self.ShowGroup()
    
    def PrintHeader(self):
        return render_template("header.tpl")

    def PrintFooter(self):
        return render_template("footer.tpl")

    def DeleteItem(self, id):
        del(self.items[id])
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
    
   # def ShowFromClass(self, id):
    #    a=""
     #   a = self.items[id].ShowForm(id)
      #  return a
        