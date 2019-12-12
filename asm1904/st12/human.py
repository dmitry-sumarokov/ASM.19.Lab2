from flask import request, render_template

class Human():
    human_behaviour = None

    def __init__(self):
        self.id = 0
        self.Fname = ''
        self.Sname = ''
        self.Email = ''

    def SetData(self):
        self.id = request.form.get('id')
        self.Fname = request.form.get('Fname')
        self.Sname = request.form.get('Sname')
        self.Email = request.form.get('Email')

    def ShowForm(self):
        return self.IO_behaviour.ShowForm(self)

    def Show(self):
        return self.IO_behaviour.Show(self)


class IOWebEngineer():
    def ShowForm(self, h):
        return render_template("formEng.tpl", **h.__dict__)

    def Show(self, h):
        return render_template("Engineer.tpl", **h.__dict__)


class IOWebSpecialist():
    def ShowForm(self, h):
        return render_template("formSpec.tpl", **h.__dict__)

    def Show(self, h):
        return render_template("Specialist.tpl", **h.__dict__)


class IOWebDepartment():
    def ShowForm(self, h):
        return render_template("formDep.tpl", **h.__dict__)

    def Show(self, h):
        return render_template("Department.tpl", **h.__dict__)


class Engineer(Human):
    IO_behaviour = IOWebEngineer()


class Specialist(Human):
    IO_behaviour = IOWebSpecialist()


class Department(Human):
    IO_behaviour = IOWebDepartment()