from group import group
from group import Human
from flask import Flask
from flask import g

app = Flask(__name__)

def GetGroup():
        if 'group' not in g:
                g.group = group()              
        return g.group

def GetHuman():
        if 'humen' not in g:
                g.human = Human()              
        return g.human
    
@app.route("/")
def index():
	return GetGroup().PrintHeader() + GetGroup().ShowGroup() + GetGroup().PrintFooter()

@app.route("/HumanBehaviour/<int:id>/<int:f>")
def HumanBehaviour(id, f): 
    return GetGroup().PrintHeader() + GetGroup().HumanBehaviour(id, f) + GetGroup().PrintFooter()

@app.route("/ShowForm/<int:id>")
def ShowForm(id):
	return GetGroup().PrintHeader() + GetGroup().ShowForm(id) + GetGroup().PrintFooter()

@app.route("/DeleteItem/<int:id>")
def DeleteItem(id):
	return GetGroup().PrintHeader() + GetGroup().DeleteItem(id) + GetGroup().PrintFooter()

@app.route("/AddItemStudent", methods=['POST'])
def AddItemStudent():
	return GetGroup().PrintHeader() + GetGroup().AddItemStudent() + GetGroup().PrintFooter()

@app.route("/AddItemStarosta", methods=['POST'])
def AddItemStarosta():
	return GetGroup().PrintHeader() + GetGroup().AddItemStarosta() + GetGroup().PrintFooter()

@app.route("/AddItemProforg", methods=['POST'])
def AddItemProforg():
	return GetGroup().PrintHeader() + GetGroup().AddItemProforg() + GetGroup().PrintFooter()

@app.teardown_appcontext
def finish(ctx):
        GetGroup().store()

       
if __name__ == "__main__":
	app.run(debug=True)
