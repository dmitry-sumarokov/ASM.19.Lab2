from group import group
from group import Employee
from flask import Flask
from flask import g

app = Flask(__name__)

def GetGroup():
		if 'group' not in g:
				g.group = group()
		return g.group

def GetEmployee():
		if 'Employee' not in g:
				g.Employee = Employee()
		return g.Employee

@app.route("/")
def index():
	return GetGroup().PrintHeader() + GetGroup().ShowGroup() + GetGroup().PrintFooter()

@app.route("/EmployeeBehaviour/<int:id>/<int:f>")
def EmployeeBehaviour(id, f):
	return GetGroup().PrintHeader() + GetGroup().EmployeeBehaviour(id, f) + GetGroup().PrintFooter()

@app.route("/ShowForm/<int:id>")
def ShowForm(id):
	return GetGroup().PrintHeader() + GetGroup().ShowForm(id) + GetGroup().PrintFooter()

@app.route("/DeleteItem/<int:id>")
def DeleteItem(id):
	return GetGroup().PrintHeader() + GetGroup().DeleteItem(id) + GetGroup().PrintFooter()

@app.route("/AddItemLeader", methods=['POST'])
def AddItemLeader():
	return GetGroup().PrintHeader() + GetGroup().AddItemLeader() + GetGroup().PrintFooter()

@app.route("/AddItemManager", methods=['POST'])
def AddItemManager():
	return GetGroup().PrintHeader() + GetGroup().AddItemManager() + GetGroup().PrintFooter()

@app.route("/AddItemAssistant", methods=['POST'])
def AddItemAssistant():
	return GetGroup().PrintHeader() + GetGroup().AddItemAssistant() + GetGroup().PrintFooter()

@app.teardown_appcontext
def finish(ctx):
		GetGroup().store()


if __name__ == "__main__":
	app.run(debug=True)
