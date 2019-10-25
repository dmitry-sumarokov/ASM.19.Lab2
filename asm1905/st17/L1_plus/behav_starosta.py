from .behavior import BehaviorStud


class BStarosta:
    def __init__(self):
        pass

    @staticmethod
    def do_input(starosta_):
        BehaviorStud.stand_do_input(starosta_)
        starosta_.scholarship = float(input('Надбавка к стипендии: '))

    @staticmethod
    def do_print(starosta_, index):
        print('\nНомер студента: ' + str(index))
        print('\nСтароста')
        BehaviorStud.stand_do_print(starosta_)
        print(f'Надбавка к стипендии: {starosta_.scholarship}')
        print('------------------------------')

    @staticmethod
    def do_edit(starosta_):
        BehaviorStud.stand_do_edit(starosta_)
        new_scholarship = input('Надбавка к стипендии: ')
        starosta_.scholarship = float(new_scholarship) if new_scholarship else starosta_.scholarship

    @staticmethod
    def do_magic(starosta_):
        print('\nОтметить студентов на паре')
        starosta_.scholarship += 5
