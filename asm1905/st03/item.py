from flask import request
from flask import render_template

class Item:
    
    def __init__(self):
        
        self.id = 0
        self.name = ''
        self.material = ''
        self.price = ''
        