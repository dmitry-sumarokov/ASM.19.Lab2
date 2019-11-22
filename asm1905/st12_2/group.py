import pickle
import os
import sys
from human import Student, Starosta, Proforg
from flask import render_template
from flask import request
import time

class group:
    def __init__(self):
        try:
            self.read_File()
        except:
            self.group = {}
            self.maxid = 0

    def getObject(self, id, type):
        if id == 0:
            if type == 0:
                return Student()
            if type == 1:
                return Starosta()
            if type == 2:
                return Proforg()
        else:
            return self.group[id]


    #def call_form(self, id, type):
        #return self.group[id].write("form_new.html", **self.__dict__)
       #return render_template("form_new.html", **self.__dict__)

    def call_form(self, id, type):
        return render_template("form_new.html", id=id, type=type)

    def add_human(self):
        id = int(request.form.get('id'))
        type = int(request.form.get('type'))
        item = self.getObject(id, type)
        item.read()
        if id == 0:
            self.maxid +=1
            item.id = self.maxid
            self.group[item.id] = item
        return self.show_list()

    def show_list(self):
        r = "<h3>Group list:</h3>"
        # for (key, item) in self.group:
        print(self.group)
        for (key, item) in self.group.items():
            # obj = self.group[item]
            # print(obj)
            r += item.write()
        r += render_template("add.html")
        return r

    def delete_card(self, id):
        del(self.group[id])
        return self.show_list()

    def action(self, id):
        return (self.group[id].action() + self.show_list())

    def write_File(self):
        with open('group.txt', 'wb') as f:
            pickle.dump((self.maxid, self.group), f)
        # with open(os.path.join(os.path.abspath(__name__).replace('\group', '\\'), 'group.txt'), 'wb') as f:
        #     pickle.dump(self.group, f)

    def read_File(self):
        with open('group.txt', 'rb') as f:
            (self.maxid, self.group) = pickle.load(f)
        # with open(os.path.join(os.path.abspath(__name__).replace('\group', '\\'), 'group.txt'), 'rb') as f:
        #     self.group = pickle.load(f)

    def change(self, id, type):
        item = self.getObject(id, type)
        return render_template("form_new.html", **item.__dict__)

    def Header(self):
        return render_template("header.html")

    def Footer(self):
        return render_template("footer.html")


"""   def newHuman(self, id):
       List=dict(firstname = '', lastname = '', age = '',  number_stud = '')
       List['id'] = id
       return render_template("form_new.html", **List)

   def add_newHuman(self):
       Menu = [self.addStudent, self.addStarosta, self.addProforg]
       id = int(request.form.get('id', 0))
       Menu[id]()
       return self.show_list()
          
          
          
          
    def update_form(self, id):
        return self.group[id].write(id, "form_update.html")

    def change(self):
        id = int(request.form.get('id', 0))
        self.group[id].read()
        return self.show_list()
"""