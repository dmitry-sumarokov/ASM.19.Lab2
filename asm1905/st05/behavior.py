from flask import request
from flask import render_template

class Behavior():
    def __init__(self):
        return 
    
    def SetData(self, obj):
        obj.id = request.form.get('id')
        obj.name = request.form.get('name')
        obj.surname = request.form.get('surname')
        obj.age = request.form.get('age')
        obj.wexp = request.form.get('wexp')

    def Show(self, obj, tpl):
        return render_template(tpl, **obj.__dict__)
