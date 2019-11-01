from person import Person
from des_behavior import Des_behavior
from flask import request
from flask import render_template

class Designer(Person):
    def __init__(self):
        super().__init__()
        self.orders = ''

    def SetData(self):
        return Des_behavior().SetData(self)
        #super().SetData()
        #self.orders = request.form.get('orders')"""

    def Show(self, tpl):
        return Des_behavior().Show(self, tpl)
