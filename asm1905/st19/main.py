from flask import Flask, request
app = Flask(__name__)

if __name__ == '__main__':
    from group import Group_behav, Group_web, Group_console
else:
    from .group import Group_behav, Group_web, Group_console

cur_group=None

Menu_list=None

def menu_web():
    ret = []
    ret.append("------------------------------")
    for i, item in enumerate(Menu_list):
        ret.append("{0:2}. {1}".format(i, item[0]))
    ret.append("------------------------------")
    return('<br /> '.join(ret))

def menu():
    print("------------------------------")
    for i, item in enumerate(Menu_list):
        print("{0:2}. {1}".format(i, item[0]))
    print("------------------------------")
    return int(input())

def main():
    try:
        while True:
            Menu_list[menu()][1]()
    except Exception as e:
        print(e, "\nFinally")


@app.route("/")
def main_web():
    menu_p=menu_web()
    return("""<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Лабораторная работа №2 Шишкин</title>
</head>
<body>
"""+menu_p+"""
    <form action="/" method="POST">
        Выберите номер меню: <input type="number" name="num">
        <input type="submit">
    </form>
</body>
</html>""")




@app.route("/", methods=['POST'])
def main_num():
    menu_p=""
    if (not request.form['num']):
        return (main_web())
    else:
        menu_p = str(Menu_list[int(request.form['num'])][1](request))
    ret = """<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Лабораторная работа №2 Шишкин</title>
</head>
<body>
"""+ menu_p 
    return(ret)


if __name__ == "__main__":
    cur_group = Group_behav(Group_web)._group()
    Menu_list = [
        ['Добавить сотрудника', cur_group.add_worker],
        ['Редактировать информацию о сотруднике', cur_group.change_worker],
        ['Вывести на экран список сотрудников', cur_group.print_group],
        ['Удалить сотрудника из списка', cur_group.remove_worker],
        ['Очистить список', cur_group.clear_worker],
        ['Выполнить особое действие', cur_group.do_magic],
        ['Сохранить список в файл', cur_group.save_to_file],
        ['Загрузить список из файла', cur_group.load_from_file]

        ]
#    main()
    app.run(debug=True)
