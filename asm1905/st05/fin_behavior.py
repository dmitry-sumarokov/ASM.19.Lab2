from flask import request
from flask import render_template
from behavior import Behavior

class Fin_behavior(Behavior):
    def __init__(self):
        return
        
    def SetData(self, obj):
        super().SetData(obj)
        obj.account = request.form.get('account')
