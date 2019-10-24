from .behavior import BehaviorStud


class BSimpStudent:
    def __init__(self):
        pass

    @staticmethod
    def do_input(simple_student):
        BehaviorStud.stand_do_input(simple_student)
        simple_student.performance = float(input('Успеваемость: '))

    @staticmethod
    def do_print(simple_student, index):
        print('\nНомер студента: ' + str(index))
        print('\nОбычный студент')
        BehaviorStud.stand_do_print(simple_student)
        print(f'Успеваемость: {simple_student.performance}')
        print('------------------------------')

    @staticmethod
    def do_edit(simple_student):
        BehaviorStud.stand_do_edit(simple_student)
        new_performance = input('Введите успеваемость: ')
        simple_student.performance = float(new_performance) if new_performance else simple_student.performance

    @staticmethod
    def do_magic(simple_student):
        print('\nПрогулял пару')
        simple_student.performance -= 0.1
