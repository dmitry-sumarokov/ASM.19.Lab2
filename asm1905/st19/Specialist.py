from Worker import Worker
from random import randint
from flask import request


class Specialist(Worker):
    def do_init(self,request=None):
        if not request:
            self._deadline = int(input('Введите количество дней до дедлайна: '))
        else:
            if ("deadline" not in request.form or not request.form['deadline']):
                return("""Введите количество дней до дедлайна: <input type="number" required name="deadline">""")
            else:
                self._deadline = int(request.form['deadline'])

    def do_edit(self,request=None):
        if not request:
            new_deadline = input('Введите количество дней до дедлайна: ')
            self._deadline = int(new_deadline) if new_deadline else self._deadline    
        else:
            if ("deadline" not in request.form or not request.form['deadline']):
                return("""Введите количество дней до дедлайна: <input type="number" required name="deadline">""")
            else:
                self._deadline = int(request.form['deadline'])

    def do_magic(self,per):
        rand = randint(-42, 0)
        self._deadline = self._deadline + rand if self._deadline + rand > 0 else 0
        ret=''
        if rand == 0 and self._deadline > 0:
            ret += 'Корпоратив прошел удачно, сроки сдвинулись'+per
        elif self._deadline==0:
            ret += 'Срочно, срочно за бугор'+per
        else:
            ret += 'Отлично прокрастинируем, отмазку придумаем потом'+per
        ret += 'Дней до дедлайна: {0}'.format(self._deadline)
        return(ret)

    def do_print(self):
        return('Должность: Специалист'+per+' Дней до дедлайна: {0}'.format(self._deadline))


