from flask import render_template
from flask import request

class Student():
    IO_behavior = None

    def __init__(self):
        self.id = 0
        self.name = ''
        self.age = ''
        self.gender = ''

    def SetData(self):
        self.id = request.form.get('id')
        self.name = request.form.get('name')
        self.age = request.form.get('age')
        self.gender = request.form.get('gender')

    def ShowForm(self):
        return self.IO_behaviour.ShowForm(self)

    def Show(self):
        return self.IO_behaviour.Show(self)


class IOWebBachelor():
    def ShowForm(self, h):
        return render_template("formbachelor.tpl", **h.__dict__)

    def Show(self, h):
        return render_template("bachelor.tpl", **h.__dict__)


class IOWebMaster():
    def ShowForm(self, h):
        return render_template("formmaster.tpl", **h.__dict__)

    def Show(self, h):
        return render_template("master.tpl", **h.__dict__)


class IOWebGraduate_student():
    def ShowForm(self, h):
        return render_template("formgraduate_student.tpl", **h.__dict__)

    def Show(self, h):
        return render_template("graduate_student.tpl", **h.__dict__)


class Bachelor(Student):
    IO_behaviour = IOWebBachelor()


class Master(Student):
    IO_behaviour = IOWebMaster()


class Graduate_student(Student):
    IO_behaviour = IOWebGraduate_student()