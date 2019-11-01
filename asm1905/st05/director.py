from person import Person
from dir_behavior import Dir_behavior
from flask import request
from flask import render_template

class Director(Person):

    def __init__(self):
        super().__init__()
        self.clients = ''

    def SetData(self):
        Dir_behavior().SetData(self)
        #super().SetData()
        #self.clients = request.form.get('clients')
    
    def Show(self, tpl):
        return Dir_behavior().Show(self, tpl)
        
