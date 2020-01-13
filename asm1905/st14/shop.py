import pickle
from products import Table, Wardrobe, Bed
from flask import render_template
from flask import request

class Shop:

    def __init__(self):
        try:
            self.load()
        except:
            self.items = {}
            self.maxid = int(0)

    def PrintHeader(self):
        return render_template("header.tpl")

    def load(self):
        with open('items.db', 'rb') as f:
            (self.maxid, self.items) = pickle.load(f)

    def store(self):
        with open('items.db', 'wb') as f:
            pickle.dump((self.maxid, self.items), f)

    def ShowItems(self):
        r = ""
        n = ""
        for (key, i) in self.items.items():
            n = i.__class__.__name__
            r += i.Print(f"i_{n}.tpl")
        r += render_template("menu.tpl")
        return r

    def AddItem(self, type):
        if type==0:
            return Table().Print("table.tpl")
        elif type==1:
            return Bed().Print("bed.tpl")
        else: return Wardrobe().Print("wardrobe.tpl")

    def Add(self, type):
        id = int(request.form.get('id', 0))

        if id==0:
            if type==0:
                i = Table()
            elif type==1:
                i = Bed()
            else: i = Wardrobe()

            i.SetData()
            self.maxid += 1
            i.id = self.maxid
            self.items[i.id] = i
        else:
            i = self.items[id]
            i.SetData()
            self.items[id] = i
        return self.ShowItems()

    def Edit(self, id):
        return self.items[id].Print(f"{self.items[id].__class__.__name__}.tpl")

    def DeleteItem(self, id):
        del(self.items[id])
        if id >= 1:
            print(self.maxid)
            for i in range(id+1,self.maxid+1):
                self.items[i].id -= 1
                self.items[i-1] = self.items[i]
                del(self.items[i])
        self.maxid -= 1
        print(self.maxid)
        return self.ShowItems()

    def DeleteAll(self):
        self.items.clear()
        self.maxid = 0
        return self.ShowItems()