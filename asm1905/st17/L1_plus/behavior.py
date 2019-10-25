class BehaviorStud:
    def __init__(self):
        pass

    @staticmethod
    def stand_do_input(student_):
        student_.first_name = input('Введите имя: ')
        student_.second_name = input('Введите фамилию: ')
        student_.gender = input('Введите пол: ')
        student_.age = int(input('Введите возраст: '))

    @staticmethod
    def stand_do_print(student_):
        print(f'\nИмя: {student_.first_name}',
              f'Фамилия: {student_.second_name}',
              f'Пол: {student_.gender}',
              f'Возраст: {student_.age}', sep='\n')

    @staticmethod
    def stand_do_edit(student_):
        print('Если нужно оставить неизменным, нажмите Enter без ввода значения')
        new_first_name = input('Введите имя: ')
        student_.first_name = new_first_name if new_first_name else student_.first_name
        new_second_name = input('Введите фамилию: ')
        student_.second_name = new_second_name if new_second_name else student_.second_name
        new_gender = input('Введите пол: ')
        student_.gender = new_gender if new_gender else student_.gender
        new_age = input('Введите возраст: ')
        student_.age = int(new_age) if new_age else student_.age
