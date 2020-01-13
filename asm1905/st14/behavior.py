from flask import request
from flask import render_template

class Behavior:
    
    def __init__(self):
        return
    
    def SetData(self, itm):
        itm.id = request.form.get('id')
        itm.name = request.form.get('name')
        itm.material = request.form.get('material')
        itm.price = request.form.get('price')
        
        
    def Print(self, itm, temp):
      return render_template(temp, **itm.__dict__)