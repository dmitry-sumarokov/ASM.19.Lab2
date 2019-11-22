import pickle
import os
from human import Student, Starosta, Proforg
from flask import render_template
from flask import request

class group:
    def __init__(self):
        try:
            self.read_File()
        except:
            self.group = {}
            self.maxid = 0

    def GetItem(self, id, cmd):
        if id <= 0:
            if cmd == 0:
                return Student()
            if cmd == 1:
                return Starosta()
            if cmd == 2:
                return Proforg()
        else:
            return self.group[id]

    def newHuman(self, id, cmd):
        List = dict(firstname = '', lastname = '', age = '',  number_stud = '')
        #List['id'] = id
        #List['cmd'] = cmd
        return render_template("form_new.html", **List)

    def add_newHuman(self, id, cmd):
        #Menu = [self.addStudent, self.addStarosta, self.addProforg]
        id = int(request.form.get('id', 0))
        cmd = int(request.form.get('cmd', 0))
        item = self.GetItem(id,cmd)
        item.write()
        if id <= 0:
            self.maxid += 1
            item.id = self.maxid
            self.items[item.id] = item
        return self.show_list()

    def addStudent(self):
        newStudent = Student()
        newStudent.read()
        self.group.append(newStudent)

    def addStarosta(self):
        newStarosta = Starosta()
        newStarosta.read()
        self.group.append(newStarosta)

    def addProforg(self):
        newProforg = Proforg()
        newProforg.read()
        self.group.append(newProforg)

    def show_list(self):
        r = "<h3>Список группы:</h3>"
        for (key, item) in enumerate(self.group):
            r += item.write(key, "item.html")
        r += render_template("add.html")
        return r

    def delete_card(self, id):
        self.group.pop(int(id))
        return self.show_list()

    def action(self, id):
        return (self.group[id].action() + self.show_list())

    def write_File(self):
        with open(os.path.join(os.path.abspath(__name__).replace('\group', '\\'), 'group.txt'), 'wb') as f:
            pickle.dump(self.group, f)

    def read_File(self):
        with open(os.path.join(os.path.abspath(__name__).replace('\group', '\\'), 'group.txt'), 'rb') as f:
            self.group = pickle.load(f)

    def Header(self):
        return render_template("header.html")

    def Footer(self):
        return render_template("footer.html")

    """  
        def update_form(self, id):
             return self.group[id].write(id, "form_update.html")
    
    def change(self):
         id = int(request.form.get('id', 0))
         self.group[id].read()
         return self.show_list()
"""