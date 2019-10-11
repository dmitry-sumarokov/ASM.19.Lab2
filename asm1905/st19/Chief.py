from Worker import Worker
from random import randint

class Chief(Worker):
    def do_print(self):
            return('Начальник')


    def do_magic(self, magic = None):
        self._award = magic
        rand = randint(-10, 10)
        self._award += 10*rand
        ret=''
        if rand < 0:
            ret += 'Ваш подчиненный перепутал названия фирм поставщиков, вами заинтересовались органы<br>'
        else:
            ret += 'Вы смогли наладить отношения с тегеранскими поставщиками<br>'
        ret += 'Премия составляет {0}% от годового дохода'.format(self._award)
        return(ret)


