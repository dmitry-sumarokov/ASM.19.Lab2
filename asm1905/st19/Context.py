from Worker import Worker
from flask import render_template,request

class Context():
    ___dict__ = ('_first_name', '_second_name', '_gender', '_age','_magic','_position')
    def __init__(self, worker: Worker):
        self._worker = worker
        self._position = self._worker.do_print()
        self._first_name = ''
        self._second_name = ''
        self._gender = ''
        self._age = 0
        self._magic = 0

    def do_magic_logic(self):
        return(self._worker.do_magic(self._magic))


    def do_add_worker(self):
        self._first_name = request.form.get('_first_name')
        self._second_name = request.form.get('_second_name')
        self._gender = request.form.get('_gender')
        self._age = int(request.form.get('_age'))
        self._magic = int(request.form.get('_magic'))

    def do_print(self,i, tpl):
        context = self.__dict__
        context['id']=i
        return render_template(tpl, **context)

    
      
