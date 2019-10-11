from Worker import Worker
from random import randint


class Specialist(Worker):
    def do_print(self):
            return('Специалист')

    def do_magic(self, magic = None):
        rand = randint(-42, 0)
        self._deadline = magic + rand if magic + rand > 0 else 0
        ret=''
        if rand == 0 and self._deadline > 0:
            ret += 'Корпоратив прошел удачно, сроки сдвинулись<br>'
        elif self._deadline==0:
            ret += 'Срочно, срочно за бугор<br>'
        else:
            ret += 'Отлично прокрастинируем, отмазку придумаем потом<br>'
        ret += 'Дней до дедлайна: {0}'.format(self._deadline)
        return(ret)

  
