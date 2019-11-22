from flask import render_template
from flask import request

import pickle, datetime

class Library:
    def __init__(self):
        try:
            self.load()
        except:
            self.items = {}
            self.maxid = 0



    def GetItem(self, id, f):
        if id <= 0:
            if f == 0:
                return Book()
            if f == 1:
                return Journal()
            if f == 2:
                return Newspaper()
        else:
            return self.items[id]
        
    def load(self):
        with open('book.db', 'rb') as f:
            (self.maxid, self.items) = pickle.load(f)

    def store(self):
        with open('book.db', 'wb') as f:
            pickle.dump((self.maxid, self.items), f)
    
    def PrintHeader(self):
        return render_template("header.tpl")

    def PrintFooter(self):
        return render_template("footer.tpl")
    
    def ShowBook(self):
        r = ""
        for (key, item) in self.items.items():
            r += item.Show()
        r += render_template("add.tpl")
        return r
    
    def ShowForm(self, id):
        return self.GetItem(id).Show("form.tpl")
    
    def ShowFormJournal(self, id):
        return self.GetItem(id).Show("formjournal.tpl")
        
    def ShowFormNewspaper(self, id):
        return self.GetItem(id).Show("formnewspaper.tpl")
    
    def AddItem(self):
        id = int(request.form.get('id', 0))
        item = self.GetItem(id, 0)
        item.SetData()
        if id <=0:
            self.maxid +=1
            item.id = self.maxid
            self.items[item.id] = item
        return self.ShowBook()
        
    def AddItemNewspaper(self):
        id = int(request.form.get('id', 0))
        item = self.GetItem(id,2)
        item.SetData()
        if id <=0:
            self.maxid +=1
            item.id = self.maxid
            self.items[item.id] = item
        return self.ShowBook()
    
    def AddItemJournal(self):
        id = int(request.form.get('id', 0))
        item = self.GetItem(id,1)
        item.SetData()
        if id <=0:
            self.maxid +=1
            item.id = self.maxid
            self.items[item.id] = item
        return self.ShowBook()
    
    def DeleteItem(self, id):
        del(self.items[id])
        return self.ShowBook()
    
    def Behaviour(self, id, f):
        obj = self.GetItem(id, f)
        return obj.ShowForm() 
    
class BookBehaviour():
    def ShowForm(self, h):
        return render_template("form.tpl", **h.__dict__)    
    
    def Show (self, h):
        return render_template("item.tpl", **h.__dict__)    
    
class JournalBehaviour():
    def ShowForm(self, h):
        return render_template("formjournal.tpl", **h.__dict__)    

    def Show (self, h):
        return render_template("journal.tpl", **h.__dict__)    
    
class NewspaperBehaviour():
    def ShowForm(self, h):
        return render_template("formnewspaper.tpl", **h.__dict__)
    
    def Show (self, h):
        return render_template("newspaper.tpl", **h.__dict__)    
    
class Book:
    behaviour = BookBehaviour()
    def __init__(self):
        self.id = 0
        self.title = '0'
        self.body = ''
        self.author = ''
        self.time = datetime.datetime.now()

    def SetData(self):
        self.id = request.form.get('id')
        self.title = request.form.get('title')
        self.body = request.form.get('body')
        self.author = request.form.get('author')

    def ShowForm(self):
        return self.behaviour.ShowForm(self)
        
    def Show(self):
        return self.behaviour.Show(self)
    
    def execute(self):
        self.behaviour.execute(self.title)
        
class Journal(Book):
    behaviour = JournalBehaviour()
    def __init__(self):
        Book.__init__(self)
        self.year = ''
        
    def SetData(self):
        Book.SetData(self)
        self.year = request.form.get('year')
        
class Newspaper(Book):
    behaviour = NewspaperBehaviour()
    def __init__(self):
        Book.__init__(self)
        self.number = ''

    def SetData(self):
        Book.SetData(self)
        self.number = request.form.get('number')    