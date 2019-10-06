if __name__ == '__main__':
    from group import group
else:
    from .group import group

#from .Human import group

group=group()

def main():
    menu = {"1":("Добавить студента", group.insertStudent),
        "2":("Добавить старосту", group.insertStarosta),
        "3":("Добавить профорга", group.insertProforg),        
        "4":("Специальное действие", group.execute),
        "5":("Редактировать", group.edit),
        "6":("Удалить", group.delete),
        "7":("Показать", group.show),
        "8":("Считать из файла", group.readfile),
        "9":("Записать в файл", group.writefile),
        "10":("Очистить", group.clean),
        "11":("Выход", None)}
    while True:
        print('')
        print('Меню:')
        for k in range(1,12):
            print(k, " : ", menu[str(k)][0])
        x = input()
        if int(x)==11:
            break
        if int(x) >= 1 and int(x) < 12:
            menu[x][1]()
        else:
            print('Некорректный ввод')
        


if __name__ == '__main__':
	main()


