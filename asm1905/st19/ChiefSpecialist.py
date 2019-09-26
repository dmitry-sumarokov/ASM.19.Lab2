from Worker import Worker
from random import randint
from flask import request


class ChiefSpecialist(Worker):
    def do_init(self,request=None):
        if not request:
            self._share = int(input('Введите ставку отката: '))
        else:
            if ("share" not in request.form or not request.form['share']):
                return("""Введите ставку отката: <input type="number" required name="share">""")
            else:
                self._share = int(request.form['share'])


    def do_edit(self,request=None):
        if not request:
            new_share = input('Введите ставку отката: ')
            self._share = int(new_share) if new_share else self._share
        else:
            if ("share" not in request.form or not request.form['share']):
                return("""Введите ставку отката: <input type="number" required name="share">""")
            else:
                self._share = int(request.form['share'])

    def do_magic(self,per):
        rand = randint(0, 210)
        self._share = rand
        ret=''
        if rand == 0:
            ret += 'Вас поймал шеф, придется залечь на дно'+per
        else:
            ret += 'Удачная сделка с афганскими ребятами'+per
            self._share += 100
        ret += 'Откат составляет {0}% от месячного дохода'.format(self._share)
        return(ret)

    def do_print(self,per):
        return('Должность: Главный специалист'+per+' Откат составляет {0}% от месячного дохода'.format(self._share))


