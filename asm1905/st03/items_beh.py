from behavior import Behavior
from flask import request
from flask import render_template

class Table_beh(Behavior):

    def __init__(self):
        return

    def SetData(self, itm):
        super().SetData(itm)
        itm.high = request.form.get('high')    
            
class Bed_beh(Behavior):

    def __init__(self):
        return

    def SetData(self, itm):
        super().SetData(itm)
        itm.width = request.form.get('width')    
        
class Wardrobe_beh(Behavior):

    def __init__(self):
        return

    def SetData(self, itm):
        super().SetData(itm)
        itm.doors = request.form.get('doors')    