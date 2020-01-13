from item import Item
from items_beh import Table_beh, Bed_beh, Wardrobe_beh
from flask import request
from flask import render_template

class Table(Item):

    def __init__(self):
        super().__init__()
        self.high = ''

    def SetData(self):
        return Table_beh().SetData(self)

    def Print(self, temp):
        return Table_beh().Print(self, temp)

class Wardrobe(Item):

    def __init__(self):
        super().__init__()
        self.doors = ''

    def SetData(self):
        return Wardrobe_beh().SetData(self)

    def Print(self, temp):
        return Wardrobe_beh().Print(self, temp)

class Bed(Item):

    def __init__(self):
        super().__init__()
        self.width = ''

    def SetData(self):
        return Bed_beh().SetData(self)

    def Print(self, temp):
        return Bed_beh().Print(self, temp)        