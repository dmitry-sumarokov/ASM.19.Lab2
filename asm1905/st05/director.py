from person import Person
from flask import request
from flask import render_template

class Director(Person):

    def __init__(self):
        super().__init__()
        self.clients = ''

    def SetData(self):
        super().SetData()
        self.clients = request.form.get('clients')

    def Show(self):
        return render_template("i_dir.tpl", **self.__dict__)

    

    

    
