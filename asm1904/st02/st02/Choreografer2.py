from Tancor2 import Tancor2
from random import randint
class Choreografer2(Tancor2):
    # def do_init(self,request = None):
        # if  not request:
            # self._spektakl = int(input('Введите название спектакля: '))
        # else:
            # if ("spektakl" not in request.form or not request.form['spektakl']):
                # return("""Введите название спектакля: <input type="text" required  name="spektakl">""")
            # else:
                # self._spektakl = str(request.form['spektakl'])

    # def do_edit(self,request = None):
        # if  not request:
            # new_spektakl = input('Введите название спектакля: ')
            # self._spektakl = int(new_spektakl) if new_spektakl else self._spektakl
        # else:
            # if ("spektakl" not in request.form or not request.form['spektakl']):
                # return("""Введите название спектакля: <input type="text" name="spektakl">""")
            # else:
                # self._spektakl = str(request.form['spektakl'])



    def do_magic(self):
    
        ret = 'Я хореограф'
        return(ret)

    def do_print(self):
        return(' ')