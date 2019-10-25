from random import randint

from .behavior import BehaviorStud


class BProforg:

    def __init__(self):
        pass

    @staticmethod
    def do_input(proforg_):
        BehaviorStud.stand_do_input(proforg_)
        proforg_.amount_contribution = float(input('Величина взноса: '))

    @staticmethod
    def do_print(proforg_, index):
        print('\nНомер студента: ' + str(index))
        print('\nПрофорг')
        BehaviorStud.stand_do_print(proforg_)
        print(f'Величина взноса: {proforg_.amount_contribution}')
        print('------------------------------')

    @staticmethod
    def do_edit(proforg_):
        BehaviorStud.stand_do_edit(proforg_)
        new_contribution = input('Величина взноса: ')
        proforg_.amount_contribution = float(new_contribution) if new_contribution else proforg_.amount_contribution

    @staticmethod
    def do_magic(proforg_):
        c_sum = proforg_.amount_contribution * randint(0, 10)
        print('\nСумма собранных взносов:', c_sum)
