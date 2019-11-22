from group import group
from flask import Flask
from flask import g

app = Flask(__name__)

def GetGroup():
        if 'Group' not in g:
                g.Group = group()
        return g.Group

@app.route("/")
def index():
	return GetGroup().Header() + GetGroup().show_list() + GetGroup().Footer()

"""@app.route("/update/<int:id>")
def update_form(id):
	return GetGroup().Header() + GetGroup().update_form(id) + GetGroup().Footer()

@app.route("/Update", methods=['POST'])  
def change():
	return GetGroup().Header() + GetGroup().change() + GetGroup().Footer()
"""

@app.route("/new_human/<int:id>/<int:cmd>")
def newHuman(id, cmd):
	return GetGroup().Header() + GetGroup().newHuman(id,cmd) + GetGroup().Footer()

@app.route("/New/<int:id>/<int:cmd>", methods=['POST'])
def add_newHuman(id, cmd):
	return GetGroup().Header() + GetGroup().add_newHuman(id, cmd) + GetGroup().Footer()

@app.route("/delete_card/<int:id>")
def delete_card(id):
	return GetGroup().delete_card(id) + GetGroup().Footer()

@app.route("/action/<int:id>")
def action(id):
	return GetGroup().Header() + GetGroup().action(id) + GetGroup().Footer()

@app.teardown_appcontext
def finish(ctx):
    GetGroup().write_File()

if __name__ == '__main__':
    app.run(debug=True)
    
    
"""Menu = [
    ["0 - Выход", None],
    ["1 - Добавить объект типа 'студент'", gr.addStudent],
    ["2 - Добавить объект типа 'староста'", gr.addStarosta],
    ["3 - Добавить объект типа 'профорг'", gr.addProforg],
    ["4 - Вывести список учеников", gr.show_list],
    ["5 - Изменить данные ученика", gr.change],
    ["6 - Удалить ученика из списка группы", gr.delete_card],
    ["7 - Сохранить список группы в файл", gr.write_file],
    ["8 - Считать список группы из файла", gr.read_file]
]
"""