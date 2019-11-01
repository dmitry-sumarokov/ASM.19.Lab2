from flask import request
from flask import render_template
from behavior import Behavior

class Des_behavior(Behavior):
    def __init__(self):
        return 
        
    def SetData(self, obj):
        super().SetData(obj)
        obj.orders = request.form.get('orders')
