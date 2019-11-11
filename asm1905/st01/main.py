if __name__ == '__main__':
    from nursery import Nursery
else:
    from .nursery import Nursery

from flask import Flask
from flask import g



app = Flask(__name__)

def GetNursery():
        if 'Nursery' not in g:
                g.Nursery = Nursery()
        return g.Nursery

@app.route("/")
def index():
	return GetNursery().print_cats()

@app.route("/ShowForm/<id>")
def ShowForm(id):
	return GetNursery().change_cat(int(id))

@app.route("/DeleteItem/<int:id>")
def DeleteItem(id):
	return GetNursery().remove_the_cat(id)

@app.route("/DoMeow/<int:id>")
def DoMeow(id):
	return GetNursery().do_special_meow(id)

@app.route("/ClearList")
def ClearNursery():
	return GetNursery().clear_cats_list()

@app.route("/AddItem", methods=['POST'])
def AddItem():
	return GetNursery().add_cat()

@app.teardown_appcontext
def finish(ctx):
        GetNursery().save_to_file()

       
if __name__ == "__main__":
	app.run(debug=True)
