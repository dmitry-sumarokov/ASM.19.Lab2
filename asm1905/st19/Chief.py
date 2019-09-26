from Worker import Worker
from random import randint
from flask import request


class Chief(Worker):
    def do_init(self,request = None):
        if  not request:
            self._award = int(input('Введите коэффициент годовой премии: '))
        else:
            if ("award" not in request.form or not request.form['award']):
                return("""Введите коэффициент годовой премии: <input type="number" required  name="award">""")
            else:
                self._award = int(request.form['award'])

    def do_edit(self,request = None):
        if  not request:
            new_award = input('Введите коэффициент годовой премии: ')
            self._award = int(new_award) if new_award else self._award
        else:
            if ("award" not in request.form or not request.form['award']):
                return("""Введите коэффициент годовой премии: <input type="number" name="award">""")
            else:
                self._award = int(request.form['award'])



    def do_magic(self,per):
        rand = randint(-10, 10)
        self._award += 10*rand
        ret=''
        if rand < 0:
            ret += 'Ваш подчиненный перепутал названия фирм поставщиков, вами заинтересовались органы'+per
        else:
            ret += 'Вы смогли наладить отношения с тегеранскими поставщиками'+per
        ret += 'Премия составляет {0}% от годового дохода'.format(self._award)
        return(ret)

    def do_print(self,per):
        return('Должность: Начальник'+per+' Премия составляет {0}% от годового дохода'.format(self._award))

