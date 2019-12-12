from flask import render_template
from flask import request


class Human():
    display = None
    behaviour = None

    def __init__(self):
        self.firstname = ' '
        self.lastname = ' '
        self.age = ' '
        self.number_stud = ' '
        self.type = ' '
        self.id = ' '

    def SetBehaviour(self, behavior, display):
        self.behaviour = behavior
        self.display = display

    def action(self):
        return self.behaviour.action(self)

    def read(self):
        self.display.read(self)

    def write(self):
        return self.display.write(self)


class BehaviourStudent():
    def action(self, human):
        return ('Меня зовут ' + human.firstname + ' ' + human.lastname + ', я студент.')


class BehaviourStarosta():
    def action(self, human):
        return ('Я староста этой группы, мне ' + human.age + '.')


class BehaviourProforg():
    def action(self, human):
        return ('Мой номер студенческого - ' + human.number_stud + '. В этой группе я профорг.')


class ConsoleWork():
    def read(self, human):
        human.id = request.form.get('id')
        human.firstname = request.form.get('firstname')
        human.lastname = request.form.get('lastname')
        human.age = request.form.get('age')
        human.number_stud = request.form.get('number_stud')
        human.type = request.form.get('type')


    # def write(self, human, key, fname):
    def write(self, h):
        return render_template("item.html", **h.__dict__)
        #List = human.__dict__
        #List['id'] = key
        # return render_template(fname, **human.__dict__)
        #return render_template(fname, **List)



class Student(Human):
    def __init__(self):
        self.SetBehaviour(BehaviourStudent(), ConsoleWork())

    # display = ConsoleWork()
    # behaviour = BehaviourStudent()


class Starosta(Human):
    def __init__(self):
        self.SetBehaviour(BehaviourStarosta(), ConsoleWork())
    # display = ConsoleWork()
    # behaviour = BehaviourStarosta()


class Proforg(Human):
    def __init__(self):
        self.SetBehaviour(BehaviourProforg(), ConsoleWork())
    # display = ConsoleWork()
    # behaviour = BehaviourProforg()