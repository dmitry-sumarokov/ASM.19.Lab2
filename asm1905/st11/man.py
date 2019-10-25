# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 20:51:12 2019

@author: alena
"""

from flask import render_template
from flask import request

import pickle, datetime

class Man():
    
    def __init__(self):
        try:
            self.load()
        except:
            self.items = {}
            self.maxid = 0

    def GetItem(self, id, f):
        if id <= 0:
            if f == 0:
                return AnalystItem()
            if f == 1:
                return Developer()
            if f == 2:
                return Tester()
        else:
            return self.items[id]
        
    def load(self):
        with open('team.db', 'rb') as f:
            (self.maxid, self.items) = pickle.load(f)

    def store(self):
        with open('team.db', 'wb') as f:
            pickle.dump((self.maxid, self.items), f)
    
    def PrintHeader(self):
        return render_template("header.tpl")

    def PrintFooter(self):
        return render_template("footer.tpl")
    
    def ShowMan(self):
        r = ""
        for (key, item) in self.items.items():
            r += item.Show()
        r += render_template("add.tpl")
        return r
    
    def ManBehaviour(self, id, f):
        obj = self.GetItem(id, f)
        return obj.ShowForm()  

    def AddItemAnalyst(self):
        id = int(request.form.get('id', 0))
        item = self.GetItem(id,0)
        item.SetData()
        if id <=0:
            self.maxid +=1
            item.id = self.maxid
            self.items[item.id] = item
        return self.ShowMan()
        
    def AddItemTester(self):
        id = int(request.form.get('id', 0))
        item = self.GetItem(id,2)
        item.SetData()
        if id <=0:
            self.maxid +=1
            item.id = self.maxid
            self.items[item.id] = item
        return self.ShowMan()
    
    def AddItemDeveloper(self):
        id = int(request.form.get('id', 0))
        item = self.GetItem(id,1)
        item.SetData()
        if id <=0:
            self.maxid +=1
            item.id = self.maxid
            self.items[item.id] = item
        return self.ShowMan()
    
    def DeleteItem(self, id):
        del(self.items[id])
        return self.ShowMan()

        
class AnalystBehaviour():
    def ShowForm(self, h):
        return render_template("form.tpl", **h.__dict__)    
    
    def Show (self, h):
        return render_template("item.tpl", **h.__dict__)    
    
class DeveloperBehaviour():
    def ShowForm(self, h):
        return render_template("formdeveloper.tpl", **h.__dict__)    

    def Show (self, h):
        return render_template("developer.tpl", **h.__dict__)    
    
class TesterBehaviour():
    def ShowForm(self, h):
        return render_template("formtester.tpl", **h.__dict__)
    
    def Show (self, h):
        return render_template("tester.tpl", **h.__dict__)
    
class AnalystItem:
    behaviour = AnalystBehaviour()
    def __init__(self):
        self.id = 0
        self.name = ''
        self.surname = ''
        self.category = ''
        self.time = datetime.datetime.now()

    def SetData(self):
        self.id = request.form.get('id')
        self.name = request.form.get('name')
        self.surname = request.form.get('surname')
        self.category = request.form.get('category')
        
    def ShowForm(self):
        return self.behaviour.ShowForm(self)
        
    def Show(self):
        return self.behaviour.Show(self)
    
    def execute(self):
        self.behaviour.execute(self.name)
        
class Developer(AnalystItem):
    behaviour = DeveloperBehaviour()
    def __init__(self):
        AnalystItem.__init__(self)
        self.programming_language = ''
        
    def SetData(self):
        AnalystItem.SetData(self)
        self.programming_language = request.form.get('programming_language')
        
class Tester(AnalystItem):
    behaviour = TesterBehaviour()
    def __init__(self):
        AnalystItem.__init__(self)
        self.view = ''

    def SetData(self):
        AnalystItem.SetData(self)
        self.view = request.form.get('view')    
        


