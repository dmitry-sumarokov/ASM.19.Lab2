from worker import worker
from flask import Flask
from flask import g

app = Flask(__name__)

def GetWorker():
        if 'worker' not in g:
                g.worker = worker()              
        return g.worker
    
@app.route("/")
def index():
	return GetWorker().PrintHeader() + GetWorker().ShowWorker() + GetWorker().PrintFooter()

@app.route("/WorkerBehaviour/<int:id>/<int:f>")
def WorkerBehaviour(id, f): 
    return GetWorker().PrintHeader() + GetWorker().WorkerBehaviour(id, f) + GetWorker().PrintFooter()

@app.route("/ShowForm/<int:id>")
def ShowForm(id):
	return GetWorker().PrintHeader() + GetWorker().ShowForm(id) + GetWorker().PrintFooter()

@app.route("/DeleteItem/<int:id>")
def DeleteItem(id):
	return GetWorker().PrintHeader() + GetWorker().DeleteItem(id) + GetWorker().PrintFooter()

@app.route("/AddItemDriller", methods=['POST'])
def AddItemDriller():
	return GetWorker().PrintHeader() + GetWorker().AddItemDriller() + GetWorker().PrintFooter()

@app.route("/AddItemGeologist", methods=['POST'])
def AddItemGeologist():
	return GetWorker().PrintHeader() + GetWorker().AddItemGeologist() + GetWorker().PrintFooter()

@app.route("/AddItemDeveloper", methods=['POST'])
def AddItemDeveloper():
	return GetWorker().PrintHeader() + GetWorker().AddItemDeveloper() + GetWorker().PrintFooter()

@app.teardown_appcontext
def finish(ctx):
        GetWorker().store()

       
if __name__ == "__main__":
	app.run(debug=True)
