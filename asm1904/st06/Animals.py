from flask import render_template
from flask import request

class Animals():
    Behaviour = None
    Display = None
    
    def __init__(self):
        self.Name = ''
        self.Klass = ''
        self.Age = ''
        self.MaxAge = ''
        self.Detki = ''

    def SetBehaviour(self, Behaviour, Display):
        self.Behaviour = Behaviour
        self.Display = Display

    def Feature(self):
        return self.Behaviour.Feature_animal(self)

    def Read (self):
        self.Display.Read(self)

    def Write (self, key, tpl):
        return self.Display.Write(self, key, tpl)
        
class Behaviour_Mammals():
        def Feature_animal(self, Animals):
            return('<br> Кормит детей молоком.'+'<br>')
            
class Behaviour_Fish():
        def Feature_animal(self, Animals):
            return('<br> Метает икру.'+'<br>')
    
class Behaviour_Bird():
        def Feature_animal(self, Animals):
            return('<br> Имеет клюв.'+'<br>')
    
class Behaviour_Reptile():
        def Feature_animal(self, Animals):
            return('<br> Хладнокровный, имеет низкую температуру тела.'+'<br>')

class Disp():
    def Read(self, Animals):
        Animals.Name = request.form.get('Name')
        Animals.Klass = request.form.get('Klass')
        Animals.Age = request.form.get('Age')
        Animals.MaxAge = request.form.get('MaxAge')
        Animals.Detki = request.form.get('Detki')
        
    def Write(self, Animals, key, tpl):
        List=Animals.__dict__
        List['id']=key
        return render_template(tpl,**List)


class Mammals(Animals):
    def __init__(self):
        self.SetBehaviour(Behaviour_Mammals(), Disp())
        
class Fish(Animals):
    def __init__(self):
        self.SetBehaviour(Behaviour_Fish(),Disp())
        
class Bird(Animals):
    def __init__(self):
        self.SetBehaviour(Behaviour_Bird(),Disp())
        
class Reptile(Animals):
    def __init__(self):
        self.SetBehaviour(Behaviour_Reptile(),Disp())
