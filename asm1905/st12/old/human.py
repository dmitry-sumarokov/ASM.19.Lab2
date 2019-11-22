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


    def action(self):
        return self.behaviour.action(self)

    def read(self):
        self.display.read(self)

    def write(self, key, fname):
        return self.display.write(self, key, fname)


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
        human.firstname = request.form.get('firstname')
        human.lastname = request.form.get('lastname')
        human.age = request.form.get('age')
        human.number_stud = request.form.get('number_stud')


    def write(self, human, key, fname):
        List = human.__dict__
        List['id'] = key
        return render_template(fname, **List)


class Student(Human):
    display = ConsoleWork()
    behaviour = BehaviourStudent()


class Starosta(Human):
    display = ConsoleWork()
    behaviour = BehaviourStarosta()


class Proforg(Human):
    display = ConsoleWork()
    behaviour = BehaviourProforg()
