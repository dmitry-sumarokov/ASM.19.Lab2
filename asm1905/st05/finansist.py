from person import Person
from fin_behavior import Fin_behavior
from flask import request
from flask import render_template

class Finansist(Person):

    def __init__(self):
        super().__init__()
        self.account = ''

    def SetData(self):
        Fin_behavior().SetData(self)
        #super().SetData()
        #self.account = request.form.get('account')
    
    def Show(self, tpl):
        return Fin_behavior().Show(self, tpl)
