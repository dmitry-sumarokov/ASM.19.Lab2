from group import group
from group import Worker
from flask import Flask
from flask import g

app = Flask(__name__)

def GetGroup():
		if 'group' not in g:
				g.group = group()			   
		return g.group

def GetWorker():
		if 'Worker' not in g:
				g.Worker = Worker()				 
		return g.Worker
	
@app.route("/")
def index():
	return GetGroup().PrintHeader() + GetGroup().ShowGroup() + GetGroup().PrintFooter()

@app.route("/WorkerBehaviour/<int:id>/<int:f>")
def WorkerBehaviour(id, f): 
	return GetGroup().PrintHeader() + GetGroup().WorkerBehaviour(id, f) + GetGroup().PrintFooter()

@app.route("/ShowForm/<int:id>")
def ShowForm(id):
	return GetGroup().PrintHeader() + GetGroup().ShowForm(id) + GetGroup().PrintFooter()

@app.route("/DeleteItem/<int:id>")
def DeleteItem(id):
	return GetGroup().PrintHeader() + GetGroup().DeleteItem(id) + GetGroup().PrintFooter()

@app.route("/AddItemSeller", methods=['POST'])
def AddItemSeller():
	return GetGroup().PrintHeader() + GetGroup().AddItemSeller() + GetGroup().PrintFooter()

@app.route("/AddItemManager", methods=['POST'])
def AddItemManager():
	return GetGroup().PrintHeader() + GetGroup().AddItemManager() + GetGroup().PrintFooter()

@app.route("/AddItemCleaner", methods=['POST'])
def AddItemCleaner():
	return GetGroup().PrintHeader() + GetGroup().AddItemCleaner() + GetGroup().PrintFooter()

@app.teardown_appcontext
def finish(ctx):
		GetGroup().store()

	   
if __name__ == "__main__":
	app.run(debug=True)