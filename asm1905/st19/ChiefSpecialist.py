from Worker import Worker
from random import randint


class ChiefSpecialist(Worker):
    def do_print(self):
            return('Главный специалист')
    

    def do_magic(self,magic = None):
        rand = randint(0, 210)
        self._share = rand
        ret=''
        if rand == 0:
            ret += 'Вас поймал шеф, придется залечь на дно<br>'
        else:
            ret += 'Удачная сделка с афганскими ребятами<br>'
            self._share += 100
        ret += 'Откат составляет {0}% от месячного дохода'.format(self._share)
        return(ret)

   
