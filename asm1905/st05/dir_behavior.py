from flask import request
from flask import render_template
from behavior import Behavior

class Dir_behavior(Behavior):
    def __init__(self):
        return
        
    def SetData(self, obj):
        super().SetData(obj)
        obj.clients = request.form.get('clients')
