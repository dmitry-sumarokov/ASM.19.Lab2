from abc import ABC, abstractmethod
from flask import Flask
from flask import g
from flask import render_template
from flask import request
import pickle


class StudentAbs(ABC):

    behavior = None

    def __init__(self):
        self.kind = 0
        self.age = ''
        self.student_kind = ''
        self.salary = 0
        self.FIO = ''
        self.absent = ''
        pass

    def do_fill_data(self):
        self.kind = request.form.get('kind')
        self.age = request.form.get('age')
        self.student_kind =  request.form.get('student_kind ')
        self.salary = request.form.get('salary')
        self.FIO = request.form.get('FIO')
        self.absent = request.form.get('absent')

    def form_template(self):
        return render_template("form.tpl", **self.__dict__)

    def Show(self):
        return render_template("student.tpl", **self.__dict__)

    @abstractmethod
    def do_special(self):
        pass

# Поведение Общее
class Student_behavior(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def do_magic(self):
        pass

class Starosta_behavior(Student_behavior):
    def __init__(self):
        super(Starosta_behavior, self).__init__()
        self.student_kind = 'я староста'

    def do_magic(self):
        r = render_template('header.tpl', special=self.student_kind)
        return r

class Student_behavior(Student_behavior):
    def __init__(self):
        super(Student_behavior, self).__init__()
        self.student_kind = 'я обычный студент'

    def do_magic(self):
        r = render_template('header.tpl', special=self.student_kind)
        return r

class Proforg_behavior(Student_behavior):
    def __init__(self):
        super(Proforg_behavior, self).__init__()
        self.student_kind = 'я профорг'

    def do_magic(self):
        r = render_template('header.tpl', special=self.student_kind)
        return r

# Человеееееечки
class Starosta(StudentAbs):
    def __init__(self):
        super(StudentAbs, self).__init__()
        self.behavior = Starosta_behavior()
        pass

    def do_special(self):
        header = self.behavior.do_magic()
        return header

class Student(StudentAbs):
    def __init__(self):
        super(StudentAbs, self).__init__()
        self.behavior = Student_behavior()
        pass

    def do_special(self):
        header = self.behavior.do_magic()
        return header

class Proforg(StudentAbs):
    def __init__(self):
        super(StudentAbs, self).__init__()
        self.behavior = Proforg_behavior()
        pass

    def do_special(self):
        header = self.behavior.do_magic()
        return header


class Group():
    def __init__(self):
        try:
            self.load()
        except:
            self.items = {}
            self.maxid = 0
        pass

    def getKindStudentObject(self, id, kind):
        if id == 0:
            if kind == 0:
                return Student()
            if kind == 1:
                return Starosta()
            if kind == 2:
                return Proforg()
        else:
            return self.items[id]

    def ShowGroup(self, templateName = ''):
        r = ""
        for (key, item) in self.items.items():
            r += item.Show()
        r += render_template("add.tpl") + render_template("footer.tpl")
        return r

    def AddStudent(self):
        id = int(request.form.get('id', 0))
        kind = int(request.form.get('kind', 0))
        item = self.getKindStudentObject(id, kind)
        item.do_fill_data()
        if id == 0:
            self.maxid +=1
            item.id = self.maxid
            self.items[item.id] = item
        return self.ShowGroup()

    def DeleteStudent(self, id):
        del(self.items[id])
        return self.ShowGroup()

    def DoSpecialAction(self, id):
        r = self.items[id].do_special()
        return r + self.ShowGroup()

    def load(self):
        with open('file', 'rb') as f:
            (self.maxid, self.items) = pickle.load(f)

    def store(self):
        with open('file', 'wb') as f:
            pickle.dump((self.maxid, self.items), f)

    def printHeader(self):
        return render_template("header.tpl")

    def PrintFooter(self):
        return render_template("footer.tpl")

    def ShowForm(self, id, kind):
        return render_template("form_New.tpl", id=id, kind=kind)

    def EditStudent(self, id, kind):
        item = self.getKindStudentObject(id, kind)
        return render_template("form_New.tpl", **item.__dict__)

