from person import Person
from flask import request
from flask import render_template

class Finansist(Person):

    def __init__(self):
        super().__init__()
        self.account = ''

    def SetData(self):
        super().SetData()
        self.account = request.form.get('account')

    def Show(self):
        return render_template("i_fin.tpl", **self.__dict__)

    

    

    

