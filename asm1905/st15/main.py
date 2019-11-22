from group import group
from group import Workman
from flask import Flask
from flask import g

app = Flask(__name__)

def GetGroup():
		if 'group' not in g:
				g.group = group()			   
		return g.group

def GetWorkman():
		if 'Workman' not in g:
				g.Workman = Workman()				 
		return g.Workman
	
@app.route("/")
def index():
	return GetGroup().PrintHeader() + GetGroup().ShowGroup() + GetGroup().PrintFooter()

@app.route("/WorkmanBehaviour/<int:id>/<int:f>")
def WorkmanBehaviour(id, f): 
	return GetGroup().PrintHeader() + GetGroup().WorkmanBehaviour(id, f) + GetGroup().PrintFooter()

@app.route("/ShowForm/<int:id>")
def ShowForm(id):
	return GetGroup().PrintHeader() + GetGroup().ShowForm(id) + GetGroup().PrintFooter()

@app.route("/DeleteItem/<int:id>")
def DeleteItem(id):
	return GetGroup().PrintHeader() + GetGroup().DeleteItem(id) + GetGroup().PrintFooter()

@app.route("/AddItemMechanic", methods=['POST'])
def AddItemMechanic():
	return GetGroup().PrintHeader() + GetGroup().AddItemMechanic() + GetGroup().PrintFooter()

@app.route("/AddItemMainEngineer", methods=['POST'])
def AddItemMainEngineer():
	return GetGroup().PrintHeader() + GetGroup().AddItemMainEngineer() + GetGroup().PrintFooter()

@app.route("/AddItemSecurity", methods=['POST'])
def AddItemSecurity():
	return GetGroup().PrintHeader() + GetGroup().AddItemSecurity() + GetGroup().PrintFooter()

@app.teardown_appcontext
def finish(ctx):
		GetGroup().store()

	   
if __name__ == "__main__":
	app.run(debug=True)