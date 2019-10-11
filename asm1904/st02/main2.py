
from abc import ABC, abstractmethod
from flask import Flask, request
from group2 import Context
app = Flask(__name__)

if __name__ == '__main__':
    from group2 import Person_strategy, Person_flask
else:
    from .group2 import Person_strategy, Person_flask

current_class=None
from random import randint
from flask import request

Menu_list=None

def menu_flask():
    ret = []
    ret.append("_________________________________")
    for i, item in enumerate(Menu_list):
        ret.append("{0:2}. {1}".format(i, item[0]))
    ret.append("_________________________________")
    return('<br /> '.join(ret))


@app.route("/")
def main_flask():
    menu_p=menu_flask()
    return("""<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Лабораторная работа №2 Бернштейн</title>
</head>
<body>
"""+menu_p+"""
    <form action="/" method="POST">
        Выберите номер меню: <input type="number" name="num">
       <input type="submit" value="Добавить">
    </form>
</body>
</html>""")




@app.route("/", methods=['POST'])
def menu_item():
    menu_p=""
    if (not request.form['num']):
        return (main_flask()())
    else:
        menu_p = str(Menu_list[int(request.form['num'])][1](request))
    ret = """<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Лабораторная работа №2 Бернштейн</title>
</head>
<body>
"""+ menu_p 
    return(ret)


if __name__ == "__main__":
    current_class = Person_strategy(Person_flask)._group2()
    Menu_list = [
        ['Добавить участника труппы', current_class.add_person],
        ['Редактировать ', current_class.change_person],
        ['Вывести на экран ', current_class.print_group2],
        ['Удалить из списка', current_class.remove_person],
        ['Очистить список', current_class.clear_person],
        ['Выполнить особое действие', current_class.do_magic],
        ['Сохранить в файл', current_class.save_to_file],
        ['Загрузить из файла', current_class.load_from_file]

        ]
#    main()
    app.run(debug=True)
