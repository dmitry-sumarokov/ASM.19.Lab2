from person import Person
from flask import request
from flask import render_template

class Designer(Person):

    def __init__(self):
        super().__init__()
        self.orders = ''

    def SetData(self):
        super().SetData()
        self.orders = request.form.get('orders')

    def Show(self):
        return render_template("i_des.tpl", **self.__dict__)

    

    

    

