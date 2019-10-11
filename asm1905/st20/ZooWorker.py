from random import randint
from flask import render_template
from flask import request

class ZooWorker():
    Behaviour = None
    AbilityDisplay = None
    
    def __init__(self):
        self.Name = ''
        self.Surname = ''
        self.Age = ''
        self.Gender = ''
        self.Position = ''

    def SetBehaviour(self, Behaviour, AbilityDisplay):
        self.Behaviour = Behaviour
        self.AbilityDisplay = AbilityDisplay

    def Do(self):
        return(self.Behaviour.Do_something(self))

    def Read (self):
        self.AbilityDisplay.Read(self)

    def Write (self, key, tpl):
        return self.AbilityDisplay.Write(self, key, tpl)

class Behaviour_DirectorZoo():
        def Do_something(self, ZooWorker):
            Animals = ['слона', 'пантеру', 'крокодила', 'ламу', 'обезьянку', 'бегемота']
            newAnimals = Animals[randint(0, 5)]
            return('<br> Внимание посетителям! Нам есть что показать! Недавно мы привезли ' + newAnimals + '!!!' + '<br>')
            
class Behaviour_SecurityZoo():
        def Do_something(self, ZooWorker):
            return('<br> Купание запрещено - вольер с крокодилами!'+'<br>')
    
class Behaviour_KeeperZoo():
        def Do_something(self, ZooWorker):
            return('<br> SOOOOOOOOOOOOOOS! Бегемот сбежал! Кто-нибудь видел бегемота?'+'<br>')
    
class Behaviour_IceCreamSellerZoo():
        def Do_something(self, ZooWorker):
            IceCream_menu = ['ванильное', 'шоколадное', 'клубничное', 'фисташковое', 'малиновое', 'банановое']
            IceCream = IceCream_menu[randint(0, 5)]
            return('<br> Держите Ваше ' + IceCream + ' мороженое!'+'<br>')

class A_Display():
    def Read(self, ZooWorker):
        ZooWorker.Name = request.form.get('Name')
        ZooWorker.Surname = request.form.get('Surname')
        ZooWorker.Age = request.form.get('Age')
        ZooWorker.Gender = request.form.get('Gender')
        ZooWorker.Position = request.form.get('Position')
        
    def Write(self, ZooWorker, key, tpl):
        List=ZooWorker.__dict__
        List['id']=key
        return render_template(tpl, **List)
        

class DirectorZoo(ZooWorker):
    def __init__(self):
        self.SetBehaviour(Behaviour_DirectorZoo(), A_Display())
        
class SecurityZoo(ZooWorker):
    def __init__(self):
        self.SetBehaviour(Behaviour_SecurityZoo(),A_Display())
        
class KeeperZoo(ZooWorker):
    def __init__(self):
        self.SetBehaviour(Behaviour_KeeperZoo(),A_Display())
        
class IceCreamSellerZoo(ZooWorker):
    def __init__(self):
        self.SetBehaviour(Behaviour_IceCreamSellerZoo(),A_Display())

