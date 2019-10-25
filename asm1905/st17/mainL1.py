if __name__ == '__main__':
    from L1_plus.group import Group
else:
    from .L1_plus.group import Group

myG = Group()


def add_student():
    print()
    for i, item in enumerate(myG.group_menu):
        print(f'{i} - {item[0]}')
    print()
    type_student = int(input())
    myG.add_student(type_student)


def change_student():
    number_stud = int(input('Введите номер студента: '))
    myG.change_student(number_stud)
    print('Изменения сохранены')


def remove_student():
    number_stud = int(input('Введите номер студента: '))
    myG.remove_student(number_stud)


def do_magic():
    number_stud = int(input('Введите номер студента: '))
    myG.do_magic(number_stud)


def save_to_file():
    myG.save_to_file()
    print('Список сохранен')


def load_from_file():
    myG.load_from_file()
    print('Список загружен')


MENU = [
    ['Добавить студента', add_student],
    ['Редактировать информацию о студенте', change_student],
    ['Удалить из списка', remove_student],
    ['Вывести на экран весь список', myG.print_group],
    ['Выполнить особые действия', do_magic],
    ['Сохранить список в файл', save_to_file],
    ['Загрузить список из файла', load_from_file]
]


def menu():
    print()
    for i, item in enumerate(MENU):
        print(f'{i}) {item[0]}')
    print()
    return int(input('Введите номер пункта меню: '))


def main():
    try:
        while True:
            MENU[menu()][1]()
    except Exception as e:
        print(e, 'Game over', sep='\n')


if __name__ == '__main__':
    main()
