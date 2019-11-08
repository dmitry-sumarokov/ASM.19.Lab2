from flask import render_template
from flask import request
import pickle    

class Worker():
    
    IO_behaviour = None
    
    def __init__(self):
        self.id = 0
        self.surname = ''
        self.age = ''
        self.qualification = ''
        
    def SetData(self):
        self.id = request.form.get('id')
        self.surname = request.form.get('surname')
        self.age = request.form.get('age')
        self.qualification = request.form.get('qualification')
        
    def ShowForm(self):
        return self.IO_behaviour.ShowForm(self)
        
    def Show(self):
        return self.IO_behaviour.Show(self)

class IOWebDriller():
    def ShowForm(self, h):
        return render_template("formdriller.tpl", **h.__dict__)    
    
    def Show (self, h):
        return render_template("driller.tpl", **h.__dict__)    
    
class IOWebGeologist():
    def ShowForm(self, h):
        return render_template("formgeologist.tpl", **h.__dict__)    

    def Show (self, h):
        return render_template("geologist.tpl", **h.__dict__)    
    
class IOWebDeveloper():
    def ShowForm(self, h):
        return render_template("formdeveloper.tpl", **h.__dict__)
    
    def Show (self, h):
        return render_template("developer.tpl", **h.__dict__)
    
class Driller(Worker):
    IO_behaviour = IOWebDriller()
    
class Geologist(Worker):
    IO_behaviour = IOWebGeologist()

class Developer(Worker):  
    IO_behaviour = IOWebDeveloper()
        
class worker:
        
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
                return Driller()
            if f == 1:
                return Geologist()
            if f == 2:
                return Developer()
        else:
            return self.items[id]

    def AddItemDriller(self):
        id = int(request.form.get('id', 0))
        item = self.GetItem(id,0)
        item.SetData()
        if id <=0:
            self.maxid +=1
            item.id = self.maxid
            self.items[item.id] = item
        return self.ShowWorker()
    
    def AddItemGeologist(self):
        id = int(request.form.get('id', 0))
        item = self.GetItem(id,1)
        item.SetData()
        if id <=0:
            self.maxid +=1
            item.id = self.maxid
            self.items[item.id] = item
        return self.ShowWorker()
    
    def AddItemDeveloper(self):
        id = int(request.form.get('id', 0))
        item = self.GetItem(id,2)
        item.SetData()
        if id <=0:
            self.maxid +=1
            item.id = self.maxid
            self.items[item.id] = item
        return self.ShowWorker()
    
    def PrintHeader(self):
        return render_template("header.tpl")

    def PrintFooter(self):
        return render_template("footer.tpl")

    def DeleteItem(self, id):
        del(self.items[id])
        return self.ShowWorker()  

    def load(self):
        with open('workers.db', 'rb') as f:
            (self.maxid, self.items) = pickle.load(f)

    def store(self):
        with open('workers.db', 'wb') as f:
            pickle.dump((self.maxid, self.items), f)
    
    def ShowWorker(self):
        r = ""
        for (key, item) in self.items.items():
            r += item.Show()
        r += render_template("add.tpl")
        return r
    
    def WorkerBehaviour(self, id, f):
        obj = self.GetItem(id, f)
        return obj.ShowForm()        