from Technic import Technic
from flask import render_template,request
class Context():
    ___dict__ = ('_mark', '_color', '_year','_it','_position')
    def __init__(self, technic: Technic):
            self._technic = technic
            self._position = self._technic.do_print()
            self._mark = ''
            self._color = ''
            self._year = 0
            self._it = 0
    def do_it_logic(self):
        return(self._technic.do_it())
    def do_add_Technic(self):
       # self._brend = request.form.get('_brend')
        self._mark = request.form.get('_mark')
        self._color = request.form.get('_color')
        self._year = int(request.form.get('_year'))
    def do_print(self,i, tpl):
        context = self.__dict__
        context['id']=i
        return render_template(tpl, **context)

