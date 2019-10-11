from Worker import Worker
from random import randint


class Engeneer(Worker):
    def do_print(self):
            return('Инженер')

    def do_magic(self, magic = None):
        self._vac = magic
        rand = randint(-2, 5)
        self._vac += rand
        ret=''
        if rand < 0:
            ret += 'Вы забыли сделать бэкап в пятницу, а Ниночке из бухгалтерии было просто необходимо зарядить свой айфон пока она строила глазки нашему новому стажеру<br>'
        else:
            ret += 'Идея нанять в коллценр картавого Никиту Еремина помогла хоть как-то нормировать рабочий график<br>'
        ret += 'Отпуск через 100500 лет, длительностью {0} дней'.format(self._vac)
        return(ret)




