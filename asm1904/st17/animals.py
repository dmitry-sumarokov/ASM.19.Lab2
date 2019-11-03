from flask import render_template
from flask import request



class Animal:
    animal_behavior = None
    display = None    

   # ___dict__ = ('name', 'age', 'gender')

    def __init__(self):
        self.name = ''
        self.age = ''
        self.gender = ''
        
    def SetBehaviour (self, animal_behavior, display):  
        self.animal_behavior = animal_behavior
        self.display = display
        
    def put(self):
        self.display.put(self)
        
    def output(self, key, tpl):
        return self.display.output(self, key, tpl)
        
    def different(self):
        return self.animal_behavior.different(self)

class CatBehavior():
    def different(self, Animal):
        return('<br> Хозяин, помурчим?'+'<br>')
        
class DogBehavior():
    def different(self, Animal):
        return('<br> Хозяин, пойдем гулять?'+'<br>')

class HamsterBehavior():
    def different(self, Animal):
        return ('<br> Хозяин, купишь мне вкусных семечек?'+'<br>')
        
class Display():

    def put(self, Animal):
        Animal.name = request.form.get('name')
        Animal.age = request.form.get('age')
        Animal.gender = request.form.get('gender')
        

    def output(self, Animal, i, tpl):
        List=Animal.__dict__
        List['id']=i
        return render_template(tpl, **List)

class Cat(Animal):
    def __init__(self):
        self.SetBehaviour(CatBehavior(), Display())

class Dog(Animal):
    def __init__(self):
        self.SetBehaviour(DogBehavior(), Display())

class Hamster(Animal):
    def __init__(self):
        self.SetBehaviour(HamsterBehavior(), Display())

    

