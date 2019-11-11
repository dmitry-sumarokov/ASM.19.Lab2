from Tancor2 import Tancor2
from flask import render_template,request
class Context2():
    ___dict__ = ('_first_name', '_stazh', '_age','_magic','_position')
    def __init__(self, tancor2: Tancor2):
            self._tancor2 = tancor2
            self._position = self._tancor2.do_print()
            self._first_name = ''
            self._stazh = ''
            self._age = 0
            self._magic = 0
    def do_magic_logic(self):
        return(self._tancor2.do_magic())
    def do_add_Tancor2(self):
        self._first_name = request.form.get('_first_name')
        self._second_name = request.form.get('_second_name')
        self._stazh = request.form.get('_stazh')
        self._age = int(request.form.get('_age'))
    def do_print(self,i, tpl):
        context = self.__dict__
        context['id']=i
        return render_template(tpl, **context)

