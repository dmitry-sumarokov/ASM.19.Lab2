if __name__ == '__main__':
    from group import Group
else:
    from .group import Group

from flask import Flask

from flask import g
app = Flask(__name__)
ctx=app.app_context()
ctx.g.cur_group = Group()
ctx.push()

def GetGroup():
    return ctx.g.cur_group
@app.route("/")
def index():
	return GetGroup().PrintHeader() + GetGroup().print_group() + GetGroup().PrintFooter()

@app.route("/ShowForm/<id>")
def ShowForm(id):
	return GetGroup().PrintHeader() + GetGroup().change_Technic(int(id)) + GetGroup().PrintFooter()

@app.route("/DeleteItem/<int:id>")
def DeleteItem(id):
	return GetGroup().PrintHeader() + GetGroup().remove_Technic(id) + GetGroup().PrintFooter()

@app.route("/ShowMagicForm/<int:id>")
def ShowMagicForm(id):
	return GetGroup().PrintHeader() + GetGroup().do_it(id) + GetGroup().PrintFooter()

@app.route("/DeleteGroup")
def DeleteGroup():
	return GetGroup().PrintHeader() + GetGroup().clear_Technic() + GetGroup().PrintFooter()

@app.route("/AddItem", methods=['POST'])
def AddItem():
	return GetGroup().PrintHeader() + GetGroup().add_Technic() + GetGroup().PrintFooter()

	
@app.route("/load")
def load():
    return GetGroup().PrintHeader() + GetGroup().load_from_file() + GetGroup().PrintFooter()
	
@app.route("/save")
def save():
    return GetGroup().PrintHeader() + GetGroup().save_to_file() + GetGroup().PrintFooter()


       
if __name__ == "__main__":
	app.run(debug=True)
