# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 20:51:12 2019

@author: alena
"""




from flask import render_template
from flask import request

import pickle, datetime
        
class AnalystBehaviour():
    def execute(self, name):
        print('Analyst '+ name)

class DeveloperBehaviour():
    def execute(self, name):
        print('Developer '+ name)
        
class TesterBehaviour():
    def execute(self, name):
        print('Tester '+ name)

class Man():
    
    def __init__(self):
        try:
            self.load()
        except:
            self.items = {}
            self.maxid = 0

    def GetItemAnalyst(self, id):
        if id <= 0:
            return AnalystItem()
        else:
            return self.items[id]

    def GetItemTester(self, id):
        if id <= 0:
            return Tester()
        else:
            return self.items[id]
        
    def GetItemDeveloper(self, id):
        if id <= 0:
            return Developer()
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
            if (type(item) is AnalystItem):
                r += item.Show("item.tpl")
            if (type(item) is Developer):
                r += item.Show("developer.tpl")
            if (type(item) is Tester):
                r += item.Show("tester.tpl")
        r += render_template("add.tpl")
        return r
    
    def ShowFormAnalyst(self, id):
        return self.GetItemAnalyst(id).Show("form.tpl")
    
    def ShowFormDeveloper(self, id):
        return self.GetItemDeveloper(id).Show("formdeveloper.tpl")
        
    def ShowFormTester(self, id):
        return self.GetItemTester(id).Show("formtester.tpl")
    
    def AddItemAnalyst(self):
        id = int(request.form.get('id', 0))
        item = self.GetItemAnalyst(id)
        item.SetData()
        if id <=0:
            self.maxid +=1
            item.id = self.maxid
            self.items[item.id] = item
        return self.ShowMan()
        
    def AddItemTester(self):
        id = int(request.form.get('id', 0))
        item = self.GetItemTester(id)
        item.SetData()
        if id <=0:
            self.maxid +=1
            item.id = self.maxid
            self.items[item.id] = item
        return self.ShowMan()
    
    def AddItemDeveloper(self):
        id = int(request.form.get('id', 0))
        item = self.GetItemDeveloper(id)
        item.SetData()
        if id <=0:
            self.maxid +=1
            item.id = self.maxid
            self.items[item.id] = item
        return self.ShowMan()
    
    def DeleteItem(self, id):
        del(self.items[id])
        return self.ShowMan()
    

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

    def Show(self, tpl):
        return render_template(tpl, **self.__dict__)
    
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
        


