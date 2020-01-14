import random
from abc import ABC, abstractmethod


class BaseEmployee(ABC):

    @abstractmethod
    def do_init(self, param_dict):
        self.name = param_dict['name']
        self.sex = param_dict['sex']
        self.age = param_dict['age']

    @abstractmethod
    def do_edit(self):
        pass

    @abstractmethod
    def do_magic(self):
        pass

    @abstractmethod
    def get_magic(self):
        pass


class Chief(BaseEmployee):
    
    def do_init(self, param_dict):
        super().do_init(param_dict)
        self.award = int(param_dict['special'])

    def do_edit(self):
        new_award = input('Введите коэффициент годовой премии: ')
        self.award = int(new_award) if new_award else self.award

    def do_magic(self):
        rand = random.randint(-10, 10)
        self.award += 10 * rand
        ret = ''
        if rand < 0:
            ret += 'Ваш подчиненный перепутал названия фирм поставщиков, вами заинтересовались органы\n'
        else:
            ret += 'Вы смогли наладить отношения с тегеранскими поставщиками\n'
        ret += f'Премия составляет {self.award}% от годового дохода'
        return ret

    def get_magic(self):
        return self.award


class Engeneer(BaseEmployee):

    def do_init(self, param_dict):
        super().do_init(param_dict)
        self.vac = int(param_dict['special'])

    def do_edit(self):
        _vac = input('Введите количетво выходных дней: ')
        self.vac = int(new_vac) if new_vac else self.vac

    def do_magic(self):
        rand = random.randint(-2, 5)
        self.vac += rand
        ret = ''
        if rand < 0:
            ret += 'Вы забыли сделать бэкап в пятницу, а Ниночке из бухгалтерии было просто необходимо зарядить свой айфон пока она строила глазки нашему новому стажеру\n'
        else:
            ret += 'Идея нанять в коллценр картавого Никиту Еремина помогла хоть как-то нормировать рабочий график\n'
        ret += f'Отпуск через 100500 лет, длительностью {self.vac} дней'
        return ret

    def get_magic(self):
        return self.vac


class Specialist(BaseEmployee):

    def do_init(self, param_dict):
        super().do_init(param_dict)
        self.deadline = int(param_dict['special'])

    def do_edit(self):
        new_deadline = input('Введите количество дней до дедлайна: ')
        self.deadline = int(new_deadline) if new_deadline else self.deadline

    def do_magic(self):
        rand = random.randint(-42, 0)
        self.deadline = self.deadline + rand if self.deadline + rand > 0 else 0
        ret = ''
        if rand == 0 and self.deadline > 0:
            ret += 'Корпоратив прошел удачно, сроки сдвинулись\n'
        elif self.deadline == 0:
            ret += 'Срочно, срочно за бугор\n'
        else:
            ret += 'Отлично прокрастинируем, отмазку придумаем потом\n'
        ret += f'Дней до дедлайна: {self.deadline}'
        return ret

    def get_magic(self):
        return self.deadline


class ChiefSpecialist(BaseEmployee):

    def do_init(self, param_dict):
        super().do_init(param_dict)
        self.share = int(param_dict['special'])

    def do_edit(self):
        new_share = input('Введите ставку отката: ')
        self.share = int(new_share) if new_share else self.share

    def do_magic(self):
        rand = random.randint(0, 210)
        self.share = rand
        ret = ''
        if rand == 0:
            ret += 'Вас поймал шеф, придется залечь на дно\n'
        else:
            ret += 'Удачная сделка с афганскими ребятами\n'
            self.share += 100
        ret += f'Откат составляет {self.share}% от месячного дохода'
        return ret

    def get_magic(self):
        return self.share
