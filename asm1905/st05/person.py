from flask import request
from flask import render_template

class Person:
    def __init__(self):
        self.id = 0
        self.name = ''
        self.surname = ''
        self.age = ''
        self.wexp = ''
        
    """def SetData(self):
        self.id = request.form.get('id')
        self.name = request.form.get('name')
        self.surname = request.form.get('surname')
        self.age = request.form.get('age')
        self.wexp = request.form.get('wexp')

    def Show(self, tpl):
        return render_template(tpl, **self.__dict__)
"""
