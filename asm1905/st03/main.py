from shop import Shop
from flask import Flask
from flask import render_template
from flask import g

app = Flask(__name__)

Furniture = Shop()

@app.route("/")
def index():
	return Furniture.PrintHeader() + Furniture.ShowItems()

@app.route("/DeleteItem/<int:id>")
def DeleteItem(id):
	return Furniture.PrintHeader() + Furniture.DeleteItem(id)

@app.route("/DeleteAll")
def DeleteAll():
	return Furniture.PrintHeader() + Furniture.DeleteAll()

@app.route("/Edit/<int:id>")
def Edit(id):
	return Furniture.PrintHeader() + Furniture.Edit(id)

@app.route("/Submenu/")
def Submenu():
	return render_template("submenu.tpl")

@app.route("/AddItem/<int:type>")
def AddItem(type):
        return Furniture.AddItem(type)

@app.route("/Add/<int:type>", methods=['POST'])
def Add(type):
        return Furniture.PrintHeader() + Furniture.Add(type)

@app.teardown_appcontext
def finish(ctx):
        Furniture.store()
       
if __name__ == "__main__":
	app.run(debug=False)