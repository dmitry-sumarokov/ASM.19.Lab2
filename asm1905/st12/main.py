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
	return GetGroup().show_list()

@app.route("/forma/<int:id>/<int:type>")
def call_form(id, type):
	return GetGroup().call_form(id, type)

@app.route("/change/<int:id>/<int:type>")
def change(id, type):
	return GetGroup().change(id, type)

@app.route("/human", methods=['POST'])
def add_human():
	return GetGroup().add_human()

@app.route("/delete_card/<int:id>")
def delete_card(id):
	return GetGroup().delete_card(id)

@app.route("/action/<int:id>")
def action(id):
	return GetGroup().action(id)

@app.teardown_appcontext
def finish(ctx):
    GetGroup().write_File()

if __name__ == '__main__':
    app.run(debug=True)


""""
@app.route("/update/<int:id>")
def update_form(id):
	return GetGroup().Header() + GetGroup().update_form(id) + GetGroup().Footer()

@app.route("/Update", methods=['POST'])  
def change():
	return GetGroup().Header() + GetGroup().change() + GetGroup().Footer()

@app.route("/new_human/<int:id>")
def newHuman(id):
	return GetGroup().Header() + GetGroup().newHuman(id) + GetGroup().Footer()

@app.route("/New", methods=['POST'])  
def add_newHuman():
	return GetGroup().Header() + GetGroup().add_newHuman() + GetGroup().Footer()
"""