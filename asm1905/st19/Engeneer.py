from Worker import Worker
from random import randint
from flask import request


class Engeneer(Worker):
    def do_init(self,request=None):
        if not request:
            self._vac = int(input('Введите количетво выходных дней: '))
        else:
            if ("vac" not in request.form or not request.form['vac']):
                return("""Введите количетво выходных дней: <input type="number" required name="vac">""")
            else:
                self._vac = int(request.form['vac'])
        

    def do_edit(self,request=None):
        if not request:
            _vac = input('Введите количетво выходных дней: ')
            self._vac = int(new_vac) if new_vac else self._vac
        else:
            if ("vac" not in request.form or not request.form['vac']):
                return("""Введите количетво выходных дней: <input type="number" required name="vac">""")
            else:
                self._vac = int(request.form['vac'])
        

    def do_magic(self,per):
        rand = randint(-2, 5)
        self._vac += rand
        ret=''
        if rand < 0:
            ret += 'Вы забыли сделать бэкап в пятницу, а Ниночке из бухгалтерии было просто необходимо зарядить свой айфон, пока она строила глазки нашему новому стажеру'+per
        else:
            ret += 'Идея нанять в коллцентр картавого Никиту Еремина помогла хоть как-то нормировать рабочий график'+per
        ret += 'Отпуск через 100500 лет, длительностью {0} дней'.format(self._vac)
        return(ret)

    def do_print(self,per):
        return('Должность: Инженер'+per+' Отпуск через 100500 лет, длительностью {0} дней'.format(self._vac))


