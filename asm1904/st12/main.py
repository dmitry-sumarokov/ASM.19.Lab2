# from group import Group
from flask import Flask
from flask import g
from StudentAbstract import Group

app = Flask(__name__)

group = Group()


@app.route("/")
def index():
    return group.printHeader() + group.ShowGroup()

@app.route("/ShowForm/<int:id>/<int:kind>")
def ShowForm(id, kind):
	return group.printHeader() + group.ShowForm(id, kind)

@app.route("/New", methods=['POST'])
def AddStudent():
	return group.printHeader() + group.AddStudent() + group.PrintFooter()

@app.route("/DeleteStudent/<int:id>/")
def DeleteStudent(id):
	return group.printHeader() + group.DeleteStudent(id) + group.PrintFooter()

@app.route("/DoSpecialAction/<int:id>/")
def DoSpecialAction(id):
	return group.DoSpecialAction(id) + group.PrintFooter()\

@app.route("/EditStudent/<int:id>/<int:kind>")
def EditStudent(id, kind):
	return group.EditStudent(id, kind) + group.PrintFooter()

@app.teardown_appcontext
def finish(ctx):
        group.store()

if __name__ == "__main__":
    app.run(debug=True)


